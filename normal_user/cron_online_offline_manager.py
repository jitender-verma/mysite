import requests

url = "http://192.81.223.127:9001/cron_request"

try:
	req_obj = requests.post(url)
	print(req_obj)
except:
	pass