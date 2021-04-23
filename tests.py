import requests
import json

url = "http://127.0.0.1:8000/stud/"

# For_View data which is already in database
def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id' : id}
    json_data = json.dumps(data)
    r = requests.get(url = url, data = json_data)
    data = r.json()
    print(data)

get_data()
    
#  For Create data   
def Create_data(id = None):
    data = {
        'name' : 'karan',
        'roll' : 105,
        'city' : 'up'
    }

    json_data = json.dumps(data)
    r = requests.post(url=url, data=json_data)
    data = r.json()
    print(data)
    
Create_data()

# For update data
def Update_data():
    data = {
        'id' : 28,
        'name' : 'suraj',
        # 'roll' : 104,
        'city' : 'mumbai'
    }

    json_data = json.dumps(data)
    r = requests.put(url=url, data=json_data)
    data = r.json()
    print(data)
    
Update_data()

# For_delete_data
def delete_data():
    data = {'id' : 27}

    json_data = json.dumps(data)
    r = requests.delete(url=url, data=json_data)
    data = r.json()
    print(data)
    
delete_data()