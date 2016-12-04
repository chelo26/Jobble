from pymongo import MongoClient

class Matcher:
    def __init__(self):
        print "Matcher Running"


    def getField(self,field,collection):
        listField=[]
        for doc in collection.find():
            listField.append(str(doc[field]))
        return listField


    def match(self):
        # Acces to the Employers DB:
        c = MongoClient()
        db = c['TECH']
        jobsDB = db.post3
        empDB = db.post2

        listJobLocation=self.getField("Location",jobsDB)
        listJobSalary= self.getField("Salary", jobsDB)
        listJobDesc = self.getField("JobDescription", jobsDB)
        listJobType = self.getField("JobType", jobsDB)
        listJobEmp = self.getField("NameEmployer", jobsDB)
        listJobPhone= self.getField("PhoneNumber", jobsDB)


        listEmpLastName=self.getField("LastName",empDB)
        listEmpPlace= self.getField("Place", empDB)
        listEmpSector = self.getField("Sector", empDB)

        #listOffers=[]
        offers=[]
        #for i in range(0,len(listJobLocation)-1):
         #   if (listJobLocation[i]==listEmpPlace[0]) & (listJobType==listEmpSector[0]):
          #      listOffers.append(listJobLocation[i],listEmpLastName[i], listJobDesc[i],listJobSalary[i],listJobPhone)

        for i in range(0,len(listJobDesc)):
            offers.append("Hello Mr. "+str(listEmpLastName[0])+", there is a job in "+str(listJobLocation[i])+" "
            "as a "+str(listJobDesc[i])+" for "+str(listJobSalary[i])+" Please contact "+ str(listJobEmp[i]) + ""
            " at "+str(listJobPhone[i]))
        #print offers
        return offers



    def readClient(self,phoneNumber):
        c = MongoClient()
        db = c['TECH']
        posts=db.post
        #print phoneNumber
        return posts.find_one({"senderPhone": phoneNumber})

