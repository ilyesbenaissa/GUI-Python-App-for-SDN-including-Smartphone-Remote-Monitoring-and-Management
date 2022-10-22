import json
import requests

#making a class and name it Add_User
class Add_User:
    def __init__(self, username, password, role):
        #set the baseUri
        baseUri = "http://127.0.0.1:58000/api/v1"
        #set the headers
        headers = {"Content-type":"application/json"}
        #set the data
        data = json.dumps({"username" : "admin" , "password": "admin123"})
        #post the data to the baseUri
        resp = requests.post(baseUri +"/ticket", data=data, headers=headers)
        result=resp.json()
        ticket = result["response"]["serviceTicket"]
        headers = {"Content-type":"application/json","X-Auth-Token": ticket }
        payload = json.dumps({"username":username, "password":password, "authorization":[{"role":role}]})
        response = requests.post(baseUri+"/user", headers=headers, data=payload)
        #make if conditions for strong password

        if len(password) < 8:
            print("Password must be at least 8 characters long")
        elif password.isalpha() or password.isdigit():
            print("Password must contain at least one letter and one number")


        #if user is added successfully, print a success message
        if response.status_code == 201|200:
            print("User "+username+" was added successfully")
        #if user is not added successfully, print an error message
        else:
            message = response.json()["response"]["message"]
            print("User "+username+" was not added successfully\nReason: "+message)
#importable in other scripts
if __name__ == "__main__":
    pass
