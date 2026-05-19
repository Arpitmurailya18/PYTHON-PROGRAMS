import requests

# we are asking codeforces for the data of a specific user (e.g., tourist)
url = "https://codeforces.com/api/user.info?handles=Srapit"
response = requests.get(url)

print(response.status_code) # this will print the status code of the response (e.g., 200 for success)

# The response comes back as JSON, which python easily converts into a Dictionary (like C++ map)
data = response.json()

# Accessing the specific rating value from the nested dictionary 
rating = data["result"][0]["rating"]
fc = data["result"][0]["friendOfCount"]
print(rating)
print(fc)

"""
import requests --> this import the request package 
purpose : send HTTP requests, talk to websites/APIs, fetch internet data

url = "some url" --> this stores the API URL in variable url

# /api/user.info --> this is the endpoint of the API which give us the user info of a codeforces user

# ?handles=Srapit --> give information about user Srapit

## Sending Request:
response = requests.get(url) --> this sends an HTTP GET request.    

HTTP has methods:

Method               Meaning
GET                  Retrieve data from the server (fetch data)
POST                 Send data to the server (submit data)
PUT                  Update existing data on the server
DELETE               Remove data from the server
PATCH                Partially update existing data on the server
HEAD                 Retrieve only the headers of a resource
OPTIONS              Describe the communication options for the target resource

** What is response ???
Answer: response store everything returned by server, icluding status code, headers, Json data, text content, etc.

** Converting JSON data to Python dictionary:
data = response.json() --> this converts the JSON data from the response into a Python dictionary.
The API returns JSON data 
"""