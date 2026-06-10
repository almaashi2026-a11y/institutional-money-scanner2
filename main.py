import streamlit as st
import yfinance as yf
import pandas as pd

st.title("📊 Institutional Money Scanner")

stocks = ["AAPL", "TSLA", "NVDA", "AMZN", "MSFT"]

def analyze_stock(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="5d")

    if data.empty:
        return None

    last_price = data["Close"].iloc[-1]
    avg_volume = data["Volume"].mean()

    return {
        "Symbol": symbol,
        "Price": round(last_price, 2),
        "Avg Volume": int(avg_volume)
    }

results = []

for s in stocks:
    result = analyze_stock(s)
    if result:
        results.append(result)

df = pd.DataFrame(results)

st.dataframe(df)
