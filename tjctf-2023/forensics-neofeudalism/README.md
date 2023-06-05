# neofeudalism
Category: Forensics

## Description
One of my friends has gotten into neo-feudalism recently. He says that society should be more like a feudalist one, with unequal rights, legal protections, and wealth distribution.

I found this weird photo on his computer; can you find a flag?

Attachments: [image.png](attachments/image.png)

## Write-up
Performing a quick check using the following command reveals the flag:
```
zsteg --all image.png | grep ctf
```

![](solution/image.png)

Flag: `tjctf{feudalism_still_bad_ea31e43b}`
