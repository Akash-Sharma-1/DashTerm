import yfinance as yf


def get_stock_info(name):
    msft = yf.Ticker(name)
    return msft.info

# if __name__ == '__main__':
#     print(get_stock_info("MSFT"))