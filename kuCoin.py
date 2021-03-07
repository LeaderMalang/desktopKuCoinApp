from kucoin.client import Client
from db import DB
from kucoin.exceptions import KucoinAPIException
class KUCoin():

    global client
    global api_key
    global api_secret
    global api_pasphrase
    global balance_percent
    global pair
    global base_coin
    def __init__(self,balance_percent_value,coin_name):
        #api_key = '602e39d9a2644e0006e7e2c2'
        #603e5c8473b5c50006582528
        db=DB()

        config=db.connection.all()
        
        self.api_key = config[0]['api_key']
        #api_secret = '2db4483e-2a76-4c2c-b533-f64a80a25c6d'
        self.api_secret = config[0]['api_secret']
        self.api_passphrase =config[0]['api_pass']
        #, sandbox=True
        self.client = Client(self.api_key, self.api_secret, self.api_passphrase)

        self.base_coin = config[1]['base_coin']
        self.balance_percent = balance_percent_value

        self.pair = coin_name + "-"+self.base_coin






    def getcurprice(self,pair):
        ticker = self.client.get_ticker(pair)
        return float(ticker['price'])


    def getAccounts(self,):
        accounts = self.client.get_accounts()
        return accounts



    def get_max_position_available(self,currency,pair):
        accounts = self.getAccounts()

        for account in accounts:
            if account['currency'] == currency:
                balance = account['balance']
                break


        price = self.getcurprice(pair)

        to_use = (float(balance)*self.balance_percent)/100

        decide_position_to_use = to_use / price

        return decide_position_to_use



    def create_sell_order(self,pair, quantity, price):

        order = self.client.create_limit_order(pair,
                                          Client.SIDE_SELL, price, quantity)
        print(order)
        return order


    def create_market_order(self):
        maxquantity = 0.0
        try:
            maxquantity = round(0.9 * self.get_max_position_available(self.base_coin, self.pair))
            if maxquantity > 0.0:
                # place a market buy order
                order = self.client.create_market_order(pair, Client.SIDE_BUY, size=maxquantity)
                print("Done")
                if not order['orderId']:
                    return "No Order Created Yet"
                else:
                    return "Max quantity "+ str(maxquantity)+ "for Current Pair "+ pair


        except KucoinAPIException  as e:
            return  e.message







# try:
#     buy_price = float(order['fills'][0]['price'])
#     buy_quantity = int(float(order['executedQty']))
#
#     sell_at_profit(client, pair, buy_quantity, buy_price, sell_percent)
# except Exception as ex:
#     print("No Order Placed Yet")
