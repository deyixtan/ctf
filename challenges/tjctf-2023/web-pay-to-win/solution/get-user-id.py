import hashlib
import json
from base64 import b64encode

LOGIN_DATA = {
    "username": "test",
    "user_type": "basic"
}
EXPECTED_HASH = "53c660ea278ecff97090810ef8421c3b17a28d9b2eca76e49c866195e8145794"

def hash(data):
    return hashlib.sha256(bytes(data, "utf-8")).hexdigest()

def get_user_id(login_data, expected_hash):
    b64data = b64encode(json.dumps(login_data).encode())
    for i in range(2**24):
        curr_hash = hash(b64data.decode() + hex(i)[2:])
        if curr_hash == expected_hash:
            return i
    return None

if __name__ == "__main__":
    user_id = get_user_id(LOGIN_DATA, EXPECTED_HASH)
    if user_id:
        print(f"User ID: {user_id}")
    print("Done")
