import requests
import json
from prettytable import PrettyTable


#creating a class to delelte a network branch using for loop

class Del_Net:
    def __init__(self, NET_ID):
        full_ip=""
        NET_ID = NET_ID[:-1]
        for i in range(0,254):
            full_ip = NET_ID + str(i)
            baseUri = "http://127.0.0.1:58000/api/v1"
            headers = {"Content-type":"application/json"}
            data = json.dumps({"username" : "admin" , "password": "admin123"})
            resp = requests.post(baseUri +"/ticket", data=data, headers=headers)
            result = resp.json()
            ticket = result["response"]["serviceTicket"]
            url = "http://127.0.0.1:58000/api/v1/network-device/ip-address/"+full_ip
            headers ={
            "Content-Type": "application/json",
            "X-Auth-Token": ticket,
            'Accept': 'application/json'
                     }
            response = requests.delete(url, headers=headers, data={'ipAddress': full_ip})
            result = response.json()
            if ((response.status_code) == 200):
                print("Network ID: "+ NET_ID +".0 has been deleted")
            

#make it importable in other scripts
if __name__ == "__main__":
    pass
