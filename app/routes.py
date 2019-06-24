from flask import render_template

from app import app
from config import Config

import boto3

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/travels")
def travels():
	all_images = get_all_images()
	return render_template("feed.html", all_images=all_images)

def s3_client():
	s3 = boto3.client(
	   "s3",
	   aws_access_key_id=Config.S3_KEY,
	   aws_secret_access_key=Config.S3_SECRET,
	)
	return s3

def get_all_images():
	s3 = s3_client()
	objects = s3.list_objects(Bucket=Config.S3_BUCKET)
	images = [Image("https://" + Config.CLOUDFRONT_LOCATION + "/" + file["Key"]) for file in objects["Contents"]]
	print(images)
	return images

class Image():
	def __init__(self, url):
		self.url = url