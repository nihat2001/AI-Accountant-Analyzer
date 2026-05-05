from ai_side import analyze_financials

def main():
    periods = [] 
    
    print("🚀 AI Accountant Analitic started to process...")
    
    while True:
        period_name = input("\nPeriod (example: January) or for finish write 'ok': ")
        if period_name.lower() == 'ok':
            break
            
        try:
            earning = float(input("Earning: "))
            spending = float(input("Spending: "))
            profit = earning - spending 
            
            data = {
                "Period": period_name,
                "Earning": earning,
                "Spending": spending,
                "Profit": profit
            }
            periods.append(data)
        except ValueError:
            print("❌ Please use only numbers!")

    if len(periods) > 0:
        print("\n📊 AI analyze informations...")
        result = analyze_financials(periods)
        
        print("\n" + "="*40)
        print("Financial Analysis Report")
        print("="*40)
        print(result)
    else:
        print("Information not entered.")

if __name__ == "__main__":
    main()

