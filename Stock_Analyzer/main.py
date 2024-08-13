import logging
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS
from crewai import Crew
from task import Stock_bot
from agents import Stock_bot_agents
import requests

app = Flask(__name__)
CORS(app)

def get_stock_symbol(stock_name):
    """Fetch the stock symbol from Yahoo Finance"""
    try:
        stock_name = stock_name.replace(" ", "")
        url = "https://query2.finance.yahoo.com/v1/finance/search"
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        params = {"q": stock_name, "quotes_count": 1}
        res = requests.get(url=url, params=params, headers={"User-Agent": user_agent})
        res.raise_for_status()  # This will raise an exception for HTTP errors
        data = res.json()
        stock_symbol = data["quotes"][0]["symbol"]
        return stock_symbol
    except (requests.RequestException, IndexError) as e:
        logging.error(f"Failed to fetch stock symbol for {stock_name}: {e}")
        return None

def generate_reports(stock_symbol):
    """Generate stock analysis and investment analysis reports"""
    tasks = Stock_bot()
    agent = Stock_bot_agents()

    # Create agents
    stock_analysis = agent.stock_analysis(stock_symbol)
    investment_analysis = agent.investment_analysis(stock_symbol)

    # Create tasks
    stock_analysis_task = tasks.stock_analysis(stock_analysis, stock_symbol)
    investment_analysis_task = tasks.investment_analysis(investment_analysis, stock_symbol)

    # Execute tasks
    stock_analysis_crew = Crew(
        agents=[stock_analysis],
        tasks=[stock_analysis_task],
        verbose=True,
        max_rpm=29,
    )

    investment_analysis_crew = Crew(
        agents=[investment_analysis],
        tasks=[investment_analysis_task],
        verbose=True,
        max_rpm=29,
    )

    result_stock_analysis = stock_analysis_crew.kickoff()
    result_investment_analysis = investment_analysis_crew.kickoff()

    return str(result_stock_analysis), str(result_investment_analysis)

@app.route('/analyze-stock', methods=['POST'])
def analyze_stock():
    """API endpoint to analyze a stock and return reports in Markdown format"""
    data = request.get_json()
    stock_name = data.get("stock_name")
    logging.info(f"Received request to analyze stock: {stock_name}")

    if not stock_name:
        return jsonify({"error": "Stock name is required"}), 400

    stock_symbol = get_stock_symbol(stock_name)
    if not stock_symbol:
        return jsonify({"error": "Stock symbol not found"}), 404

    stock_report, investment_report = generate_reports(stock_symbol)

    return jsonify({
        "stock_report": stock_report,
        "investment_report": investment_report
    })

if __name__ == "__main__":
    load_dotenv()
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True)
