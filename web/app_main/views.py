from flask import render_template, Flask, request, send_from_directory
from app_main import app
#import os
from boto.s3.connection import S3Connection
from aws import aws_access, aws_key

# conn = S3Connection('access-key','secret-access-key')

def check_gifs():
	gifs = []
	# 	for root, dirs, files in os.walk("/media/ana0/000/Documents/wigglegif/web/app_main/static/giftest"):
	# 	    for f in files:
	# 	        if f.endswith('.GIF'):
	# 	            gifs.append(f)
	conn = S3Connection(aws_access,aws_key)
	bucket = conn.get_bucket('wigglegifphotobooth')
	if bucket:
		for key in bucket.list():
			gifs.append(str(key.generate_url(expires_in=1000, query_auth=False)))

		#this part is going on because of weird ordeing from AWS
		for i in range(len(gifs)):
			gifs[i] = gifs[i].split("/")
			gifs[i] = gifs[i][-1]
			gifs[i] = gifs[i].split(".")
			gifs[i] = int(gifs[i][0])

		gifs = list(reversed(sorted(gifs)))

		for i in range(len(gifs)):
			gifs[i] = "https://wigglegifphotobooth.s3.amazonaws.com/" + str(gifs[i]) + ".GIF"

		return gifs
	else:
		return "sorry please try again later"

def total_pages(gifs,count_by):
	try:
		return len(gifs)//countby + 1
	except:
		return "sorry please try again later"


gifs = check_gifs()
countby = 15
pages = total_pages(gifs, countby)

@app.route('/')
def hello_world():
	more = True
	return render_template('index.html', gifs=gifs[countby*0:countby], more=more, next=str(2))


@app.route('/<int:num>')
def pagination(num=[num+1 for num in range(pages) if num!=1]):
	more = True
	if num >= pages:
		more = False
	next = num+1
	return render_template('index.html', gifs=gifs[countby*1:countby*2], more=more, next=str(next))
