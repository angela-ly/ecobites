from typing import Self
from flask import Flask, jsonify, render_template, request, redirect, url_for
import dao

app = Flask(__name__)

def get_data(data):
     data['_id'] = str(data['_id'])
     return data


@app.route('/', methods=['GET'])
def index():
    """
    Render Main Index Page 
    """
    return render_template("/index.html")


@app.route('/restaurant', methods = ['GET'])
def restaurant():
    """
    Dashboard Routing 
    """
    #restaurants = dao.fetch_Restaurants()
    return render_template("/restaurants.html")

@app.route('/contact', methods = ['GET'])
def contact():
    """
    Dashboard Routing 
    """
    #restaurants = dao.fetch_Restaurants()
    return render_template("/contact.html")


# @app.route('/restaurant', methods = ['GET'] )
# def get_restaurants():
#     restaurants = dao.fetch_Restaurants()
#     return jsonify([get_data(restaurant) for restaurant in restaurants])

if __name__ == "__main__":
    app.run(debug= True)