from tinydb import TinyDB, Query

class DB():
    global connection
    def __init__(self):
        self.connection = TinyDB('db.json')


    def insert(self,jsonVals):
        self.connection.insert(jsonVals)

