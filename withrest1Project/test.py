import json
import requests

base_url = 'http://127.0.0.1:8000/'
end_point = 'api/'

def get_resource(id=None):
    data = {}
    if id is not None:
        data ={'id':id}
    resp = requests.get(base_url+end_point,data = json.dumps(data))
    print(resp.status_code)
    print(resp.json())

def create_resource():
    new_data = {'ename':'unknown','eage':28,'esal':24242,'eaddr':'mandya'}
    resp = requests.post(base_url+end_point,data = json.dumps(new_data))
    print(resp.status_code)
    print(resp.json())

def update_resource(id):
    new_data = {'id':id,'ename':'unknown1','eage':29,'esal':63535,'eaddr':'mysore'}
    resp = requests.put(base_url+end_point,data = json.dumps(new_data))
    print(resp.status_code)
    print(resp.json())

def delete_resource(id):
    data = {'id':id}
    resp = requests.delete(base_url+end_point,data = json.dumps(data))
    print(resp.status_code)
    print(resp.json())



print('1 for getting resource or 2 for creating resource or 3 for updating resource or 4 for deleting resource')
n = int(input("enter:"))
if n == 1:
    get_resource()
elif n == 2:
    create_resource()
elif n == 3:
    id = input('enter id :')
    update_resource(id)
elif n == 4:
    id = input('enter id :')
    delete_resource(id)
