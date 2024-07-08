import datetime
import time
from plyer import notification
import yfinance as yf
import matplotlib.pyplot as plt

def plot_stock_graph(ticker,company):
    stock = yf.Ticker(ticker)

    hist = stock.history(period="1mo")

    plt.figure(figsize=(10, 5))
    plt.plot(hist.index, hist['Close'], label='Close Price',color='g')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.title(f'{company} Stock Price Over the Last Month')
    plt.legend()
    plt.show()

def stockdata(ticker):
    stock = yf.Ticker(ticker)
    data = stock.info
    company_name = data['longName']

    while True:
        data = stock.info
        notification.notify(
            title=f"{company_name} Data",
            message=f"Current Price={data['currentPrice']}\n"
                    f"DayLow={data['regularMarketDayLow']}\n"
                    f"DayHigh={data['regularMarketDayHigh']}\n"
                     f"P/E Ratio ={data['payoutRatio']}\n"
                    f"Mkt.Capital={data['marketCap']}\n"    
                    f"52week Low={data['fiftyTwoWeekLow']}\n"
                    f"52week High={data['fiftyTwoWeekHigh']}\n"
                    f"Recommendation={data['recommendationKey']}\n",
            app_icon="D:/Python Project/noti.ico",
            timeout=5
        )
        plot_stock_graph(ticker,company_name)
        time.sleep(8)

def main():
    ticker = input("Enter the stock ticker symbol: ")
    stockdata(ticker)

if __name__ == "__main__":
    main()
