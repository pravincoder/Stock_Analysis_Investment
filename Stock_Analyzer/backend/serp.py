from serpapi import search

import os
from langchain.tools import tool

SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

params_search = {"engine": "google", "api_key": SERPAPI_API_KEY}
params_news = {"engine": "google_news", "api_key": SERPAPI_API_KEY}
params_finance = {"engine": "google_finance", "api_key": SERPAPI_API_KEY}


class SerpApi:
    @tool("Stock Details")
    def stock_details(stock: str):
        """Get stock details from the SERP API
        Args:
            stock (str): The stock name
        Returns:
            dict: The stock details"""

        params_search["q"] = stock.get("title")
        sear = search(params_search)
        results = sear.get("knowledge_graph")
        return results

    @tool("Stock News")
    def stock_news(stock: str, num_articles: int):
        """Get stock news from the SERP API
        Args:
            stock (str): The stock name
            num_articles (int): The number of articles to return
        Returns:
            list: The list of news articles"""

        params_news["q"] = stock
        sear = search(params_news)
        results = sear.as_dict().get("news_results")
        extracted_data = []
        if results:
            for article in results[:num_articles]:
                extracted_article = {
                    "title": article.get("title"),
                    "source": article.get("source"),
                    "date": article.get("date"),
                }
                extracted_data.append(extracted_article)
        else:
            extracted_data = {"error": "No news found"}
        return extracted_data

    @tool("Stock Market Data")
    def stock_market_data(stock: str):
        """Get stock market data from the SERP API
        Args:
            stock (str): The stock name
        Returns:
            dict: The stock market data"""
        params_finance["q"] = stock
        sear = search(params_finance)
        results = sear.as_dict()
        if results:
            market = results.get("markets")
            asia_market = market.get("asia")
            us_market = market.get("us")
            futures = results.get("futures")
            futures_chain = results.get("futures_chain")
            data = {
                "asia_market": asia_market,
                "us_market": us_market,
                "futures": futures,
                "futures_chain": futures_chain,
            }
        else:
            data = {"error": "No market data found"}
        return data

    @tool("Stock Financials")
    def stock_financials(stock: str):
        """Get stock financials from the SERP API
        Args:
            stock (str): The stock name
        Returns:
            dict: The stock financials"""

        params_search["q"] = f"{stock} stock financials"
        sear = search(params_search)
        results = sear.as_dict()
        knowledge_graph = results.get("knowledge_graph")
        if knowledge_graph:
            financials = knowledge_graph.get("financials")
            answer_box = results.get("answer_box")
            data = {"financials": financials, "answer_box_data": answer_box}
        else:
            data = {"error": "No financial data available"}
        return data

    def tools():
        return [
            SerpApi.stock_details,
            SerpApi.stock_news,
            SerpApi.stock_market_data,
            SerpApi.stock_financials,
        ]
