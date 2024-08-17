from textwrap import dedent
from crewai import Task
  

class Stock_bot:
    # Stock Analysis Tasks
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
                STOCK NAME, SECTOR, MARKET CAP, P/E RATIO, EPS, DIVIDEND YIELD AND AVERAGE VOLUME OF THE STOCK
                Note :- The Market Cap should be in Crores, P/E Ratio, EPS and Dividend Yield should be upto 2 decimal places and Average Volume should be in Thousands.If some thing is missing then just ignore it.) 
                ## News Analysis
                (REQUIREMENTS:- The Latest News of the stock we are analysising in Table with the date.
                - News must have a Title and a small Description. Article link if present in a .md link format.)
                ## Events Analysis
                (The Upcomming if any  or include passed major events,dividents,etc of the stock in Table with the date.)
                ## Trend Analysis
                (REQUIREMENTS:- Try to include the trend analysis of the stock for the past 3 months , by reading various indicator
                - Make a Table that include 3 months trends based on the indicators like SMA,EMA,RSI,MACD,etc.
                - Include the Buy/Sell/Hold Signal based on the indicators.
                - Include the Current Price and the 52 Week High and Low Price of the stock.
                - Include the Volume of the stock and the Average Volume of the stock.)
                ## Financial Table
                (REQUIREMENTS:- A TABLE THAT HAS THE All The Important and Key Financial Metrics of the stock like Revenue,Net Income,Operating Income,etc)
                ## Financial Analysis
                (REQUIREMENTS:- Make a Table that include the Financial Analysis of the stock for the past 3 years)
                ## CONCLUSION
                (REQUIREMENTS:- Must Include a Short and Long Term view seperatly highlighted in points, NOT MORE THAN 200 WORDS for Both point)"""
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
    
    # Investment Analysis Tasks
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
