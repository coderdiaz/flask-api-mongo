import json
from flask import Flask, jsonify, make_response, request
from pymongo import MongoClient
from bson import json_util, ObjectId

# Creating application
app = Flask(__name__)

# Mongo DB connection
client = MongoClient('mongodb://db:27017')
db = client.libraries

# GET /api/
@app.route('/api/', methods=['GET'])
def get_root():
  return jsonify({
    'message': 'Welcome to my Flask API'
  })

@app.route('/api/author/', methods=['GET'])
def get_authors():
  authors = db.authors.find()
  return jsonify({
    'data': json.loads(json_util.dumps(authors))
  })

@app.route('/api/author/', methods=['POST'])
def create_author():
  if not request.json or not 'name' in request.json or not 'bio' in request.json:
    return jsonify({ 'code': 400, 'message': 'Bad request' }), 400

  name = request.json['name']
  bio = request.json['bio']

  db.authors.insert({ 'name': name,'bio': bio })
  return jsonify(), 201

# Error handler for catch 404 not found
@app.errorhandler(404)
def not_found(error):
  return make_response(jsonify({
    'code': 404,
    'message': 'Not Found'
  }), 404)

# Run application
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)