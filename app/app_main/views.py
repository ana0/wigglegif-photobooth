from flask import render_template, Flask, redirect, url_for, flash
from app_main import app
import os

@app.route('/')
def hello_world():
	gifs = []
	for root, dirs, files in os.walk("/media/ana0/000/Documents/wigglegif/giftest"):
	    for f in files:
	        if f.endswith('.GIF'):
	            gifs.append(f)
    #files = [files for root, dirs, files, in os.walk("/media/ana0/000/Documents/wigglegif/giftest")]
    #gifs = [f for f in files if f.endswith('.gif')]
    #gifs = "gifs"
	return render_template('index.html', gifs=gifs)