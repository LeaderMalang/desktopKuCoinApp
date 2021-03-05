from kucoin.client import Client
import requests
from kucoin.exceptions import KucoinAPIException

#api_key = '602e39d9a2644e0006e7e2c2'
api_key = '603e5c8473b5c50006582528'
#api_secret = '2db4483e-2a76-4c2c-b533-f64a80a25c6d'
api_secret = '7ac588b7-9c62-45ff-8dca-627897e5196a'
api_passphrase = 'Test987654'
#, sandbox=True
client = Client(api_key, api_secret, api_passphrase)
print(client)
balance = "USDT"
balance_percent = float(input("balance Percent %: "))
# sell_percent = float(input("Profit %: "))
print("Type Coin Name: ")
pair = input() + "-"+balance




def getcurprice(pair):
    ticker = client.get_ticker(pair)
    return float(ticker['price'])


def getAccounts():
    accounts = client.get_accounts()
    return accounts



def get_max_position_available(currency,pair):
    accounts = getAccounts()

    for account in accounts:
        if account['currency'] == currency:
            balance = account['balance']
            break


    price = getcurprice(pair)

    to_use = (float(balance)*balance_percent)/100

    decide_position_to_use = to_use / price

    return decide_position_to_use



def create_sell_order(pair, quantity, price):

    order = client.create_limit_order(pair,
                                      Client.SIDE_SELL, price, quantity)
    print(order)
    return order




maxquantity=0.0
try:
    maxquantity = round(0.9 * get_max_position_available(balance,pair))
    if maxquantity >0.0:
        # place a market buy order
        order = client.create_market_order(pair, Client.SIDE_BUY, size=maxquantity)
        print("Done")
        if not order['orderId']:
            print("No Order Created Yet")
        else:
            print("Max quantity ", maxquantity, "for Current Pair", pair)


except KucoinAPIException  as e:
    print(e.message)



# try:
#     buy_price = float(order['fills'][0]['price'])
#     buy_quantity = int(float(order['executedQty']))
#
#     sell_at_profit(client, pair, buy_quantity, buy_price, sell_percent)
# except Exception as ex:
#     print("No Order Placed Yet")