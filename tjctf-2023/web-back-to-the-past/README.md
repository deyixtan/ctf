# back-to-the-past
Category: Web

## Description
"Back to the Future" never made sense as a title

[back-to-the-future.tjc.tf](https://back-to-the-future.tjc.tf/)

Attachments: [server.zip](attachments/server.zip)

## Write-up
When we navigate to the provided URL, we are presented with the following webpage:

![](solution/image1.png)

We will proceed to register an account with the following details:

![](solution/image2.png)

However, we encounter the following page:

![](solution/image3.png)

After analyzing the codebase, we have determined our end goal:

```
@app.route("/retro")
@login_required()
def retro(user):
    if int(user["year"]) > 1970:
        return render_template("retro.html", flag="you aren't *retro* enough")
    else:
        return render_template("retro.html", flag=flag)
```

Upon accessing the endpoint, we are presented with the following view:

![](solution/image4.png)

Our objective is to navigate to the `/retro` endpoint with the `year` field in our session set to a value less than or equal to `1970`. At first glance, it may seem simple to create a user with a `year` set to `<= 1970`, right? To find out more, let's take a closer look at the code snippet related to the `/register` endpoint which handles user registrations:

```
@app.route("/register", methods=["POST"])
def post_register():
    username = request.form["username"]
    year = request.form["year"]

    if username in u2id:
        return redirect("/register?msg=So+unoriginal")
    if not username:
        return redirect("/register?msg=No+username+provided")
    if not year.isnumeric() or not 1970 < int(year) < 2024:
        return redirect("/register?msg=Invalid+year")

    id = str(uuid.uuid4())
    u2id[username] = id
    u2year[username] = year
    res = make_response(redirect("/"))
    res.set_cookie("token", generate_token(id, username, year))

    return res
```

As we can observe, there are validations in place that restrict the `year` value to be between `1970` and `2024` (exclusive). Modifying the `year` post-registration would require forging the JWT session tokens and regenerating the token's signature to prevent it from appearing tampered.

Now, let's examine the JWT encoding/decoding functionalities used by the server to create/verify session tokens:

```
def encode(payload, secret, algorithm=None):
    if not algorithm or algorithm not in possible_algorithms:
        raise ValueError("invalid algorithm")
    header = {"typ": "JWT", "alg": algorithm}
    b64header = base64url_encode(json.dumps(header).encode())
    b64payload = base64url_encode(json.dumps(payload).encode())
    if algorithm == "HS256":
        h = hmac.HMAC(secret, hashes.SHA256())
        h.update(b".".join([b64header, b64payload]))
        signature = h.finalize()
    elif algorithm == "RS256":
        priv = serialization.load_pem_private_key(
            secret, password=None, backend=default_backend()
        )
        signature = priv.sign(
            b".".join([b64header, b64payload]),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256(),
        )
    return b".".join([b64header, b64payload, base64url_encode(signature)])


def decode(token, secret, algorithms=None):
    if not algorithms or any(alg not in possible_algorithms for alg in algorithms):
        return None
    if token.count(b".") != 2:
        return None

    header, payload, signature = token.split(b".")
    if not header or not payload or not signature:
        return None
    try:
        json_header = json.loads(base64url_decode(header))
        json_payload = json.loads(base64url_decode(payload))
        decoded_signature = base64url_decode(signature)
        alg_to_use = json_header["alg"]
        if alg_to_use == "HS256":
            h = hmac.HMAC(secret, hashes.SHA256())
            h.update(b".".join([header, payload]))
            h.verify(decoded_signature)
        elif alg_to_use == "RS256":
            pub = serialization.load_pem_public_key(secret)
            pub.verify(
                decoded_signature,
                b".".join([header, payload]),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH,
                ),
                hashes.SHA256(),
            )
        return json_payload
    except Exception as e:
        print(e)
        return None
```

It's worth noting that both functions support encoding/decoding using the `RS256` (asymmetric encryption) and `HS256` (symmetric encryption) algorithms.

Here is our current session token:

```
eyJ0eXAiOiAiSldUIiwgImFsZyI6ICJSUzI1NiJ9.eyJpZCI6ICI3N2Y1MmU4Zi02NDIzLTRmZDQtYjY5YS01OWMzODFiNGZiNWQiLCAidXNlcm5hbWUiOiAidGVzdCIsICJ5ZWFyIjogIjE5NzEifQ.BvpXxu4x9RzmQEj3IVPhn3-7VvWUKy-sXxjcXnHLp4iuYvR8kYk-xcxO4mn1QPRJ7Et4rNUaZOuaFt4PIumpGajSt66W8Au6xbDN3Iim_rRd9eiWyfRGkUcy2rZkfwFty1zVGN3qpmsyhP3I9yPzJEgUP8ON7pNDQH71CxbtKhdcFyDDQJHFbApjdOP94Pf0mg0ajVsjKc8fMlRXX4CIO0XcS2s-aq_A9zNWUHTZXluxDySFc3vkANj111TCafUYc4o1Wui7CjvcSpOe35Yilzrenz6h-XD4c-JieKVXn8M8YTm2xSgfwiG7-F4XxVsk7bGVRVKxzN9kIHEARB64sQ
```

When parsed using tools like [https://jwt.io/](https://jwt.io/), we can observe the header:

```
{
  "typ": "JWT",
  "alg": "RS256"
}
```

And the payload:

```
{
  "id": "77f52e8f-6423-4fd4-b69a-59c381b4fb5d",
  "username": "test",
  "year": "1971"
}
```

Currently, our session token is signed using asymmetric encryption (`RS256`). Since obtaining the private key from server is not feasible, a more practical approach would be to "force" our session token to utilize the `HS256` algorithm. By doing so, we can utilize the publicly accessible public key located at `static/public.pem` to create/verify our session token, allowing us to maliciously control the payload of our session token.

To generate a new malicious session token using the `HS256` algorithm, you can utilize the [solve.py](solution/solve.py) script. 

When we update our session token with the malicious version, the flag will be displayed in the `/retro` page.

![](solution/image5.png)

Flag: `tjctf{very_very_retro_3bbff613}`
