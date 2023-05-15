# Chrome-Plated Nonsense - 2
Category: Jubilife

## Description
The second extension the employee installed is named ChickenChickenStop Privacy Kit (see attached crx file). It claims to delete unnecessary cookies and improve user privacy, but it came from the same source as the first extension, and based on the traffic it is generating, it also appears to be exfiltrating information.

Your task is to examine the network traffic from this extension, which has been ingested into Malcolm, and determine what information it was used to extract.

Within the extracted data, what is the value of the lt variable in the cookie named `MSPRequ`?

*Flag format: value of the lt variable. Example: if cookie contained a=0&lt=12345&b=0, the flag would be **12345***

Attachments: [chickenchickenstop-privacy-kit.crx](attachments/chickenchickenstop-privacy-kit.crx)

## Write-up
- Similar to the process described in [Chrome-Plated Nonsense - 1](../jubilife-chrome-plated-nonsense-1/README.md), we can begin by extracting the files from the provided Chrome extension.
- The main logic of the Chrome extension can be found in the extracted `background.js` file.
- Upon installation, the Chrome extension collects system information, encodes it along with a generated ID, and sends it to a remote server located at `http://192.88.99.24:8080/`.
- Any subsequent changes to cookies are serialized, encoded using the ID, and appended to the URL for a request to the server.
- To proceed, we need to identify the first request sent to the server during installation in order to retrieve the ID (which is base64 encoded in the URL). This ID is necessary for decoding the entire request payload for subsequent requests triggered by cookie changes.
- To examine the network traffic related to this extension, we can review the network logs in `Arkime`.
- Since it's associated with a Chrome extension, we can apply the following filter: `destination.ip == 192.88.99.24 && event.dataset == http`. This filter will narrow down the list for analysis.
- We discover that the request with the URL `192.88.99.24:8080/aWQ9NTFmZmJjMWE5ZWZhNzZmOGE1YTAwNWQyMjdhMGYzNjYwNmI1MjRiY2I2Mjc2NTg1MjBkMGUwNjc4ZGEzMGU4NSx0aW1lc3RhbXA9MTY3NDU4MDg2NDc4NCxhcmNoTmFtZT14ODZfNjQsbW9kZWxOYW1lPXZpcnQtNy4yLG51bU9mUHJvY2Vzc29ycz04LGF2YWlsYWJsZUNhcGFjaXR5PTEzNjgxNTE2NTQ0LGNhcGFjaXR5PTE3MTcxNjExNjQ4` corresponds to the installation request of the Chrome extension. The query can be decoded with base64, revealing the ID `51ffbc1a9efa76f8a5a005d227a0f36606b524bcb627658520d0e0678da30e85`.
- We also identify a request related to changes in the `MSPRequ` cookie. The URL associated with this request is `192.88.99.24:8080/bh8KCVcMVhtZWBADHgZXWBlECAJVA1FbUFVKAFEJS1AZRRQTVUl1ZmVjAxdFSRcZW145FFUWTEdcUhIPXwsUQUdEA0pEF01QGQFKD1RYdhNZRVtXBlIMAAIGVVYDQ1taCAA7`.
- By utilizing the [solve.py](solution/solve.py) script, we can retrieve the contents of the cookie. We observe that `lt=1674577303` is among the retrieved information.

Flag: `1674577303`
