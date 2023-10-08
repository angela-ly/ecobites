from flask import Flask
from flask_pymongo import PyMongo
from credentials import constants



app = Flask(__name__)

# connecting to mongo
app.config["MONGO_URI"] = constants.MONGO_CONNECT
mongodb_client = PyMongo(app)
db = mongodb_client.init_app(app, tlsAllowInvalidCertificates=True)
db = mongodb_client.db

def fetch_Restaurants() -> object:
    '''
    Queries restaurants dataset from database
    Args:
        None
    Returns:
        cursor (object): queried dataset object address
    '''
    restaurants = db.restaurants.find()
    return restaurants

if __name__ == "__main__":
    # Print all the courses
    # print(fetch_Restaurants())
    pass