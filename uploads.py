import subprocess

def upload_file(num1, num2, num3):
	subprocess.call(["aws s3 cp %d-%d-%d.GIF s3://wigglegifphotobooth/ --acl public-read-write" % (num1, num2, num3)], shell=True)
	return

#upload_file(1, 2, 12)

#"aws s3 cp 0-2-12.GIF s3://wigglegifphotobooth/ --acl public-read-write"