# Referrrrer
Category: Web

## Description
Defeated the security of the website which implements authentication based on the `Referer` header.

URL : [http://static-01.heroctf.fr:7000](http://static-01.heroctf.fr:7000)

Format : **Hero{flag}**

Author : **xanhacks**

Attachments: [Referrrrer.zip](attachments/Referrrrer.zip)

## Write-up
- Upon examining the codebase, we discovered two important files: `app/index.js` and `nginx/nginx.conf`. These files contain the logic for the backend and the configurations for the reverse proxy (NGINX) respectively.
- Let's start by analyzing `nginx/nginx.conf`. This file contains standard configurations for routing traffic to the `/` and `/admin` paths. Of particular interest is the route to `/admin`, which performs a regex check on the HTTP `Referer` header. It ensures that the `Referer` header must start with `https://admin.internal.com` before forwarding the request to the backend server. If the condition is not met, a status code of `403 (Forbidden)` is returned.
- Moving on to `app/index.js`, we find similar routes for `/` and `/admin`. The route that stands out is `/admin`, where the code checks the value of the HTTP `Referer` header. It specifically requires the `Referer` header to be exactly `YOU_SHOUD_NOT_PASS!` in order to retrieve the flag.
- However, there is a conflict between the requirements of NGINX and the backend. NGINX expects the `Referer` header to start with `https://admin.internal.com`, while the backend requires it to be exactly `YOU_SHOUD_NOT_PASS!`.
- Upon further investigation, we discovered that within the Express.js request object, the `referer` value is first retrieved from `header.referrer` before `header.referer`, as shown [here](https://github.com/expressjs/express/blob/f540c3b0195393974d4875a410f4c00a07a2ab60/lib/request.js#L65).
- This means that we can set up a request with both the `Referer` and `Referrer` headers. The former will pass the check for NGINX, while the latter will pass the check for the backend.
- The request looks like this:
```
curl -H "Referer: https://admin.internal.com" -H "Referrer: YOU_SHOUD_NOT_PASS!" http://static-01.heroctf.fr:7000
```

Flag: `Hero{ba7b97ae00a760b44cc8c761e6d4535b}`
