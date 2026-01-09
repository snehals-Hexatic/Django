import requests
import io


URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id = None):
   params={}
   if id is not None:
    params ={'id':id}

    
   r =requests.get( URL, params=params)
   data = r.json()
   print(data)
    
#get_data()


def post_data():
   data ={
      'name':'Ray',
      'roll': 88,
      'city':'Ranchi'
   }
     
   r = requests.post(URL, json=data)
   print(r.json())
   
#post_data()
   
def update_data():
   data ={
      'id':4,
      'name':'Jack',
      'city':'Delhi'
   }
     
   r = requests.put(URL, json=data)
   print(r.json())
   
#update_data()

def delete_data():
   params ={'id':4}
     
   r = requests.delete(URL, params=params)
   print(r.json())
   
delete_data()
