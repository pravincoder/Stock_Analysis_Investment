from textwrap import dedent
from crewai import Task
  


class Stock_bot:
    

    def stock_analysis(self, agent, stock_name):
        return Task(
            description=dedent(
                f"""
            As a stock analyst you are working for a Goldman Sachs company.
            you have been assigned to create a report of the analysis of the {stock_name} stock.
            FOR LARGE NUMBER LIKE 345634760 AS 3.4 CORERS,LIKEWISE FOR LAKHS AND THOUSANDS IN THE BELOW REPORT.
            The report Template :- 
                # Title :- Stock Analysis Report of {stock_name}
                ## Basic Info
                (REQUIREMENTS:- NOT MORE THAN 200 WORDS  IN PARAGRAPHS) 
                (REQUIREMENTS:- A TABLE THAT HAS THE FOLLOWING DETAILS
                STOCK NAME, SECTOR, MARKET CAP, P/E RATIO, EPS, DIVIDEND YIELD and there meaning in table format)
                ## News Analysis
                (REQUIREMENTS:- Top 5 news of the stock in bullet points with the date,link of news and source of the news and the impact on the stock price(if possible).
                ## Events Analysis
                (The Upcomming and passed major events,dividents,etc of the stock in Table with the date.)
                ## Trend Analysis
                (REQUIREMENTS:- Try to include the trend analysis of the stock for the past 3 months , by reading various indicator data like EMA,RSI,etc and give a brief of what you think.)
                ## Financial Table
                (REQUIREMENTS:- A TABLE THAT HAS THE All The Import and Key Financial Metrics of the stock like Revenue,Net Income,Operating Income,etc)
                ## Financial Analysis
                (REQUIREMENTS:- NOT MORE THAN 200 WORDS  IN PARAGRAPHS)
                ## CONCLUSION
                (REQUIREMENTS:- Must Include a Short and Long Term view for investment , NOT MORE THAN 200 WORDS  IN PARAGRAPHS)"""
            ),
            expected_output=dedent(
                f"""
            A detailed stock analysis of the {stock_name} stock.
            The analysis should include the following:
            - Title :- Stock Analysis Report of {stock_name}
            - Basic Info
            - News Analysis
            - Trend Analysis
            - Financial Analysis
            - Conclusion
        """
            ),
            verbose=True,
            agent=agent,
            
        )

    def investment_analysis(self, agent, stock_name):
        return Task(
            description=dedent(
                f"""
            As a stock analyst you are working for a Goldman Sachs company.
            you have been assigned to create a report of the analysis of the stock.
            The report Template :- 
                # Title :- Investment Analysis Report of {stock_name}
                ## Pros/Positives :-
                (REQUIREMENTS:- NOT MORE THAN 200 WORDS  IN BULLET POINTS)
                ## Cons/Negatives :-
                (REQUIREMENTS:- NOT MORE THAN 200 WORDS  IN BULLET POINTS)
                ## Future Prospects :-
                (REQUIREMENTS:- NOT MORE THAN 200 WORDS  IN BULLET POINTS)
                ## Risk Analysis :-
                (REQUIREMENTS:- NOT MORE THAN 200 WORDS  IN BULLET POINTS)
                ## Remommendation
                (REQUIREMENTS:- STATE BUY/SELL/HOLD based on Current Value,market and Highlight it, EXPLAIN WHY IN 50-100 WORDS)
                NOTE:-Avoid Adding Caution and Disclaimer in the report.
        """
            ),
            expected_output=dedent(
                f"""
            A detailed stock analysis of the {stock_name} stock must be in MarkDown Format.
            The analysis should include the following:
            - Title :- Investment Analysis Report of {stock_name}
            - Pros/Positives
            - Cons/Negatives
            - Future Prospects
            - Risk Analysis
            - Recommendation
            """
            ),
            agent=agent,
            verbose=True,
            
        )
