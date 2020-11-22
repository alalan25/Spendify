from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
import dateutil.parser as parser
from datetime import datetime


app = Flask(__name__)
api = Api(app)
CORS(app)

class HelloWorld(Resource):
    def get(self):
        return {"data" : "Hello World"}

account_data = [
  
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 20000,
   "transactionDateTime": "2016-01-02T09:02:21",
   "transactionAmount": 62.2,
   "merchantName": "Hilton Hotels #692816",
   "merchantCategoryCode": "hotels",
   "currentBalance": 0
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 19937.8,
   "transactionDateTime": "2016-01-02T19:41:31",
   "transactionAmount": 150.78,
   "merchantName": "Hyatt House #998451",
   "merchantCategoryCode": "hotels",
   "currentBalance": 62.2
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 19787.02,
   "transactionDateTime": "2016-01-08T03:39:46",
   "transactionAmount": 0,
   "merchantName": "target.com",
   "merchantCategoryCode": "online_retail",
   "currentBalance": 212.98
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 19812.02,
   "transactionDateTime": "2016-02-05T01:01:58",
   "transactionAmount": 6.16,
   "merchantName": "Apple iTunes",
   "merchantCategoryCode": "mobileapps",
   "currentBalance": 187.98
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 19805.86,
   "transactionDateTime": "2016-02-06T14:05:25",
   "transactionAmount": 18.87,
   "merchantName": "Hilton Hotels #352797",
   "merchantCategoryCode": "hotels",
   "currentBalance": 194.14
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 19786.99,
   "transactionDateTime": "2016-02-13T00:52:51",
   "transactionAmount": 85.53,
   "merchantName": "Hilton Hotels #316622",
   "merchantCategoryCode": "hotels",
   "currentBalance": 213.01
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 19701.46,
   "transactionDateTime": "2016-02-17T07:23:52",
   "transactionAmount": 89.95,
   "merchantName": "Hilton Hotels #278076",
   "merchantCategoryCode": "hotels",
   "currentBalance": 298.54
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 19611.51,
   "transactionDateTime": "2016-02-19T05:52:20",
   "transactionAmount": 94.08,
   "merchantName": "KFC #553537",
   "merchantCategoryCode": "fastfood",
   "currentBalance": 388.49
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 19542.43,
   "transactionDateTime": "2016-03-07T13:56:33",
   "transactionAmount": 6.16,
   "merchantName": "Apple iTunes",
   "merchantCategoryCode": "mobileapps",
   "currentBalance": 457.57
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 19536.27,
   "transactionDateTime": "2016-03-10T07:05:50",
   "transactionAmount": 30.66,
   "merchantName": "Hilton Hotels #680956",
   "merchantCategoryCode": "hotels",
   "currentBalance": 463.73
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 19505.61,
   "transactionDateTime": "2016-03-27T00:13:09",
   "transactionAmount": 163.14,
   "merchantName": "Rodeway Inn #124016",
   "merchantCategoryCode": "hotels",
   "currentBalance": 494.39
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 19367.47,
   "transactionDateTime": "2016-04-02T18:02:48",
   "transactionAmount": 91.32,
   "merchantName": "apple.com",
   "merchantCategoryCode": "online_retail",
   "currentBalance": 632.53
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 19276.15,
   "transactionDateTime": "2016-04-03T13:56:46",
   "transactionAmount": 68.11,
   "merchantName": "Krispy Kreme #720032",
   "merchantCategoryCode": "fastfood",
   "currentBalance": 723.85
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 19208.04,
   "transactionDateTime": "2016-04-05T18:01:04",
   "transactionAmount": 170.46,
   "merchantName": "McDonalds #791572",
   "merchantCategoryCode": "fastfood",
   "currentBalance": 791.96
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 19037.58,
   "transactionDateTime": "2016-04-07T05:47:20",
   "transactionAmount": 6.16,
   "merchantName": "Apple iTunes",
   "merchantCategoryCode": "mobileapps",
   "currentBalance": 962.42
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 19031.42,
   "transactionDateTime": "2016-04-09T07:08:11",
   "transactionAmount": 26.88,
   "merchantName": "Hilton Hotels #999142",
   "merchantCategoryCode": "hotels",
   "currentBalance": 968.58
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 19004.54,
   "transactionDateTime": "2016-04-19T01:13:17",
   "transactionAmount": 447.04,
   "merchantName": "Rodeway Inn #329268",
   "merchantCategoryCode": "hotels",
   "currentBalance": 995.46
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 18557.5,
   "transactionDateTime": "2016-04-21T18:07:31",
   "transactionAmount": 85.36,
   "merchantName": "KFC #806300",
   "merchantCategoryCode": "fastfood",
   "currentBalance": 1442.5
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 18497.14,
   "transactionDateTime": "2016-05-01T20:19:21",
   "transactionAmount": 393.03,
   "merchantName": "Hyatt House #621607",
   "merchantCategoryCode": "hotels",
   "currentBalance": 1502.86
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 18104.11,
   "transactionDateTime": "2016-05-08T22:36:21",
   "transactionAmount": 6.16,
   "merchantName": "Apple iTunes",
   "merchantCategoryCode": "mobileapps",
   "currentBalance": 1895.89
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 18097.95,
   "transactionDateTime": "2016-05-13T09:00:03",
   "transactionAmount": 42.82,
   "merchantName": "Burger King #61773",
   "merchantCategoryCode": "fastfood",
   "currentBalance": 1902.05
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 18055.13,
   "transactionDateTime": "2016-05-15T16:46:18",
   "transactionAmount": 349.21,
   "merchantName": "Hilton Hotels #119121",
   "merchantCategoryCode": "hotels",
   "currentBalance": 1944.87
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 17705.92,
   "transactionDateTime": "2016-05-23T19:28:32",
   "transactionAmount": 153.3,
   "merchantName": "Rodeway Inn #784818",
   "merchantCategoryCode": "hotels",
   "currentBalance": 2294.08
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 17552.62,
   "transactionDateTime": "2016-05-24T05:17:10",
   "transactionAmount": 63.42,
   "merchantName": "Marriott Hotels",
   "merchantCategoryCode": "hotels",
   "currentBalance": 2447.38
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 17489.2,
   "transactionDateTime": "2016-05-28T06:20:11",
   "transactionAmount": 63.42,
   "merchantName": "Marriott Hotels",
   "merchantCategoryCode": "hotels",
   "currentBalance": 2510.8
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 17577.62,
   "transactionDateTime": "2016-06-09T17:01:48",
   "transactionAmount": 6.16,
   "merchantName": "Apple iTunes",
   "merchantCategoryCode": "mobileapps",
   "currentBalance": 2422.38
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 17571.46,
   "transactionDateTime": "2016-06-14T01:45:48",
   "transactionAmount": 42.67,
   "merchantName": "Renaissance Hotel #628831",
   "merchantCategoryCode": "hotels",
   "currentBalance": 2428.54
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 17528.79,
   "transactionDateTime": "2016-06-15T23:59:54",
   "transactionAmount": 44.81,
   "merchantName": "Rodeway Inn #784818",
   "merchantCategoryCode": "hotels",
   "currentBalance": 2471.21
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 17573.6,
   "transactionDateTime": "2016-06-16T01:11:57",
   "transactionAmount": 170.43,
   "merchantName": "Rodeway Inn #211609",
   "merchantCategoryCode": "hotels",
   "currentBalance": 2426.4
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 17403.17,
   "transactionDateTime": "2016-06-20T23:48:51",
   "transactionAmount": 174.89,
   "merchantName": "Hilton Hotels #405695",
   "merchantCategoryCode": "hotels",
   "currentBalance": 2596.83
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 17228.28,
   "transactionDateTime": "2016-06-23T17:10:38",
   "transactionAmount": 168.65,
   "merchantName": "Renaissance Hotel #97439",
   "merchantCategoryCode": "hotels",
   "currentBalance": 2771.72
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 17059.63,
   "transactionDateTime": "2016-06-30T13:29:48",
   "transactionAmount": 27.66,
   "merchantName": "Hilton Hotels #533600",
   "merchantCategoryCode": "hotels",
   "currentBalance": 2940.37
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 17056.97,
   "transactionDateTime": "2016-07-03T04:05:58",
   "transactionAmount": 4.42,
   "merchantName": "Hyatt House #770440",
   "merchantCategoryCode": "hotels",
   "currentBalance": 2943.03
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 17052.55,
   "transactionDateTime": "2016-07-03T22:57:39",
   "transactionAmount": 114.48,
   "merchantName": "discount.com",
   "merchantCategoryCode": "online_retail",
   "currentBalance": 2947.45
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 16938.07,
   "transactionDateTime": "2016-07-11T15:20:29",
   "transactionAmount": 6.16,
   "merchantName": "Apple iTunes",
   "merchantCategoryCode": "mobileapps",
   "currentBalance": 3061.93
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 16931.91,
   "transactionDateTime": "2016-07-13T11:24:13",
   "transactionAmount": 41.69,
   "merchantName": "Hyatt House #464602",
   "merchantCategoryCode": "hotels",
   "currentBalance": 3068.09
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 16890.22,
   "transactionDateTime": "2016-07-16T16:00:24",
   "transactionAmount": 443.99,
   "merchantName": "Renaissance Hotel #809953",
   "merchantCategoryCode": "hotels",
   "currentBalance": 3109.78
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 16446.23,
   "transactionDateTime": "2016-07-19T18:23:16",
   "transactionAmount": 3.8,
   "merchantName": "Renaissance Hotel #738212",
   "merchantCategoryCode": "hotels",
   "currentBalance": 3553.77
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 16442.43,
   "transactionDateTime": "2016-07-27T01:17:26",
   "transactionAmount": 162.25,
   "merchantName": "Hilton Hotels #992076",
   "merchantCategoryCode": "hotels",
   "currentBalance": 3557.57
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 16305.18,
   "transactionDateTime": "2016-08-02T06:47:52",
   "transactionAmount": 189.24,
   "merchantName": "Hilton Hotels #28693",
   "merchantCategoryCode": "hotels",
   "currentBalance": 3694.82
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 16115.94,
   "transactionDateTime": "2016-08-02T10:02:23",
   "transactionAmount": 128.79,
   "merchantName": "Wendys #940261",
   "merchantCategoryCode": "fastfood",
   "currentBalance": 3884.06
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 15987.15,
   "transactionDateTime": "2016-08-08T16:13:48",
   "transactionAmount": 282.13,
   "merchantName": "Renaissance Hotel #89242",
   "merchantCategoryCode": "hotels",
   "currentBalance": 4012.85
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 15705.02,
   "transactionDateTime": "2016-08-10T00:04:11",
   "transactionAmount": 13.6,
   "merchantName": "cheapfast.com",
   "merchantCategoryCode": "online_retail",
   "currentBalance": 4294.98
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 15691.42,
   "transactionDateTime": "2016-08-11T00:53:07",
   "transactionAmount": 6.16,
   "merchantName": "Apple iTunes",
   "merchantCategoryCode": "mobileapps",
   "currentBalance": 4308.58
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 15685.26,
   "transactionDateTime": "2016-08-14T13:01:48",
   "transactionAmount": 48.04,
   "merchantName": "Hyatt House #232008",
   "merchantCategoryCode": "hotels",
   "currentBalance": 4314.74
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 15637.22,
   "transactionDateTime": "2016-08-19T07:00:40",
   "transactionAmount": 16.08,
   "merchantName": "Renaissance Hotel #845122",
   "merchantCategoryCode": "hotels",
   "currentBalance": 4362.78
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 15621.14,
   "transactionDateTime": "2016-08-24T22:08:33",
   "transactionAmount": 18.45,
   "merchantName": "abc.com",
   "merchantCategoryCode": "online_subscriptions",
   "currentBalance": 4378.86
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 15627.69,
   "transactionDateTime": "2016-09-01T04:46:45",
   "transactionAmount": 223.46,
   "merchantName": "Hilton Hotels #141743",
   "merchantCategoryCode": "hotels",
   "currentBalance": 4372.31
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 15404.23,
   "transactionDateTime": "2016-09-10T19:29:08",
   "transactionAmount": 6.16,
   "merchantName": "Apple iTunes",
   "merchantCategoryCode": "mobileapps",
   "currentBalance": 4595.77
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 15398.07,
   "transactionDateTime": "2016-09-13T20:16:35",
   "transactionAmount": 477.32,
   "merchantName": "discount.com",
   "merchantCategoryCode": "online_retail",
   "currentBalance": 4601.93
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 14920.75,
   "transactionDateTime": "2016-09-23T23:57:28",
   "transactionAmount": 42.2,
   "merchantName": "Renaissance Hotel #738212",
   "merchantCategoryCode": "hotels",
   "currentBalance": 5079.25
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 14878.55,
   "transactionDateTime": "2016-09-24T13:27:59",
   "transactionAmount": 18.45,
   "merchantName": "abc.com",
   "merchantCategoryCode": "online_subscriptions",
   "currentBalance": 5121.45
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 14860.1,
   "transactionDateTime": "2016-09-29T03:07:20",
   "transactionAmount": 211.15,
   "merchantName": "Renaissance Hotel #696523",
   "merchantCategoryCode": "hotels",
   "currentBalance": 5139.9
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 14673.95,
   "transactionDateTime": "2016-10-04T18:29:00",
   "transactionAmount": 166.03,
   "merchantName": "Hyatt House #237946",
   "merchantCategoryCode": "hotels",
   "currentBalance": 5326.05
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 14507.92,
   "transactionDateTime": "2016-10-12T07:04:32",
   "transactionAmount": 6.16,
   "merchantName": "Apple iTunes",
   "merchantCategoryCode": "mobileapps",
   "currentBalance": 5492.08
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 14501.76,
   "transactionDateTime": "2016-10-13T03:46:16",
   "transactionAmount": 0,
   "merchantName": "Hilton Hotels #992076",
   "merchantCategoryCode": "hotels",
   "currentBalance": 5498.24
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 14501.76,
   "transactionDateTime": "2016-10-13T12:20:11",
   "transactionAmount": 53.04,
   "merchantName": "Hilton Hotels #900000",
   "merchantCategoryCode": "hotels",
   "currentBalance": 5498.24
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 14448.72,
   "transactionDateTime": "2016-10-22T10:08:20",
   "transactionAmount": 28.28,
   "merchantName": "Hilton Hotels #119121",
   "merchantCategoryCode": "hotels",
   "currentBalance": 5551.28
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 14420.44,
   "transactionDateTime": "2016-10-26T07:56:33",
   "transactionAmount": 18.45,
   "merchantName": "abc.com",
   "merchantCategoryCode": "online_subscriptions",
   "currentBalance": 5579.56
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 14401.99,
   "transactionDateTime": "2016-10-28T13:02:51",
   "transactionAmount": 59.91,
   "merchantName": "Subway #401837",
   "merchantCategoryCode": "fastfood",
   "currentBalance": 5598.01
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 14367.08,
   "transactionDateTime": "2016-11-07T08:09:31",
   "transactionAmount": 41.33,
   "merchantName": "Rodeway Inn #987870",
   "merchantCategoryCode": "hotels",
   "currentBalance": 5632.92
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 14325.75,
   "transactionDateTime": "2016-11-11T08:36:05",
   "transactionAmount": 6.16,
   "merchantName": "Apple iTunes",
   "merchantCategoryCode": "mobileapps",
   "currentBalance": 5674.25
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 14319.59,
   "transactionDateTime": "2016-11-20T03:26:36",
   "transactionAmount": 176.11,
   "merchantName": "Dunkin' Donuts #343350",
   "merchantCategoryCode": "fastfood",
   "currentBalance": 5680.41
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 14143.48,
   "transactionDateTime": "2016-11-21T07:18:41",
   "transactionAmount": 70.88,
   "merchantName": "Rodeway Inn #166841",
   "merchantCategoryCode": "hotels",
   "currentBalance": 5856.52
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 14072.6,
   "transactionDateTime": "2016-11-25T14:24:15",
   "transactionAmount": 231.09,
   "merchantName": "Rodeway Inn #923883",
   "merchantCategoryCode": "hotels",
   "currentBalance": 5927.4
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 13841.51,
   "transactionDateTime": "2016-11-26T23:33:21",
   "transactionAmount": 18.45,
   "merchantName": "abc.com",
   "merchantCategoryCode": "online_subscriptions",
   "currentBalance": 6158.49
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 13848.06,
   "transactionDateTime": "2016-12-04T12:38:52",
   "transactionAmount": 158.85,
   "merchantName": "Renaissance Hotel #151808",
   "merchantCategoryCode": "hotels",
   "currentBalance": 6151.94
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 13689.21,
   "transactionDateTime": "2016-12-07T04:26:02",
   "transactionAmount": 231.09,
   "merchantName": "Rodeway Inn #923883",
   "merchantCategoryCode": "hotels",
   "currentBalance": 6310.79
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 13920.3,
   "transactionDateTime": "2016-12-12T03:06:29",
   "transactionAmount": 6.16,
   "merchantName": "Apple iTunes",
   "merchantCategoryCode": "mobileapps",
   "currentBalance": 6079.7
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 13914.14,
   "transactionDateTime": "2016-12-24T15:02:36",
   "transactionAmount": 78.56,
   "merchantName": "Arbys #669514",
   "merchantCategoryCode": "fastfood",
   "currentBalance": 6085.86
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 13835.58,
   "transactionDateTime": "2016-12-24T19:05:12",
   "transactionAmount": 189.38,
   "merchantName": "Hyatt House #464602",
   "merchantCategoryCode": "hotels",
   "currentBalance": 6164.42
 },
 {
   "accountNumber": 999789077,
   "creditLimit": 20000,
   "availableMoney": 13646.2,
   "transactionDateTime": "2016-12-28T08:23:38",
   "transactionAmount": 18.45,
   "merchantName": "abc.com",
   "merchantCategoryCode": "online_subscriptions",
   "currentBalance": 6353.8
 }
]



@app.route('/api/account/year/', methods=['GET'])
def get_account_summary():
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
    print("Getting categorical data")
    #current_date = datetime.strptime((account_data[0]["transactionDateTime"]), "%a %B %d, %Y %I:%M %p")
    #return(parser.parse(account_data[0]["transactionDateTime"]).strftime('%m/%d/%Y').m, "is the date")
    #return current_date
    monthly_transactions = {
        "rideshare":0,
        "food":0,
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
    
    output[0] = monthly_transactions["food"]
    output[1] = monthly_transactions["health"]
    output[2] = monthly_transactions["personal care"]
    output[3] = monthly_transactions["entertainment"]
    output[4] = monthly_transactions["cable/phone"]
    output[5] = monthly_transactions["rideshare"]
    
    
    print(monthly_transactions)
    return monthly_transactions
    

api.add_resource(HelloWorld, "/p")

if __name__ == "__main__":
    app.run(debug=True)
    get_account_summary()