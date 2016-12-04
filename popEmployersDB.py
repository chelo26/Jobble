from pymongo import MongoClient
import datetime
import pprint

class popEmployersDB:
    def __init__(self):
        print "popDB New Employer"

    def insertEmployer(self, name,phone,salary,jobDes,jobType,location):

        c = MongoClient()
        db = c['TECH']
        newDocument = {"NameEmployer": name,
                "PhoneNumber": phone,
                 "Salary": salary,
                "JobDescription":jobDes,
                       "JobType":jobType,
                       "Location":location}
        posts = db.post3
        post_id = posts.insert_one(newDocument).inserted_id

    def readClient(self,phoneNumber):
        c = MongoClient()
        db = c['TECH']
        posts=db.post
        #print phoneNumber
        return posts.find_one({"senderPhone": phoneNumber})

