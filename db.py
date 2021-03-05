from tinydb import TinyDB, Query

class DB():
    global connection
    def __init__(self):
        self.connection = TinyDB('db.json')


    def insertBaseCoin(self,jsonVals):
        config = self.connection.all()
        oldBase_coin = config[1]['base_coin']
        coin_query=Query()
        self.connection.update(jsonVals,coin_query.base_coin==oldBase_coin)
        return "Saved"

    def insertConfig(self,jsonVals):
        config = self.connection.all()
        old_api_key = config[0]['api_key']
        api_key_query=Query()
        self.connection.update(jsonVals,api_key_query.api_key==old_api_key)
        return "Saved"


    def searchConfig(self,val):
        find=Query()
        row=self.connection.search(find.api_key==val)
        return row
    def searchBaseCoin(self,val):
        find = Query()
        row = self.connection.search(find.base_coin == val)
        return row


