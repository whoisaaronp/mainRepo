from flask import Flask, render template
# from flask_pymongo import PyMongo
import json
import requests
from datetime import datetime
import pytz


app = Flask(__name__)
# app.config['MONGO_URI'] = 'mongodb://admin:123@mongo:27017/movie_cms'
# mongo = PyMongo(app)
mongodb+srv://juniha:Rodyroem@cluster0-naqor.mongodb.net/test?authSource=admin&replicaSet=Cluster0-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true

# set up your route
@app.route('/')
def index():
	return render_template('home.html')

# set up your barchart
@app.route('/bar_chart')
def bar_chart():
	return render_template('barchart.html')

# set up your linechart
@app.route('/line_chart')
def line_chart():
	return render_template('linechart.html')

# set up your piechart
@app.route('/pie_chart')
def pie_chart():
	return render_template('piechart.html')

# set up your bubblechart
@app.route('/bubble_chart')
def bubble_chart():
	return render_template('bubblechart.html')

# # building the second route
# @app.route('/fetch')
# def fetch():
# 	params = {
# 		'spider_name': 'movie',
# 		'start_requests': True
# 	}
# 	response = requests.get('http://scrapy:9080/crawl.json', params)
# 	return response.text

