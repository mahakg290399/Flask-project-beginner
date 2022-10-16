 
from flask import Flask, jsonify, request
app = Flask(__name__)

stores=[
    {
        "name": "Agrasen Kirana Store",
        "items":[
            {
                "name":"My Item",
                "price": 15.99
            }
        ]
    }
]

@app.route("/store", methods=["POST"])
def create_store():
    request_data = request.get_json()
    new_store = {
        "name": request_data['name'],
        "items" : request_data['items']
    }
    stores.append(new_store)
    return(jsonify(stores))
    

@app.route("/store/<string:name>")
def get_store(name):
    return stores[0][name]

@app.route("/store")
def get_stores():
    return jsonify({"Stores":stores})

@app.route("/store/<string:name>/item",methods=['POST'])
def create_item_in_store(name):
    pass

@app.route("/store/<string:name>/item")
def get_item_in_store(name):
    pass





app.run(debug=True, port=5000)