from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)
class HelloWorld(Resource):
    def get(self):
        return {"data" : "Hello World"}



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

api.add_resource(HelloWorld, "/p")

if __name__ == "__main__":
    app.run(debug=True)