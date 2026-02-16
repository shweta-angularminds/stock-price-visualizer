import yfinance as yf

def get_stock_Data(symbol,period):
    stock = yf.Ticker(symbol)
    
    data = stock.history(period=period)
    info = stock.info
    return data,info