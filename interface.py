import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from groq import Groq
import os 
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Accountant", page_icon="📊", layout="wide")


client = Groq(api_key = os.getenv("api_key"))

def analyze_financials(periods_data):
    data_summary = ""
    for item in periods_data:
        status = "profitable" if item['Profit'] > 0 else ("Unprofitable" if item['Profit'] < 0 else "In balance")
        data_summary += f"- {item['Period']}: Earning {item['Earning']}, Spending {item['Spending']}, Profit {item['Profit']} ({status})\n"

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a professional Financial Analyst. Analyze trends, detect anomalies, and provide actionable recommendations."},
                {"role": "user", "content": f"Please analyze the following financial metrics:\n{data_summary}"}
            ],
            temperature=0.7,
            max_tokens=1024
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error connecting to AI: {str(e)}"


def create_static_graph(df, y_col, name, color, title):
    axis_style = dict(
        gridcolor='#D0D7DE',
        linecolor='#333333',
        linewidth=1,
        mirror=True
    )

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df['Period'], 
        y=df[y_col], 
        name=name,
        mode='lines+markers',
        line=dict(color=color, width=3.5),
        marker=dict(color=color, size=12, symbol='circle'),
        hoverinfo='skip'
    ))

    fig.update_layout(
        title=dict(text=title, font=dict(color='#333333')),
        xaxis=axis_style,
        yaxis=axis_style,
        plot_bgcolor='white',
        margin=dict(l=40, r=40, t=60, b=40),
        height=380,
        showlegend=False
    )

    config = {
        'displayModeBar': False,
        'scrollZoom': False,
        'staticPlot': True
    }

    st.plotly_chart(fig, use_container_width=True, config=config)


if 'period_list' not in st.session_state:
    st.session_state.period_list = []
if 'report_generated' not in st.session_state:
    st.session_state.report_generated = False
if 'ai_report_content' not in st.session_state:
    st.session_state.ai_report_content = ""


st.title("🚀 AI Accountant Analyzer")


with st.sidebar:
    st.header("📝 Input Financial Data")
    
    
    period = st.text_input("Period Name", placeholder="e.g., January 2026 or Q1")
    earning = st.number_input("Earning ($)", min_value=0.0, step=10.0, format="%.2f")
    spending = st.number_input("Spending ($)", min_value=0.0, step=10.0, format="%.2f")
    
    current_profit = earning - spending
    st.info(f"Calculated Profit: ${current_profit:,.2f}")

    if st.button("➕ Add Period", use_container_width=True, type="primary"):
        if period:
            new_entry = {
                "Period": period,
                "Earning": earning,
                "Spending": spending,
                "Profit": current_profit
            }
            st.session_state.period_list.append(new_entry)
            st.session_state.report_generated = False 
            st.toast(f"✅ {period} added!")
        else:
            st.error("Please enter a Period Name.")

    st.markdown("---")
    if st.button("🗑️ Clear All Data", use_container_width=True):
        st.session_state.period_list = []
        st.session_state.report_generated = False
        st.session_state.ai_report_content = ""
        st.rerun()


if len(st.session_state.period_list) > 0:
    df = pd.DataFrame(st.session_state.period_list)

    # 1. TOP METRICS
    m1, m2, m3 = st.columns(3)
    total_e = df['Earning'].sum()
    total_s = df['Spending'].sum()
    total_p = df['Profit'].sum()
    
    m1.metric("Total Earning", f"${total_e:,.2f}")
    m2.metric("Total Spending", f"${total_s:,.2f}")
    m3.metric("Net Profit", f"${total_p:,.2f}", delta=f"{(total_p/total_e*100 if total_e !=0 else 0):.1f}% Margin")

    col_left, col_right = st.columns([1, 1.8])
    
    with col_left:
        st.subheader("📊 Data Table")
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        if st.button("🔍 Generate AI Analysis & Trend Report", use_container_width=True, type="primary"):
            with st.spinner("Analyzing and plotting..."):
                st.session_state.ai_report_content = analyze_financials(st.session_state.period_list)
                st.session_state.report_generated = True

    with col_right:
        if st.session_state.report_generated:
            st.subheader("📊 Trend Visualizations")
            tab1, tab2 = st.tabs(["Earning Trend", "Profit/Loss Movement"])

            blue_line_color = '#0D47A1'

            with tab1:
                st.markdown("##### Earning Progress Over Periods")
                create_static_graph(df, 'Earning', 'Earning', blue_line_color, "Total Earnings")

            with tab2:
                st.markdown("##### Net Profit Growth/Decline")
                create_static_graph(df, 'Profit', 'Profit', blue_line_color, "Total Profit")

            st.subheader("🤖 AI Financial Insight")
            st.info("The report below is generated based on your ledger trends.")
            st.markdown(st.session_state.ai_report_content)
        else:
            st.write("### 👈 Click 'Generate' to see charts and AI insights.")
            st.caption("Visual trends and professional analysis will appear here once triggered.")

else:
    
    st.info("👋 Welcome! Please enter financial data in the sidebar to begin.")
    st.image("https://cdn-icons-png.flaticon.com/512/2652/2652234.png", width=120)
    st.markdown("""
    ### Get Started
    1. Enter your **Period** and **Amounts** in the sidebar.
    2. Click **Add Period** for each entry.
    3. Use the **Generate** button to create a professional financial report.
    """)

st.markdown("---")
st.caption("AI Accountant Analyzer | Designed by NIHAT")

