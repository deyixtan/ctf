# Migraine
Category: Web

## Description
Author: `Mr. Blade`

The administrator changed their password, and we lost access to their account. We need to regain access to continue our operations.

NOTE: all letters used in this flag will be lowercase (if you have `GIGEM{...}`, you should use `gigem{...}`)

[http://logical.tamuctf.com](http://logical.tamuctf.com)

## Write-up
- Requests sent to the `/chpass` endpoint with the `username` parameter will return a JSON response indicating if the user exists (`res = exists`) or not (`res = not exists`).
- The username `admin` is known to exist based on the response.
- The feature is vulnerable to SQL blind injection, as determined with `admin' AND 1 = '2';`.
- Since the flag may be hidden within the user's password, a brute-force approach can be used to extract each character of the password using SQL's `LIKE` operator.
- By iterating through all printable ASCII characters, a payload can be constructed to leak the password character by character. An example payload would look like: `admin' AND password LIKE '<BRUTEFORCED_CHARS>%';`.
- The solve script, which performs the character-by-character leakage, can be found [here](solution/solve.py).

Flag: `gigem{bl1nd-1nj3ct10n}`
