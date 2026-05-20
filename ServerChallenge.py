# Level 1 --->

## Challenge 1: User info API

# import requests
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/userinfo/{handle}")
# def get_userinfo(handle: str):
#     url = f"https://codeforces.com/api/user.info?handles={handle}"
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         data = response.json()
        
#         return data
#     else:
#         return {"error": "Failed to fetch data. Please check the username and try again."}
    
## Challenge 2: Online judge checker 
"""_
    input : handle , output : active/inactive
    use: user.status API
"""

# import requests
# import time
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/UserStatus/{handle}")
# def get_UserStatus(handle: str):
#     url = f"https://codeforces.com/api/user.status?handle={handle}"
#     response = requests.get(url)
    
#     data = response.json()
    
#     # submissions = data["result"]
    
#     # # latest submission
#     # latest = submissions[0]
#     # submission_time = latest["creationTimeSeconds"]
    
#     submission_time = data["result"][0]["creationTimeSeconds"]
    
#     current_time = time.time()
    
#     if response.status_code == 200:
#         if current_time - submission_time < 30*24*3600:
#             return {"status": "active"}
#         else:
#             return {"status": "inactive"}
#     else: 
#         return {"error": "Failed to fetch data. Please check the username and try again."}    

## Challenge 3: User Submission viewer
# returning last 5 submissions of a user

# from unittest import result

# import requests
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/submissions/{handle}")
# def get_Submissions(handle: str):
#         url = f"https://codeforces.com/api/user.status?handle={handle}"
        
#         response = requests.get(url)
        
#         data = response.json()
        
#         submissions = data["result"]
        
#         result = []
#         # Taking first 5 submissions
#         for submission in submissions[:5]:
            
#             problem_name = submission["problem"]["name"]
            
#             verdict = submission["verdict"]
            
#             result.append({
#                 "problem": problem_name,
#                 "verdict": verdict
#             })
#         return result

## Challenge 4: Accepted problem count for last 100 submissions

# import requests
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def home():
#     return {"message": "Welcome to the Code Comparison Engine API!"}

# @app.get("/accepted_count/{handle}")
# def get_AC_count(handle: str):
#     url = f"https://codeforces.com/api/user.status?handle={handle}&count=100"
#     response = requests.get(url)
    
#     data = response.json()
    
#     submissions = data["result"]
    
#     ac_count = sum(1 for submission in submissions if submission.get("verdict") == "OK")
            
#     return {"accepted_count": ac_count}


# Level 2 --->
## Challenge 1: Rating comparator

# import requests
# from fastapi import FastAPI

# app = FastAPI()
# @app.get("/")
# def home():
#     return {"message": "Welcome to the Code Comparison Engine API!"}

# @app.get("/compare/{h1}/{h2}")
# def compare_rating(h1: str, h2: str):
#     url1 = f"https://codeforces.com/api/user.info?handles={h1}"
#     url2 = f"https://codeforces.com/api/user.info?handles={h2}"
    
#     response1 = requests.get(url1)
#     response2 = requests.get(url2)
    
#     if response1.status_code == 200 and response2.status_code == 200:
#         data1 = response1.json()
#         data2 = response2.json()
        
#         rating1 = data1["result"][0]["rating"]
#         rating2 = data2["result"][0]["rating"]
        
#         if rating1 > rating2:
#             return {f"{h1} has a higher rating than {h2}"}
#         elif rating1 < rating2:
#             return {f"{h2} has a higher rating than {h1}"}
#         else:
#             return {"Both users have the same rating"}
#     else:
#         return {"error": "Failed to fetch data. Please check the usernames and try again."}

## Challenge 2: Contest Rating Hystory

# import requests
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def home():
#     return {"message": "Welcome to the Code Comparison Engine API!"}

# @app.get("/rating_history/{handle}")
# def get_rating_history(handle: str):
#     url = f"https://codeforces.com/api/user.rating?handle={handle}"
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         data = response.json()
#         contest_count = len(data["result"])
        
#         if contest_count == 0:
#             return {"message": "This user has not participated in any contests."}
        
#         if contest_count>=5:
#             worst = 0
#             best = 0
#             mini = 10**18
#             maxi= -10**18
#             for i in range(4, contest_count):
#                 rating_diff = data["result"][i]["newRating"] - data["result"][i]["oldRating"]
#                 if rating_diff < mini:
#                     mini = rating_diff
#                     worst = i
#                 if rating_diff > maxi:
#                     maxi = rating_diff
#                     best = i
                
#             wcoid = data["result"][worst]["contestId"]
#             bcoid = data["result"][best]["contestId"]
#             wcoName = data["result"][worst]["contestName"]
#             bcoName = data["result"][best]["contestName"]
                
#             return {
#                 "worst_contest": {
#                     "contest_id": wcoid,
#                     "contest_name": wcoName,
#                     "rating_change": mini
#                 },
#                 "best_contest": {
#                     "contest_id": bcoid,
#                     "contest_name": bcoName,
#                     "rating_change": maxi
#                 }
#             }         
            
#         else:
#             worst = 0
#             best = 0
#             mini = 10**18
#             maxi = -10**18
#             for i in range(contest_count):
#                 rating_diff = data["result"][i]["newRating"] - data["result"][i]["oldRating"]
#                 if rating_diff < mini:
#                     mini = rating_diff
#                     worst = i
#                 if rating_diff > maxi:
#                     maxi = rating_diff
#                     best = i
                
#             wcoid = data["result"][worst]["contestId"]
#             bcoid = data["result"][best]["contestId"]
#             wcoName = data["result"][worst]["contestName"]
#             bcoName = data["result"][best]["contestName"]
                
#             return {
#                 "worst_contest": {
#                     "contest_id": wcoid,
#                     "contest_name": wcoName,
#                     "rating_change": mini
#                 },
#                 "best_contest": {
#                     "contest_id": bcoid,
#                     "contest_name": bcoName,
#                     "rating_change": maxi
#                 }
#             }
            
#     else:
#         return {"error": "Failed to fetch data. Please check the username and try again."}
