from pymongo import MongoClient
import datetime
import pprint

class db:
    def __init__(self):
        print "working"

    def insertClient(self, phoneNumber,text,messageID):

        c = MongoClient()
        db = c['TECH']
        newDocument = {"senderPhone": phoneNumber,
                "messID": messageID,
                 "body": text}
        posts = db.post
        post_id = posts.insert_one(newDocument).inserted_id
        #print post_id

    def readClient(self,phoneNumber):
        c = MongoClient()
        db = c['TECH']
        posts=db.post
        #print phoneNumber
        return posts.find_one({"senderPhone": phoneNumber})





