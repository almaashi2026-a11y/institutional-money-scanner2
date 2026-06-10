import streamlit as st
import yfinance as yf
import pandas as pd

st.title("📊 Institutional Money Scanner Pro")

stocks = ["AAPL", "TSLA", "NVDA", "AMZN"]

def analyze(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="5d")

    if data is None or data.empty:
        return [symbol, "No Data", "No Data"]

    price = data["Close"].iloc[-1]
    volume = data["Volume"].mean()

    return [symbol, round(price, 2), int(volume)]

rows = [analyze(s) for s in stocks]

df = pd.DataFrame(rows, columns=["Symbol", "Price", "Volume"])

st.dataframe(df)
