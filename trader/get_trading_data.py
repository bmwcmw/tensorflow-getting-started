import json
import requests
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def get_trades(url):
    re = requests.get(url)
    content = re.content
    trades = json.loads(content)
    date = []
    price = []
    amount = []
    for trade in trades:
        date.append(trade['date'])
        price.append(trade['price'])
        amount.append(trade['amount'])
    return date, price, amount

#https://www.bitstamp.net/api/v2/transactions/btceur/?time=day&step=60
#https://www.bitstamp.net/api/v2/order_book/btceur/
#https://www.bitstamp.net/api/v2/ticker/btceur/
#compare with https://www.bitstamp.net/market/tradeview_data/?currencyPair=BTC/EUR&step=21600
def main():
    SRVC_TRANSACTION = 'transactions'
    SRVC_ORDER_BOOK = 'order_book'
    SRVC_TICKER = 'ticker'
    BITSTAMP = 'https://www.bitstamp.net/api/v2/'"'
    KRAKEN = 'https://api.kraken.com/0/'
    print('in main()')
    date, price, amount = get_trades(BITSTAMP)
    print(len(price))
    plt.figure()
    plt.plot(date, price)
    plt.show()


if __name__ == '__main__':
    print('to launch main()')
    main()
