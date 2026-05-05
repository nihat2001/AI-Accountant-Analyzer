from groq import Groq
import os 
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key = os.getenv("api_key"))

def analyze_financials(periods_data):
    
    data_summary = ""
    for item in periods_data:
       
        status = "profitable" if item['Profit'] > 0 else ("Unprofitable" if item['Profit'] < 0 else "In balance")
        
        data_summary += f"- {item['Period']}: Earning {item['Earning']}, Spending {item['Spending']}, Profit {item['Profit']} ({status})\n"

    completion = client.chat.completions.create(
        model= "llama-3.3-70b-versatile", 
        messages=[
            {
                "role": "system",
                "content": """You are a professional Financial Analyst. 
                                    Your task is to analyze financial data, 
                                            identify trends, detect anomalies, 
                                                and provide future projections and actionable recommendations."""
            },
            {
                "role": "user",
                "content": f"Please analyze the following financial metrics:\n{data_summary}"
            }
        ],
        temperature=0.7,
        max_tokens=1024
    )
    
    return completion.choices[0].message.content
