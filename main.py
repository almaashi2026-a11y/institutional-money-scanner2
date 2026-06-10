import streamlit as st
import yfinance as yf
import pandas as pd

st.title("📊 Institutional Money Scanner Pro")

stocks = ["AAPL", "TSLA", "NVDA", "AMZN"]

def analyze_stock(symbol):
    try:
        stock = yf.Ticker(symbol)
        data = stock.history(period="5d")

        if data is None or data.empty:
            return {
                "Symbol": symbol,
                "Price": "No Data",
                "Volume": "No Data"
            }

        last_price = float(data["Close"].iloc[-1])
        avg_volume = float(data["Volume"].mean())

        return {
            "Symbol": symbol,
            "Price": round(last_price, 2),
            "Volume": int(avg_volume)
        }

    except Exception as e:
        return {
            "Symbol": symbol,
            "Price": "Error",
            "Volume": str(e)
        }

results = [analyze_stock(s) for s in stocks]

df = pd.DataFrame(results)

st.dataframe(df)
