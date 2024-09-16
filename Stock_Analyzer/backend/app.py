import logging
from dotenv import load_dotenv
from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from crewai import Crew
from task import Stock_bot
from agents import Stock_bot_agents
import requests
from chart_data import ChartData

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Log to console
        logging.FileHandler('app.log')  # Log to file
    ]
)
logger = logging.getLogger(__name__)

def get_stock_symbol(stock_name):
    """Fetch the stock symbol from Yahoo Finance
    
    Args:
        stock_name (str): The name of the stock
    Returns: 
    stock_symbol (str): The stock symbol
    """
    try:
        stock_name = stock_name.replace(" ", "")
        url = "https://query2.finance.yahoo.com/v1/finance/search"
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        params = {"q": stock_name, "quotes_count": 1}
        res = requests.get(url=url, params=params, headers={"User-Agent": user_agent})
        res.raise_for_status()  
        data = res.json()
        stock_symbol = data["quotes"][0]["symbol"]
        logger.info(f"Fetched stock symbol for {stock_name}: {stock_symbol}")
        return stock_symbol
    except (requests.RequestException, IndexError) as e:
        logger.error(f"Failed to fetch stock symbol for {stock_name}: {e}")
        return None

def generate_analysis_reports(stock_symbol):
    """Generate stock analysis reports
    Args:
        stock_symbol (str): The stock symbol
    Returns:
    stock_report (str): The stock analysis report with financial chart
    """
    try:
        tasks = Stock_bot()
        agent = Stock_bot_agents()

        # Create agents
        stock_analysis = agent.stock_analysis(stock_symbol)
        # Create tasks
        stock_analysis_task = tasks.stock_analysis(stock_analysis, stock_symbol)

        # Execute tasks
        stock_analysis_crew = Crew(
            agents=[stock_analysis],
            tasks=[stock_analysis_task],
            verbose=True,
            max_rpm=29,
        )
        result_stock_analysis = stock_analysis_crew.kickoff()

        logger.info(f"Generated analysis report for {stock_symbol}")
        return str(result_stock_analysis)
    except Exception as e:
        logger.error(f"Failed to generate analysis report for {stock_symbol}: {e}")
        return None

def generate_investment_reports(stock_symbol):
    """Generate stock investment reports
    Args:
        stock_symbol (str): The stock symbol
    Returns:
        stock_report (str): The stock investment report
        """
    try:
        tasks = Stock_bot()
        agent = Stock_bot_agents()

        # Create agents
        investment_analysis = agent.investment_analysis(stock_symbol)

        # Create tasks
        investment_analysis_task = tasks.investment_analysis(investment_analysis, stock_symbol)

        # Execute tasks
        investment_analysis_crew = Crew(
            agents=[investment_analysis],
            tasks=[investment_analysis_task],
            verbose=True,
            max_rpm=29,
        )

        result_investment_analysis = investment_analysis_crew.kickoff()

        logger.info(f"Generated investment report for {stock_symbol}")
        return str(result_investment_analysis)
    except Exception as e:
        logger.error(f"Failed to generate investment report for {stock_symbol}: {e}")
        return None

@app.route('/analyze-stock', methods=['POST'])
def analyze_stock():
    """API endpoint to analyze a stock and return reports in Markdown format"""
    data = request.get_json()
    stock_name = data.get("stock_name")
    logger.info(f"Received request to analyze stock: {stock_name}")

    if not stock_name:
        return jsonify({"error": "Stock name is required"}), 400

    stock_symbol = get_stock_symbol(stock_name)
    if not stock_symbol:
        return jsonify({"error": "Stock symbol not found"}), 404

    analysis_report = generate_analysis_reports(stock_symbol)
    
    return jsonify({
        "analysis_report": analysis_report,
    })

@app.route('/chart/<stock_name>', methods=['GET'])
def chart(stock_name):
    """API endpoint to generate and return a stock chart"""
    logger.info(f"Received request to generate chart for stock: {stock_name}")

    if not stock_name:
        return jsonify({"error": "Stock name is required"}), 400

    stock_symbol = get_stock_symbol(stock_name)
    if not stock_symbol:
        return jsonify({"error": "Stock symbol not found"}), 404
    
    try:
        image = ChartData.generate_chart(stock_symbol)
        logger.info(f"Generated chart for {stock_symbol}")
        return send_file(image, mimetype='image/png')
    except Exception as e:
        logger.error(f"Failed to generate chart for {stock_symbol}: {e}")
        return jsonify({"error": "Failed to generate chart"}), 500

@app.route('/invest-stock', methods=['POST'])
def invest_stock():
    """API endpoint to analyze a stock and return investment reports in Markdown format"""
    data = request.get_json()
    stock_name = data.get("stock_name")
    logger.info(f"Received request to invest in stock: {stock_name}")

    if not stock_name:
        return jsonify({"error": "Stock name is required"}), 400

    stock_symbol = get_stock_symbol(stock_name)
    if not stock_symbol:
        return jsonify({"error": "Stock symbol not found"}), 404

    investment_report = generate_investment_reports(stock_symbol)

    return jsonify({
        "investment_report": investment_report,
    })

if __name__ == "__main__":
    load_dotenv()
    
    app.run(debug=True)
