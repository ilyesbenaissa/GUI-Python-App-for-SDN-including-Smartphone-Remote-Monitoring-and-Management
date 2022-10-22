import json

from prettytable import PrettyTable
import requests


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
#make a class and name it Add_User
class Delete_User:
    def __init__(self, username):
        payload = json.dumps({"username":username})
        response = requests.delete(baseUri+"/user/"+username, headers=headers)
        #if user is deleted, print a success message
        if response.status_code == 201|200:
            print("User "+username+" was deleted")
        else:
            print("User "+username+" was not deleted")


class Get_Users:
    def __init__(self):
        response = requests.get(baseUri+"/user", headers=headers)
        result = response.json()
        x = PrettyTable()
        #defining target fields
        x.field_names = [" username", "role"]
        #looping through the result
        for i in sorted(result["response"], key=lambda k: k['username']):
            #adding users rows to the table depending on the target fields
            x.add_row([i["username"],i["authorization"][0]["role"]])
        #printing the table of users with their roles and authorization
        print(x)


def Verify_User(username, password):
        headers = {"Content-type":"application/json"}
        payload = json.dumps({"username":username,"password":password})
        resp = requests.post(baseUri +"/ticket", data=payload, headers=headers)
        result=resp.json()
        if resp.status_code == 201|200:
            #if the user credentials are true it returns true
            return True
        else:
            #this will return false if the user credentials are false
            return False
        

#importable in other scripts
if __name__ == "__main__":
    pass

