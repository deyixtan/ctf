# Microservices
Category: Web

## Description
I just learnt about microservices. That means my internal server is safe now right?

I'm still making my website but you can have a free preview

- Junhua

[http://34.124.157.94:5004](http://34.124.157.94:5004)

Alternative links: 

[http://34.124.157.94:5014](http://34.124.157.94:5014)

[http://34.124.157.94:5024](http://34.124.157.94:5024)

Attachments: [dist.zip](attachments/dist.zip)

## Write-up
- Upon examining the codebase, we have identified three services: `admin_page`, `homepage`, and `gateway`.
- To obtain the flag, we need the `admin` (logic in `/` endpoint of `admin_page`) to access the `/` endpoint of the `homepage`.
- We can leverage the `gateway` to forward our request to the `admin_page`, which will redirect the `admin` to the `homepage` and ultimately render the `flag.html`.
- To achieve this, we need to make a request to the `gateway` with the `service` parameter set to `admin_page`, indicating that we want to forward the request to the `admin_page`.
- At the `admin_page`, we need to satisfy the conditions `service != None and service != admin_page` and `requested_url != None`.
- For the first condition, the `gateway` already forwards `service=admin_page` since we want to forward our request to the `admin_page`. To meet the `service != admin_page` condition, we can employ parameter pollution by "overwriting" the previous value of service. This can be accomplished by defining `service=1` (or any value) after the previous `service`. The logic for retrieving query parameters differs between the `gateway` and the `admin_page`, which is why fulfilling the first condition is possible.
- To fulfill the second requirement, we can simply specify the `url` as `http://home_page`, prompting the `admin` to navigate to that URL, which will trigger the rendering of the flag template.
- This is the final URL required to retrieve the flag:
```
http://34.124.157.94:5004/?service=admin_page&service=1&url=http://home_page
```

Flag: `grey{d0ubl3_ch3ck_y0ur_3ndp0ints_in_m1cr0s3rv1c3s}`
