# The DEW
Category: Web

## Description
Hello fellow Donut Earther! Check out this neat site that forwards our cause! The thing is, we think that the admin is actually a flat earther. Think you can figure it out?

[http://the-truth.hackers.best:31337/](http://the-truth.hackers.best:31337/)

Author: Pwnut

*Note: Ignore the session key, it's only present for challenge functionality. Also, if you have a working exploit, you might have to try more than once :)*

## Write-up
- The blog backend source file is provided at `/source`.
- The blog appears to be vulnerable to `XSS (Cross-Site Scripting)`, but due to `Content Security Policy (CSP)` restrictions, direct execution of JavaScript logic is blocked. However, CSP does allow the import of scripts from its own domain.
- The goal is to exploit the file upload functionality to upload a malicious JavaScript file that redirects the admin bot to our webhook while capturing its cookie.
- It appears that files can be uploaded at `/upload`.
- The file upload validation process checks for specific extensions, including `png`, `jpg`, `jpeg`, and `gif`, following the first dot in the file name. This means we can upload arbitrary files of our choice by prefixing the filename with a dot (.) and one of the listed extensions.
- To leak the cookies from the admin bot, we can create a JavaScript file named `script.gif.js`. This file will contain the logic to navigate (`location.href`) to our webhook while including the admin bot's cookie. A sample payload can be found [here](solution/script.gif.js).
- After uploading our malicious JavaScript file, we will be given the remote path to our script.
- By creating multiple comments (redudancy sake) with the title and message set as `<script src="/images/<UPLOADED_PATH>"></script>` (i.e. `<script src="/images/447f81d7-d7a6-4ff4-8619-54fd9ec4aa1cscript.gif.js"></script>`), we can import our malicious script into the page.
- Once the admin bot visits our comment, it will trigger a request to our webhook receiver, allowing us to capture the desired information.

Flag: `shctf{w3_a11_l1v3_und3r_th3_DOMe}`
