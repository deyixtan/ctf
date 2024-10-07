import hashlib
import json
from base64 import b64encode

LOGIN_DATA = {
    "username": "test",
    "user_type": "basic"
}
USER_ID = 9213427

def hash(data):
    return hashlib.sha256(bytes(data, "utf-8")).hexdigest()

def get_premium_payload(login_data, user_id):
    login_data["user_type"] = "premium"
    b64data = b64encode(json.dumps(login_data).encode()).decode()
    premium_hash = hash(b64data + hex(user_id)[2:])
    return (b64data, premium_hash)

if __name__ == "__main__":
    b64_premium_data, premium_hash = get_premium_payload(LOGIN_DATA, USER_ID)
    print(f"Base64 login data: {b64_premium_data}")
    print(f"Premium hash: {premium_hash}")
