from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
import dateutil.parser as parser
from datetime import datetime
import json

app = Flask(__name__)
api = Api(app)
CORS(app)

class HelloWorld(Resource):
    def get(self):
        return {"data" : "Hello World"}

customer_one_data = json.load(open('customer1_data.json'))
customer_two_data = json.load(open('customer2_data.json'))
customer_three_data = json.load(open('customer3_data.json'))

customer_spending_prediction1 = json.load(open('output1.json'))
customer_spending_prediction2 = json.load(open('output2.json'))
customer_spending_prediction3 = json.load(open('output3.json'))

customer_segment_prediction1 = json.load(open('customer1_entertainment.json'))
customer_segment_prediction2 = json.load(open('customer2_rideshare.json'))
customer_segment_prediction3 = json.load(open('customer3_hotel.json'))

customer_risk_prediction1 = json.load(open('customer2_riskAnanlysis.json'))
customer_risk_prediction2 = json.load(open('customer2_riskAnanlysis.json'))
customer_risk_prediction3 = json.load(open('customer2_riskAnanlysis.json'))

@app.route('/api/account/prediction/risk/', methods=['GET'])
def get_risk():
    print("called for risk")
    account_data = customer_spending_prediction1
    current_id = request.args.get('id')
    if (current_id == "1"):
      print("CURRENT ID IS ONE")
      account_data = customer_risk_prediction1
    elif (current_id == "2"):
      print("CURRENT ID IS TWO")
      account_data = customer_risk_prediction2
    elif (current_id == "3"):
      print("CURRENT ID IS THREE")
      account_data = customer_risk_prediction3
    
    return jsonify(account_data)



  
@app.route('/api/account/summary/', methods=['GET'])
def summary():
    results = [{"title": "Total Savings",
                "icon": "refresh",
                "value": 567,
                "color": "violet",
                 "isIncrease": False,
                 "isCurrency": True,
                 "duration": "Since Last Year",
                 "percentValue": 0.5},

                {"title": "Money Spent",
                "icon": "attach_money",
                "value": 503,
                "color": "violet",
                 "isIncrease": True,
                 "isCurrency": True,
                 "duration": "Since Last Year",
                 "percentValue": 0.1},

                {"title": "Total Savings",
                "icon": "show_chart",
                "value": 224,
                "color": "violet",
                 "isIncrease": False,
                 "isCurrency": True,
                 "duration": "Since Last Year",
                 "percentValue": 0.1},

                {"title": "Average Money Spent",
                "icon": "star_border",
                "value": 2,
                "color": "violet",
                 "isIncrease": False,
                 "isCurrency": True,
                 "duration": "Since Last Year",
                 "percentValue": 0.25}]

 
    return jsonify(results)



@app.route('/api/account/prediction/segment/', methods=['GET'])
def get_segment_prediction():
    account_data = customer_spending_prediction1
    current_id = request.args.get('id')
    if (current_id == "1"):
      print("CURRENT ID IS ONE")
      account_data = customer_segment_prediction1
    elif (current_id == "2"):
      print("CURRENT ID IS TWO")
      account_data = customer_segment_prediction2
    elif (current_id == "3"):
      print("CURRENT ID IS THREE")
      account_data = customer_segment_prediction3
    
    return account_data



@app.route('/api/account/prediction/', methods=['GET'])
def get_prediction():
    account_data = customer_spending_prediction1
    current_id = request.args.get('id')
    if (current_id == "1"):
      print("CURRENT ID IS ONE")
      account_data = customer_spending_prediction1
    elif (current_id == "2"):
      print("CURRENT ID IS TWO")
      account_data = customer_spending_prediction2
    elif (current_id == "3"):
      print("CURRENT ID IS THREE")
      account_data = customer_spending_prediction3

    upperBound = []
    lowerBound = []

    for key, value in account_data["yhat"].items():
      upperBound.append(value)

    for key, value in account_data["yhat_lower"].items():
      lowerBound.append(value)
    
    output = [upperBound, lowerBound]
    return account_data

@app.route('/api/account/year/', methods=['GET'])
def get_account_summary():
    account_data = customer_one_data
    current_id = request.args.get('id')
    if (current_id == "1"):
      print("CURRENT ID IS ONE")
      account_data = customer_one_data
    elif (current_id == "2"):
      print("CURRENT ID IS TWO")
      account_data = customer_two_data
    elif (current_id == "3"):
      print("CURRENT ID IS THREE")
      account_data = customer_three_data
    #current_date = datetime.strptime((account_data[0]["transactionDateTime"]), "%a %B %d, %Y %I:%M %p")
    #return(parser.parse(account_data[0]["transactionDateTime"]).strftime('%m/%d/%Y').m, "is the date")
    #return current_date
    monthly_transactions = {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "12": 0,
    }

    count = 0
    for element in account_data:
        count +=1
        monthly_transactions[str(parser.parse(element["transactionDateTime"]).month)] = monthly_transactions[str(parser.parse(element["transactionDateTime"]).month)]+element["transactionAmount"] 

    myDate = parser.parse(account_data[0]["transactionDateTime"])
    return (monthly_transactions)


@app.route('/api/account/year/categories/', methods=['GET'])
def get_categorical_data():
    account_data = customer_one_data
    print("Getting categorical data")
    #current_date = datetime.strptime((account_data[0]["transactionDateTime"]), "%a %B %d, %Y %I:%M %p")
    #return(parser.parse(account_data[0]["transactionDateTime"]).strftime('%m/%d/%Y').m, "is the date")
    #return current_date
    monthly_transactions = {
        "fastfood":0,
        "hotels":0,
        "health":0,
        "personal care":0,
        "cable/phone":0,
        "entertainment":0
    }
    total = 0
    count = 0
    for element in account_data:
      if element["merchantCategoryCode"] in monthly_transactions:
        total += element["transactionAmount"]
        monthly_transactions[element['merchantCategoryCode']] += element["transactionAmount"]

    output = [0,0,0,0,0,0]
    for key, value in monthly_transactions.items():
      if monthly_transactions[key] !=0:
        monthly_transactions[key] = (monthly_transactions[key]/total)*100
    
    #The order is important so dont change it plz, ty uwu
    
    output[0] = monthly_transactions["fastfood"]
    output[1] = monthly_transactions["hotels"]
    output[2] = monthly_transactions["personal care"]
    output[3] = monthly_transactions["entertainment"]
    output[4] = monthly_transactions["cable/phone"]
    output[5] = monthly_transactions["fastfood"]
    
    
    return monthly_transactions
    

api.add_resource(HelloWorld, "/p")

if __name__ == "__main__":
    app.run(debug=True)
    get_account_summary()