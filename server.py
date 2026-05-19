## Example os simple FastAPI server code. This is the basic structure of a FastAPI application.

# from fastapi import FastAPI

# #Create teh application instance
# app = FastAPI()

# #Define waht heppens when someone wisits the root URL ("/")

# @app.get("/")
# def read_root():
#     return {"message": "Hello! The Code Comparison Engine is alive."}


"""
 from fastapi import FastAPI --> import the FastAPI class from the fastapi library
 
 ** what is Class???
 Answer: A class is like a blueprint/template.
         Example: Car class -> Blueprint 
         Object: An instance of a class.
         
 app = FastAPI() --> This creates an actual FastAPI application object
 
 *** FastAPI --> Blueprint/calss
     FastAPI() --> Actaul application instance/object.
     
 ** what is Stored in app?
 Answer: routes, server configuration, API settings, endpoint mappings everything for our backend app.
 
 
 @app.get("/") --> Decorator: Very important python feature. Meaning when someone visits "/", run the function below.
 
 ** what is "/"? 
 Answer: This is called a route/path/endpoint.
 
 Example URLs:
 Route           Meaning
 /               homepage/root
 /about          about page
 /user           user page
 
 def read_root(): --> Defins function named: read_root. This function executes whenever / route is visited.
 
 return {"message": "Hello! The Code Comparison Engine is alive."} --> This is the response that will be sent back to the client when they visit the "/" route. It returns a JSON object with a message.
  
 
"""

import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/UserData/{handle}")
def get_UserData(handle: str):
    url = f"https://codeforces.com/api/user.info?handles={handle}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rating = data["result"][0]["rating"]
        fc = data["result"][0]["friendOfCount"]
        return data
    else:
        return {"error": "Failed to fetch data. Please check the username and try again."}