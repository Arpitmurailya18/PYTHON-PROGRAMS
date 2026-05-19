import requests

url = "https://codeforces.com/api/user.info?handles=Srapit"

response = requests.get(url)

data = response.json()

rating = data["result"][0]["rating"]
fc = data["result"][0]["friendOfCount"]

with open("my_rating.txt", "w") as file:
    file.write(f"Arpit's rating is {rating}")
    file.write(f"\nArpit has {fc} friends on Codeforeces")
    
with open("my_rating.txt", "r") as file:
    content = file.read()
    print(content)

