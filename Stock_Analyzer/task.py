from textwrap import dedent
from crewai import Task
  

class Stock_bot:
    # Stock Analysis Tasks
    def stock_analysis(self, agent, stock_name):
        return Task(
            description=dedent(
                f"""
            As a Senior Stock Analyst at Goldman Sachs, your task is to produce a comprehensive and 
            professional report analyzing the stock performance of {stock_name}.
            Important Tip :- Read the recieved json data and extract the required information to generate the report.
            Report Structure :- 
            #Stock Analysis Report: {stock_name}
            ## Basic Information:
            -Length: 
                -Maximum 200 words in concise paragraphs.
            -Data Presentation:
                -Provide a table with the following details: Stock Name, Sector, Market Cap (in Crores), P/E Ratio, EPS, Dividend Yield, and Average Volume (in Thousands).
                -Formatting:
                    -Ensure Market Cap is in Crores, P/E Ratio, EPS, and Dividend Yield are rounded to two decimal places.
                    -Average Volume should be displayed in Thousands.
                (Note: If any data point is missing, exclude it without affecting the report's quality.)
            ## News Analysis:
            -Content: 
                -Summarize the latest news related to the stock.
                -Table Format:
                    -Include Date, News Title, Brief Description, and an optional article link formatted as a Markdown link.
            ## Events Analysis:
            -Content: Analyze upcoming or significant past events related to the stock.
                -Table Format:
                    -Include Date, Event Title, and Description (e.g., dividends, earnings reports).
            ## Trend Analysis:
            -Time Frame: Focus on the past 3 months.
            -Content: Analyze trends using key indicators like SMA, EMA, RSI, and MACD.
                -Table Format:
                    -Include indicators with corresponding trends and suggest Buy/Sell/Hold signals.
                    -Add the Current Price, 52-Week High/Low, Volume, and Average Volume of the stock.
            ## Financial Table:
            -Content: 
                -Present key financial metrics such as Revenue, Net Income, Operating Income, etc.
                -Table Format: 
                    -Clear and structured, focusing on essential data.
            ## Financial Analysis:
            -Content:  
                -Provide an in-depth analysis of the stock's financials based on data from the Financial Agent.
                -Table Format: 
                    -Highlight critical insights derived from the financial metrics.
            ## Conclusion:
            -Content: Offer a concise summary of the stock's outlook.
                -Format:
                    -Short-Term View: Bullet points, max 100 words.
                    -Long-Term View: Bullet points, max 100 words.
        You will be paid a large bonus if your complete report is accurate and well-structured.

                    """
            ),
            expected_output=dedent(
                f"""
            A detailed stock analysis of the {stock_name} stock.
            The analysis should include the following:
            # Stock Analysis Report :- {stock_name}
            ## Basic Info
            ## News Analysis
            ## Trend Analysis
            ## Financial Analysis
            ## Conclusion
            Complete the report in MarkDown Format.
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
            As a Senior Investment Analyst at Goldman Sachs, 
            your task is to develop a detailed report analyzing the investment potential 
            of {stock_name}.
            Important Tip :- Read the recieved json data and extract the required information to generate the report.
            Report Structure:
            # Investment Analysis Report: {stock_name}
            ## Pros/Positives:
            -Content: 
                -Highlight the key advantages and strengths of the stock.
                -Format:
                    -Present in bullet points.
                    -Length: 
                        -Maximum 200 words.
            ## Cons/Negatives:
            Content: 
                -Identify the main drawbacks or risks associated with the stock.
                -Format:
                    -Present in bullet points.
                    -Length: 
                        -Maximum 200 words.
            ## Future Prospects:
            Content: 
                -Discuss potential growth opportunities and future developments for the stock.
                -Format:
                    -Present in bullet points.
                    -Length: 
                        -Maximum 200 words.
            ## Risk Analysis:
            Content: 
                -Evaluate the risks associated with investing in the stock.
                -Format:
                    -Present in bullet points.
                    -Length: 
                        -Maximum 200 words.
            ## Recommendation:
            Content: 
                -Provide a clear investment recommendation.
                -Format:
                    -Highlight the recommendation (Buy/Sell/Hold) based on the current market value.
                    -Explanation: 
                        -Justify the recommendation in 50-100 words.
                        -Include key factors influencing the decision.
        Note :- Do Not include Disclaimers and Warnings in the report.
        You will be paid a large bonus if your report is accurate and well-structured.
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