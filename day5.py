    ### python module to generate random numbers
import requests
import random
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Code Comparison Engine API!"}

@app.get("/problem_recommendation/{handle}")
def problem_recommendation(handle: str):
    urluser = f"https://codeforces.com/api/user.info?handles={handle}"
    urlproblem = f"https://codeforces.com/api/problemset.problems"
    
    responseuser = requests.get(urluser)
    responseproblem = requests.get(urlproblem)
    
    data = responseuser.json()
    
    rating = data["result"][0]["rating"]
    rating /= 100
    rating = rating * 100
    
    problems = responseproblem.json()
    
    prob = problems["result"]["problems"]
    
    filtered = []
    
    for problem in prob:
        if "rating" not in problem:
            continue
        
        problem_rating = problem["rating"]
        
        if rating - 100 <= problem_rating <= rating + 100:
            filtered.append({
                "name": problem["name"],
                "contestId": problem["contestId"],
                "index": problem["index"],
                "rating": problem_rating
            })
            
    if len(filtered) == 0:
        for problem in prob:
            if "rating" not in problem:
                continue
            prob800 = problem["rating"]
            
            if prob800 == 800:
                filtered.append({
                    "name": problem["name"],
                    "contestId": problem["contestId"],
                    "index": problem["index"],
                    "rating": prob800
                })
    
    return random.choice(filtered)
    
    