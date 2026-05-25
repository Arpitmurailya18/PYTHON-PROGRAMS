from curl_cffi import requests
from bs4 import BeautifulSoup

contest_id = "2229"
submission_id = "375842134"
url = f"https://codeforces.com/contest/{contest_id}/submission/{submission_id}"

# 🍪 Injecting your active Codeforces login session!
my_cookies = {
    "JSESSIONID": "40825EE4E8B058AAF59DF82979BF7BB1",
    # Note: Codeforces sometimes relies on a second cookie named 'RCPC' or '39ce7'. 
    # If JSESSIONID alone doesn't work, grab those from the F12 menu and add them here too!
}

print(f"Fetching URL with Auth: {url} ...")

# Pass the cookies into the request
response = requests.get(url, impersonate="chrome", cookies=my_cookies)
print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    # Parse the HTML
    soup = BeautifulSoup(response.text, "html.parser")
    code_block = soup.find("pre", id="program-source-text")

    if code_block:
        print("✅ Successfully extracted the code!\n")
        print(code_block.text[:200]) # Printing the first 200 chars to test
    else:
        print("❌ Still failed. Open an incognito window, log in with this exact account, and manually check if YOU can see the code.")
else:
    print("❌ Network error.")