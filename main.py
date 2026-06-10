import yfinance as yf
import pandas as pd

# قائمة أسهم مثال (نقدر نطورها لاحقاً)
stocks = ["AAPL", "TSLA", "NVDA", "AMZN", "MSFT"]

def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    hist = stock.history(period="5d")
    return hist

def analyze_stock(symbol):
    data = get_stock_data(symbol)
    
    if data.empty:
        return None

    last_close = data["Close"].iloc[-1]
    avg_volume = data["Volume"].mean()

    return {
        "symbol": symbol,
        "last_price": last_close,
        "avg_volume": avg_volume
    }

results = []

for s in stocks:
    result = analyze_stock(s)
    if result:
        results.append(result)

df = pd.DataFrame(results)
print(df)
