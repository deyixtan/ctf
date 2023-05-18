import concurrent.futures
import requests
import string
import urllib.parse

session = requests.Session()
url = f"http://localhost/"
headers = { 
    "Content-Type": "application/x-www-form-urlencoded"
}

def perform_request(user_input):
    data = f"param={urllib.parse.quote(user_input)}"
    response = session.post(url, headers=headers, data=data)
    
    if response.status_code != 200:
        return None
    return user_input


def bruteforce(iterator):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(perform_request, c) for c in iterator]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result is None:
                continue
            print(f"Found input: {result}")
            executor.shutdown(wait=True, cancel_futures=True)
            break


if __name__ == "__main__":
    bruteforce(string.printable)
    print("Done")
