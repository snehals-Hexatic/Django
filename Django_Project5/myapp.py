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
    
#get_data(1)

def post_data():
   data ={
      'name':'Sona',
      'roll': 111,
      'city':'Dubai'
   }
     
   r = requests.post(URL, json=data)
   print(r.json())
   
#post_data()
   
def update_data():
   data ={
      'id':11,
      'name':'Shruti',
      'city':'Nashik'
   }
     
   r = requests.put(URL, json=data)
   print(r.json())
   
#update_data()

def delete_data():
   params ={'id':11}
     
   r = requests.delete(URL, params=params)
   print(r.json())
   
delete_data()
