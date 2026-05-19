# Level 1 : file handling in python
# # Challenge 1 : Notes saver

# notes = input("Enter notes:")

# with open("notes.txt", "a") as file:
#     file.write("\n" + notes)

# with open("notes.txt", "r") as file:
#     content = file.read()
#     print(content)
    
# # Challenge 2 : word Counter
# word_count = len(content.split())
# print("Total words in notes.txt:", word_count)

# Challenge 3 : C++ Template Generator

# name='A'

# for i in range(0, 5):
#     file_name = f"{name}.cpp"
#     with open(file_name, "w") as file:
#         file.write("#include<bits/stdc++.h>\n using namespace std;\n\n int main(){\n \n return 0;\n}")
#     name = chr(ord(name) + 1)

    
# Level 2 : API and Web Scraping

# Challenge 4 : CF Rating fetcher

import requests

t=5
for _ in range(t):
    
   username = input("Enter Codeforces Username: ")
   
   url = f"https://codeforces.com/api/user.info?handles={username}"
   response =requests.get(url)

   if response.status_code == 200:
       data = response.json()
       rating = data["result"][0]["rating"]
       fc = data["result"][0]["friendOfCount"]
       print(f"{username}'s rating is {rating}")
       print(f"{username} has {fc} friends on codeforces")
       
       with open("CF_USER_DATA.txt", "a") as file:
            file.write(f"Username: {username}\n")
            file.write(f"Rating: {rating}\n")
            file.write(f"Friends on Codeforces: {fc}\n")
            file.write("-" * 20 + "\n")  # separator for readability
   else:
       print("Failed to fetch data. Please check the username and try again.")
