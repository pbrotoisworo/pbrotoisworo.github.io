from flask import Flask, render_template
import os
import folium
from folium.plugins import HeatMap, MarkerCluster
import pandas as pd
import json
from scripts import generate_incident_map

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', jumbotron='index')

@app.route('/work/publications.html')
def publications():
    return render_template('/work/publications.html', title='Publications')

@app.route('/work/tweet2map.html')
def tweet2map():
    return render_template('/work/tweet2map.html', title='Tweet2Map')

@app.route('/cv.html')
def cv():
    return render_template('cv.html', title='CV')

@app.route('/portfolio.html')
def portfolio():
    return render_template('portfolio.html', title='CV')

@app.route('/incident_map.html')
def incident_map():
    html_map = generate_incident_map()
    return html_map

if __name__ == '__main__':
    app.run()