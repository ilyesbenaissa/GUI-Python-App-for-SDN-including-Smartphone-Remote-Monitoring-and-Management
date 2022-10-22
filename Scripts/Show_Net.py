import requests
import json
from prettytable import PrettyTable

class Show_Net:
	def __init__(self):
		baseUri = "http://127.0.0.1:58000/api/v1"

		#API call to request service ticket
		headers = {"Content-type":"application/json"}
		data = json.dumps({"username" : "admin" , "password": "admin123"})
		resp = requests.post(baseUri +"/ticket", data=data, headers=headers)

		#print(resp.status_code)
		result = resp.json()
		#print(result)

		ticket = result["response"]["serviceTicket"]
		#print(ticket)

		#API call to request list of network devices
		headers = {"X-Auth-Token": ticket }
		resp = requests.get(baseUri+"/network-device", headers=headers)

		#print(resp.status_code)
		result = resp.json()
		#print (json.dumps(result, indent=4))

		x = PrettyTable()
		x.field_names = [" hostname", "version", "Ip Address"]
		for i in sorted(result["response"], key=lambda k: k['hostname']):
			x.add_row([i["hostname"],i["softwareVersion"],i["managementIpAddress"]])
		print(x)

# importable in other scripts
if __name__ == "__main__":
	Show_Net()
	