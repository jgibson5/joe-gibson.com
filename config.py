import os

class Config():
	S3_BUCKET           = os.environ.get("S3_BUCKET_NAME")
	S3_KEY              = os.environ.get("S3_ACCESS_KEY")
	S3_SECRET           = os.environ.get("S3_SECRET_ACCESS_KEY")
	S3_LOCATION         = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)
	CLOUDFRONT_LOCATION = os.environ.get("CLOUDFRONT_LOCATION")

	SECRET_KEY          = os.urandom(32)
	DEBUG               = True
	PORT                = 5000