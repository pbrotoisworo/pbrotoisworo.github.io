from flask_frozen import Freezer
import main
import os
import shutil

tests_dir = os.path.dirname(__file__)
root_dir = os.path.dirname(os.path.dirname(__file__))
build_dir = os.path.join(root_dir, 'build')
docs_dir = os.path.join(root_dir, 'docs')

if os.path.exists(build_dir):
    shutil.rmtree(build_dir)

freezer = Freezer(main.app)
freezer.freeze()

def test_index_exists():
    message = 'Index page not detected.'
    assert os.path.exists(os.path.join(build_dir, 'index.html')), message

def test_cv_page_exists():
    message = 'CV page not detected.'
    assert os.path.exists(os.path.join(build_dir, 'cv.html')), message
    
def test_incident_map_exists():
    message = 'Incident map not detected.'
    assert os.path.exists(os.path.join(build_dir, 'incident_map.html')), message
    
def test_portfolio_page_exists():
    message = 'Portfolio page not detected.'
    assert os.path.exists(os.path.join(build_dir, 'portfolio.html')), message
    
def test_publications_page_exists():
    message = 'Publications page not detected.'
    assert os.path.exists(os.path.join(build_dir, 'work', 'publications.html')), message
    
def test_tweet2map_page_exists():
    message = 'Tweet2Map page not detected.'
    assert os.path.exists(os.path.join(build_dir, 'work', 'tweet2map.html')), message