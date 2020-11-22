from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
import pymongo
import os
import json
from bson import json_util, ObjectId

myclient = pymongo.MongoClient(os.getenv("MONGOURL"))
mydb = myclient["mydatabase"]
mycol = mydb["users"]

app = Flask(__name__)
api = Api(app)
CORS(app)

# schema = {
#     _id: "",
#     name: "",
#     spending: {
#         total:"",
#         food:"",
#         health:"",
#         personalCare:"",
#         entertainment:"",
#         cablePhone:"",
#         rideshare:""
#     },
#     crediAssesment: "",
#     category: {
#         essential:"",
#         nonEssential:""
#     },
#     pet: {
#         name: "",
#         happy: "",
#         sad: "",
#         size:""
#         }
#     }




class HelloWorld(Resource):
    def get(self):
        mydict = { "name": "BEN", "address": "131313" }
        #mycol.insert_one(mydict)
        results = []
        for doc in mycol.find():
            print(doc)
            results.append(doc)
        return json.loads(json.dumps(results, default=str))


api.add_resource(HelloWorld, "/hello")


@app.route('/api/transactions/', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    print(request.args, "args")
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = [
        {
           "creation_date": "2020-11-21",
            "recurring_date": 0,
            "status": "pending",
            "_id": "string",
            "payment_amount": 0,
            "nickname": "string",
            "upcoming_payment_date": "2020-11-21",
            "payee": "string",
            "payment_date": "2020-11-21"
        }
    ]

 
    return jsonify(results)



@app.route('/api/account/summary/', methods=['GET'])
def get_summary():
    
    results = [{"title": "Total Savings",
                "icon": "refresh",
                "value": 567,
                "color": "violet",
                 "isIncrease": False,
                 "isCurrency": True,
                 "duration": "Since Last Month",
                 "percentValue": 0.5},

                {"title": "Money Spent",
                "icon": "attach_money",
                "value": 503,
                "color": "violet",
                 "isIncrease": True,
                 "isCurrency": True,
                 "duration": "Since Last Month",
                 "percentValue": 0.1},

                {"title": "Total Savings",
                "icon": "show_chart",
                "value": 224,
                "color": "violet",
                 "isIncrease": False,
                 "isCurrency": True,
                 "duration": "Since Last Month",
                 "percentValue": 0.1},

                {"title": "Average Money Spent",
                "icon": "star_border",
                "value": 2,
                "color": "violet",
                 "isIncrease": False,
                 "isCurrency": True,
                 "duration": "Since Last Month",
                 "percentValue": 0.25}]

 
    return jsonify(results)




if __name__ == "__main__":
    app.run(debug=True)