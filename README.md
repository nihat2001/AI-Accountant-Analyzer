📊 **AI Accountant Analyzer**
AI Accountant Analyzer is a smart financial tracking and analysis platform that leverages the Groq AI (Llama 3.3) engine to transform raw financial data into professional insights. It acts as your personal digital accountant, identifying trends, detecting anomalies, and providing actionable business recommendations.

The project features a dual-interface system: a lightweight CLI (Command Line Interface) for quick data entry and a high-end Streamlit Dashboard for deep visual analysis.

🚀 **Key Features**
AI-Powered Analysis: Uses the Llama-3.3-70b-versatile model via Groq Cloud to provide expert-level financial reporting.

Dynamic Visualizations: Automatically generates earnings and profit/loss trend charts using Plotly.

Professional Persona: The AI is fine-tuned as a "Financial Analyst" to provide structured and strategic advice.

Automated Metrics: Instantly calculates net profit, profit margins, and cumulative totals.

Hybrid Interaction: Choose between a fast terminal workflow or an interactive web-based dashboard.

🛠️ **Tech Stack**
Python (Core Logic)

Streamlit (Web Interface)

Groq AI API (Inference Engine)

Plotly & Pandas (Data Processing & Visualization)

Python-Dotenv (Secure Environment Management)

📂 **Project Structure**
ai_side.py: The core logic for Groq API integration and the "Financial Analyst" system prompt.

main.py: The terminal-based (CLI) version for interactive data processing.

app.py: The modern Streamlit dashboard featuring visual trends and real-time data metrics.

.env: Secret file for storing your Groq API keys (excluded via .gitignore).

📖 **How to Use**
Input Data: Use the Sidebar to enter the Period Name (e.g., January 2026), Earnings, and Spending.

Add Entry: Click the "Add Period" button to populate your financial ledger.

Generate Report: Click "Generate AI Analysis & Trend Report" to trigger the AI inference and render the charts.

Review Insights: Read the AI-generated report for professional advice on your financial health and future projections.

⚠️ **Disclaimer** 
This application is intended for informational purposes only and does not constitute official financial advice.
