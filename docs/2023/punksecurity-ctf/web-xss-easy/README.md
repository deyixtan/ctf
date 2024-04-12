# XSS - Easy
Category: Web

## Description
We've built a new blog app!

Can you get the flag from the admin user? He's logged on right now

## Write-up
- Upon entering the blog environment, we noticed a link to an admin control panel and a comment box for the blog post.
- We published a comment and observed that the admin accesses the page and also leaves a comment whenever we make comments on the blog.
- Through a quick test using a simple payload like `<script>alert(1)</script>`, we discovered that the comment box is vulnerable to stored XSS.
- Our task is to exploit this vulnerability in order to have the admin access the page and execute our XSS payload. This will enable us to make a new comment request which include their cookie on their behalf.
- An example of the payload is:
```
<script>
    let formData = new FormData();
    formData.append('name', 'testing');
    formData.append('comment', document.cookie);
    fetch('/new-comment', { method: "POST", body: formData});
</script>
```
- After we submit our payload, we can refresh our page and view the admin's cookie in one of the blog post's comments.
- We then override our own cookie with the admin's cookie.
- After successfully accessing `/admin` with the admin's cookie, we can see the flag.

Flag: `punk_{TMYJ77I275YCKC12}`
