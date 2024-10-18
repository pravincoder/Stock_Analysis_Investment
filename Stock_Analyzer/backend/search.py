import yfinance as yf
import requests
stock_name = input()
stock_name = stock_name.replace(" ", "")
url = "https://query2.finance.yahoo.com/v1/finance/search"
user_agent = "Chrome/8.0 (Windows NT 10.0; Win64; x64)"
params = {"q": stock_name, "quotes_count": 1}
res = requests.get(url=url, params=params, headers={"User-Agent": user_agent})
res.raise_for_status()  
data = res.json()
for n in range(0, 4):
    stock_symbol = data["quotes"][n]['shortname']
    print(stock_symbol)
