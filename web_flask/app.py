from flask import Flask, render template
# from flask_pymongo import PyMongo
import json
import requests
from datetime import datetime
import pytz


app = Flask(__name__)

# mongodb+srv://juniha:Rodyroem@cluster0-naqor.mongodb.net/test?authSource=admin&replicaSet=Cluster0-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true


# time filter
@app.template_filter('strftime')
def _jinja2_filter_datetime(date,fmt=None):
    date = datetime.fromtimestamp(date)
    native = date.replace(tzinfo=None)
    format = '%Y-%m-%d'
    return native.strftime(format)

# set up your route
@app.route('/')
def index():
    status = monogo.db.status
    status_data = []
    for s in status.find().sort("date"):
        status_data.append({
			'date: _jinja2_filter_datetime(int(s.get('date'))),
			'deceased:s.get('deceased',0),
			'confirmed:s.get('confirmed',0),
			'resolved:s.get('resolved',0),
			'pending:s.get('pending',0),
			'total:s.get('total',0),

		})
	return render_template('home.html', ontario_data = status_data)

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


@app.route('/fetch')
def fetch():
	params = {
		'spider_name': 'ontario',
		'start_requests': True

	}
	response = requests.get('http://scrapy:9000/crawl.json', params)
	return response.text

	