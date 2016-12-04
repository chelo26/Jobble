from pymongo import MongoClient
import datetime
import pprint

class popDB:
    def __init__(self):
        print "popDB New Customer"

    def insertID(self,phone):
        c = MongoClient()
        db = c['TECH']
        newDocument = {"ID": phone}
        db.post2.insert(newDocument)

    def insertName(self, name,phoneNumber):
        c = MongoClient()
        db = c['TECH']
        newDocument = {"Name": name}
        posts = db.post2
        itm= posts.find_one({"ID": phoneNumber})
        phone= itm.get('_id')
        posts.update({"_id": phone}, {"$set": newDocument})

    def insertLastName(self, lastName,phoneNumber):
        c = MongoClient()
        db = c['TECH']
        newDocument = {"LastName": lastName}
        posts = db.post2
        itm= posts.find_one({"ID": phoneNumber})
        phone= itm.get('_id')
        posts.update({"_id": phone}, {"$set": newDocument})

    def insertPlace(self, place,phoneNumber):
        c = MongoClient()
        db = c['TECH']
        newDocument = {"Place": place}
        posts = db.post2
        itm= posts.find_one({"ID": phoneNumber})
        phone= itm.get('_id')
        posts.update({"_id": phone}, {"$set": newDocument})

    def insertSector(self, sector,phoneNumber):
        c = MongoClient()
        db = c['TECH']
        newDocument = {"Sector": sector}
        posts = db.post2
        itm= posts.find_one({"ID": phoneNumber})
        phone= itm.get('_id')
        posts.update({"_id": phone}, {"$set": newDocument})








    def readClient(self,phoneNumber):
        c = MongoClient()
        db = c['TECH']
        posts=db.post
        #print phoneNumber
        return posts.find_one({"senderPhone": phoneNumber})

