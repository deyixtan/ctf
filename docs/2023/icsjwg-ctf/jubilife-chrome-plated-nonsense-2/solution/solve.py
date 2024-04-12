from base64 import b64decode

raw_url = "192.88.99.24:8080/bh8KCVcMVhtZWBADHgZXWBlECAJVA1FbUFVKAFEJS1AZRRQTVUl1ZmVjAxdFSRcZW145FFUWTEdcUhIPXwsUQUdEA0pEF01QGQFKD1RYdhNZRVtXBlIMAAIGVVYDQ1taCAA7"
encoded_url = raw_url.split(":8080/")[1]
decoded_url = list(b64decode(encoded_url))

id = "51ffbc1a9efa76f8a5a005d227a0f36606b524bcb627658520d0e0678da30e85"
key = list(id[0:4] + id[-4:])

decrypted_output = ""
for i in range(len(decoded_url)):
    decrypted_output += chr(decoded_url[i] ^ ord(key[i % len(key)]))

if decrypted_output.split(",")[4] == "MSPRequ":
    print(decrypted_output)
