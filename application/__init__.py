from flask import Flask
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_cors import CORS
import os
from dotenv import load_dotenv
from flask_pymongo import PyMongo
    #env_path='.env'
load_dotenv()
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')
m=os.environ.get('MONGO_URI') 
#print(m)
app.config["MONGO_URI"] = m
# app.config["MONGO_URI"] = os.environ.get('MONGO_URI') ---NOT WOKRING 
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg','tif'}
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'sample')

# mongodb database
mongodb_client = PyMongo(app)
db = mongodb_client.db
if db is None:
    print("connection failed")
else:
    print("connected : ")
    print(db)
CORS(app)

from application import routes