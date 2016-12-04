from flask import Flask, request, redirect
import twilio.twiml
from db import db
from popDB import popDB
from popEmployersDB import popEmployersDB
from Matcher import Matcher
import time




session =""

condition = False

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
    global session
    global condition
    print session
    text=str(request.form["Body"])
    phoneNumber=str(request.form["From"])
    messageID=str(request.form["MessageSid"])
    newCustomer = db()
    populate = popDB()


    dict1 = {1: 'Q1', 2: 'Q2', 3: 'Q3',4:'Q4',5:'Q5',6:'Q6'}

    if condition == False:
        state = dict1[2]
        session = state
    resp = twilio.twiml.Response()

    if newCustomer.readClient(phoneNumber)==None:
        newCustomer.insertClient(phoneNumber, text, messageID)
        print "new Customer"
        resp.message("Hi! Welcome to Jobble, we help you find a job around you via sms. We will ask you several questions, please answer them and we will match you with a suitable job.")
        resp.message("What is your first name?")
        populate.insertID(phoneNumber)
        # Populating Employers db
        popEmployer = popEmployersDB()
        popEmployer.insertEmployer("Mr. Kenyatta", "+254 234 234567", "50 Shillings", "tractor driver", "Agriculture",
                                   "Naivasha")
        popEmployer.insertEmployer("Mr. Kibaki", "+254 524 272211", "45 Shillings", "tractor driver", "Agriculture",
                                   "Naivasha")

        state = dict1[2]
        session=state

    else:
        print "session: "
        print session

        if session == "Q2":
            name= str(request.form["Body"])
            populate.insertName(name,phoneNumber)

            resp.message("Please type your last name")
            state = dict1[3]
            session =state
            condition = True

        elif session == "Q3":
            lastname= str(request.form["Body"])
            populate.insertLastName(lastname, phoneNumber)
            resp.message("In which city would you like to work?")
            state = dict1[4]
            session = state
            condition = True

        elif session == "Q4":
            place= str(request.form["Body"])
            populate.insertPlace(place, phoneNumber)
            resp.message("In which of these sectors would you like to work:"
                         "Agriculture, Industrial, Manufacturing, Commercial, Construction?")
            state = dict1[5]
            session = state
            condition = True

        elif session == "Q5":
            sector = str(request.form["Body"])
            populate.insertSector(sector, phoneNumber)
            resp.message("Thanks for your info, will keep you updated!")
            state = dict1[6]
            session = state
            condition = True
            #time.sleep(1)
            matcher = Matcher()
            offers = matcher.match()
            print offers
            #time.sleep(1)
            resp.message(offers[0])
            #time.sleep(1)
            resp.message(offers[1])

        else:
            resp.message("Will update you as soon as we find a match")





            #session=state
            print "no new customer"
        #resp = twilio.twiml.Response()
        #resp.message("")

        #newCustomer.insertClient(phoneNumber, text, messageID)












    #newCustomer.insertClient(phoneNumber,text, messageID)
    #newCustomer.readClient("12345")


    return str(resp)



if __name__ == "__main__":
    app.run(debug=True)