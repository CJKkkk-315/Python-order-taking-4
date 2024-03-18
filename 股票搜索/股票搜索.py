import yfinance as yf

def get_realtime_price(stock_code):
    stock_info = yf.Ticker(stock_code)
    todays_data = stock_info.history(period='1d')
    return todays_data['Close'][0]

stock_code = input("请输入股票代码：")
price = get_realtime_price(stock_code)
print(f"{stock_code} 的实时股价是：{price}")
