import subprocess

def upload_file(devices, set_id=0):
	print "Attempting to upload gif to the cloud ..."
	subprocess.call(["aws s3 cp %d.GIF s3://wigglegifphotobooth/ --acl public-read-write" % (set_id)], shell=True)
	return

#upload_file(1, 2, 12)

#"aws s3 cp wigglygif.css s3://wigglegifphotobooth/ --acl public-read-write"