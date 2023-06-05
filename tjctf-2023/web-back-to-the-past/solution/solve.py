import base64
import json
from cryptography.hazmat.primitives import hashes, hmac

def base64url_encode(value):
    return base64.urlsafe_b64encode(value).rstrip(b"=")

def base64url_decode(value):
    value += b"=" * (4 - len(value) % 4)
    return base64.urlsafe_b64decode(value)

public_key = open("public_key.pem", "rb").read()

header = {
  "typ": "JWT",
  "alg": "HS256"
}

payload = {
  "id": "77f52e8f-6423-4fd4-b69a-59c381b4fb5d",
  "username": "test",
  "year": "1950"
}

b64header = base64url_encode(json.dumps(header).encode())
b64payload = base64url_encode(json.dumps(payload).encode())
h = hmac.HMAC(public_key, hashes.SHA256())
h.update(b".".join([b64header, b64payload]))
signature = h.finalize()

print(b".".join([b64header, b64payload, base64url_encode(signature)]).decode())
