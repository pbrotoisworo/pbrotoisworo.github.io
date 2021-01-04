from flask import Flask, render_template
import os
import folium
from folium.plugins import HeatMap, MarkerCluster
import pandas as pd
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

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

@app.route('/work/incident_map.html')
def get_map():
    
    # Init folium map
    mc = MarkerCluster(name='Incidents')
    metro_coords = (14.599574, 121.059929)
    m = folium.Map(
        location=metro_coords,
        zoom_start=11,
        tiles='OpenStreetMap'
    )

    # load incident data
    df = pd.read_csv(r'work\tweet2map\data_mmda_traffic_spatial.csv')
    df = df.tail(1000)  # Only get last 1000 pieces of data
    mc = MarkerCluster(name='Incidents')
    
    # Populate map
    for item in df.iterrows():
        
        source = item[1]['Source']
        text = item[1]['Tweet']
        timestamp = item[1]['Date']
        embed = """
        <head>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
        </head>
        <div>
            <h3>Tweet:</h3>
            <blockquote class="twitter-tweet tw-align-center"><p lang="en" dir="ltr"> {} </a></p>&mdash; Official MMDA (@MMDA)<a href="{}"> {}</a></blockquote>
            <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
        </div>
        """.format(text, source, timestamp)
        
        # Generate content for markers
        iframe = folium.IFrame(
            embed,
            width=500,
            height=280
        )
        
        # Put content in popup for markers
        popup = folium.Popup(iframe)
        mc.add_child(folium.Marker(location=[item[1]['Latitude'], item[1]['Longitude']],
                                    popup=popup,
                                    clustered_marker=True)).add_to(m)
        
    # Load boundaries
    with open(r'work\tweet2map\ncr_boundary.geojson', 'r') as f:
        json_file = f.read()
    geojson = json.loads(json_file)
    folium.GeoJson(
        geojson,
        name='LGU Boundaries'
    ).add_to(m)
    
    folium.LayerControl(position='topright').add_to(m)
    
    m.save(r'work\tweet2map\map.html')
    render_map = m._repr_html_()
    return render_map

if __name__ == '__main__':
    app.run()