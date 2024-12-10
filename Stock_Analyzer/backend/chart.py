import yfinance as yf
from pandas import Timestamp
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
import numpy as np
import math

class ChartData:
    def chart_data_generation(symbol: str) -> tuple[dict, tuple]:
        """Get Data from Yahoo Finance and manipulate it to create a Grouped Bar Chart

        Args: symbol (str): The symbol of the company from Yahoo Finance.

        Returns: tuple: The financial data of the company.
            - data (dict): The financial data of the company.
            - features (tuple): The features of the financial data.
            """
        try:
            data = yf.Ticker(symbol)
            data = data.financials
            financials = data.to_dict(orient='index')
            Income = financials.get("Net Income")
            Revenue = financials.get("Total Revenue")
            Profit = financials.get("Gross Profit")
            Expenses = financials.get("Total Expenses")
            # Convert the Timestamp to year
            Total_Income = {Timestamp(key).year: value for key, value in Income.items()}
            Net_Revenue = {Timestamp(key).year: value for key, value in Revenue.items()}
            Gross_Profit = {Timestamp(key).year: value for key, value in Profit.items()}
            Total_Expenses = {Timestamp(key).year: value for key, value in Expenses.items()}
            data = (Total_Income, Net_Revenue, Gross_Profit, Total_Expenses)
            features = ("Net Income", "Total Revenue", "Gross Profit", "Total Expenses")
            graph_data = {}
            for year in data[0].keys():
                graph_data[year] = [data[i][year] / 10**8 for i in range(len(data))]    # Convert to crores
            return graph_data,features
        except:
            return f"Error: Unable to fetch the financial data for {symbol}"
        
    def generate_bar_chart(symbol) -> str:    
        financial_data, financial_metric = ChartData.chart_data_generation(symbol)
        years = list(financial_data.keys())
        x = np.arange(len(years))
        width = 0.15
        fig, ax = plt.subplots(figsize=(10, 6))
        # Create a colormap
        colors = plt.cm.viridis(np.linspace(0, 1, len(financial_metric)))
        for i, feature in enumerate(financial_metric):
            measurement = [financial_data[year][i] for year in years]
            ax.bar(x + i * width, measurement, width, label=feature, color=colors[i])

        # Set labels and title
        ax.set_ylabel('Amount in Crores')
        ax.set_xlabel('Count of Years')
        ax.set_title(f'Financial Data of {symbol}')
        ax.set_xticks(x + width * (len(financial_metric) - 1) / 2)
        ax.set_xticklabels(years)
        ax.legend(loc='upper left', ncol=1)
        ax.set_ylim(0, math.ceil(max([max(financial_data[year]) for year in years]) / 10) * 10)

        # Save the figure to the current directory
        file_path = f"../grouped_bar_chart.png"
        fig.savefig(file_path, format='png')
        plt.close(fig)  # Close the Matplotlib figure to free resources
        return file_path
    
    def generate_line_chart(symbol) -> str:
        financial_data, financial_metric = ChartData.chart_data_generation(symbol)
        years = list(financial_data.keys())
        x = np.arange(len(years))
        fig, ax = plt.subplots(figsize=(10, 6))
        # Create a colormap
        colors = plt.cm.viridis(np.linspace(0, 1, len(financial_metric)))
        for i, feature in enumerate(financial_metric):
            measurement = [financial_data[year][i] for year in years]
            ax.plot(x, measurement, label=feature, color=colors[i], marker='o')
        # Set labels and title
        ax.set_ylabel('Amount in Crores')
        ax.set_xlabel('Count of Years')
        ax.set_title(f'Financial Data of {symbol}')
        ax.set_xticks(x)
        ax.set_xticklabels(years)
        ax.legend(loc='upper left', ncol=1)
        ax.set_ylim(0, math.ceil(max([max(financial_data[year]) for year in years]) / 10) * 10)
        # Save the figure to the current directory
        file_path = f"../line_chart.png"
        fig.savefig(file_path, format='png')
        plt.close(fig)
        return file_path
