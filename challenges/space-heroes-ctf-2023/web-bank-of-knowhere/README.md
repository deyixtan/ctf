# Bank-of-Knowhere
Category: Web

## Description
Groot is in dire need of some crucial intel about the Bank of Knowhere, but they only share such classified information with their inner circle. In order to become a member of their inner circle, one must have at least 2000₳ - Units in their bank account. Can you lend a hand to Groot in acquiring this information? Remember, as Peter Quill once said, "We're the frickin' Guardians of the Galaxy, we're supposed to protect the galaxy, not destroy it!"

[http://knowhere.hackers.best:31337/](http://knowhere.hackers.best:31337/) OR [spaceheroes-bank-of-knowhere.chals.io](spaceheroes-bank-of-knowhere.chals.io)

Author: bl4ckp4r4d1s3

## Write-up
- By examining the `/robots.txt` file, it reveals a `/admin` URL used to access and pay for the flag.
- Payments can be made using using a format like `/index.php?sender=Groot&receiver=Nebula&amount=500`.
- However, there are checks in place to prevent sending money to oneself, for example, `/index.php?sender=Nebula&receiver=Groot&amount=500`.
- To bypass this restriction, `parameter pollution` can be utilized. By including duplicate receiver parameters, such as `/index.php?sender=Nebula&receiver=Nebula&receiver=Groot&amount=2649`, it is possible to exploit variations in URL parsing implementations across libraries. This discrepancy leads to different parameters with the same name being checked separately, thus bypassing the validation mechanism.
- Navigating to the `/admin` URL reveals the flag.

Flag: `shctf{7h3_c0sm0s_1s_w17h1n_u5}`
