from flask_frozen import Freezer
from main import app
import os
import shutil

freezer = Freezer(app)

if __name__ == '__main__':
    
    freezer.freeze()
    
    script_dir = os.path.dirname(__file__)
    docs_dir = os.path.join(script_dir, 'docs')
    
    # If existing docs dir, delete it
    if os.path.exists(docs_dir):
        shutil.rmtree(docs_dir)
        
    # Rename build dir to docs
    src = os.path.join(script_dir, 'build')
    dst = os.path.join(script_dir, 'docs')
    os.rename(src, dst)
    