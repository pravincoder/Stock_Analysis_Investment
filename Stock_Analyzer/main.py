import logging
from dotenv import load_dotenv
from crewai import Crew
from task import Stock_bot
from agents import Stock_bot_agents
import requests

def main():
    load_dotenv()

    print("#### -----WELCOME TO STOCK Investment and Analysis BOT -----####")
    print("------_____________________________________------")
    print("Enter the stock name you want to analyze Ex :- Apple,TCS,Tata Motors etc :-")
    
    stock = input()
    print(f"Stock name entered: {stock}")

    # Get Stock Symbol
    try:
        # Strip the stock name of any leading or trailing whitespaces
        stock = stock.replace(" ", "")
        print(f"Searching for Stock Symbol of {stock}....")
        url = "https://query2.finance.yahoo.com/v1/finance/search"
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        params = {"q": stock, "quotes_count": 1}
        res = requests.get(url=url, params=params, headers={'User-Agent': user_agent})
        data = res.json()
        stock_symbol = data['quotes'][0]['symbol']
        print(f"Stock Symbol: {stock_symbol}")
    except: 
        print("Stock Symbol not found")
        
    tasks = Stock_bot()
    agent = Stock_bot_agents()

    # Create agents
    stock_analysis = agent.stock_anaylsis()
    investment_analysis = agent.investment_analysis()

    # Create tasks
    stock_analysis_task = tasks.stock_analysis(stock_analysis,stock_symbol)
    investment_analysis_task = tasks.investment_analysis(investment_analysis,stock_symbol)
    # Execute tasks
    print("Creating Crew instance >>>>")
    
    stock_analysis_crew = Crew(
        agents=[
            stock_analysis,
        ],
        tasks=[
            stock_analysis_task,
        ],verbose=True,max_rpm=29
    )

    investment_analysis_crew = Crew(
        agents=[
            investment_analysis,
        ],
        tasks=[
            investment_analysis_task,
        ],verbose=True,max_rpm=29
    )   
    result_stock_analysis = stock_analysis_crew.kickoff()
    print(result_stock_analysis)
    # Save the result in a md file
    result_stock_analysis = str(result_stock_analysis)
    with open(f"../Generated_reports/stock_analysis_{stock}.md", "w") as file:
        file.write(result_stock_analysis)
    result_investment_analysis = investment_analysis_crew.kickoff()
    print(result_investment_analysis)
    # Save the result in a md file  
    result_investment_analysis = str(result_investment_analysis)
    with open(f"../Generated_reports/investment_analysis_{stock}.md", "w") as file:
        file.write(result_investment_analysis)

    print("#### ------ THANK YOU FOR USING STOCK ANALYSIS BOT ------####")

    
if __name__ == '__main__':
    main()
    