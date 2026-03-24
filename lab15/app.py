"""
Eldon Wu
March 24, 2026
lab 15: RESTful API and unit test in a Flask app
"""
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# in-memory data
items = {}

@app.route('/')
def home():
    return render_template('index.html')

#CREATE an item
@app.route('/items', methods =['POST'])
def create_item():
    # get_json method is used to read JSON data sent by the client in an HTTP request
    data = request.get_json()

    # generate a new unique id for the new item
    item_id = str(len(items)+1)

    # add the data collected for the new item
    items[item_id] = data

    # jsonify converts a python dictionary into a json response, and returns status code as 201 (your request worked and new resource was created)
    return jsonify({'id':item_id, 'item': data}), 201

# READ ALL ITEMS
@app.route('/items', methods = ['GET'])
def get_items():
    return jsonify(items)

#READ SINGLE ITEM
@app.route('/items/<item_id>', methods = ['GET'])
def get_oneitem(item_id):
    item = items.get(item_id)
    if not item:
        # 404 = server is reachable but the item you asked for doesn't exist
        return jsonify({'Error':"Item no found"}), 404
    
    return jsonify(item)

if __name__ == '__main__':
    app.run(debug=True)