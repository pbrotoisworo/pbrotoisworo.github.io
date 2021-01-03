from flask import Flask, render_template
import os
import folium

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/work/publications')
def publications():
    return render_template('/work/publications.html', title='Publications')

@app.route('/work/tweet2map')
def tweet2map():
    return render_template('/work/tweet2map.html', title='Tweet2Map')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/cv')
def cv():
    return render_template('cv.html', title='CV')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', title='CV')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

@app.route('/get_map')
def get_map():
    start_coords = (14.568304296379958, 121.04598219286339)
    folium_map = folium.Map(location=start_coords, zoom_start=11)
    folium_map.save('projects/tweet2map/map.html')
    render_map = folium_map._repr_html_()
    return render_map

if __name__ == '__main__':
    app.run()