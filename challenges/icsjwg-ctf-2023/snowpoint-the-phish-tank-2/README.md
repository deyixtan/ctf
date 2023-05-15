# The Phish Tank - 2
Category: Snowpoint

## Description
Snowpoint’s security team spoke with an engineer who admitted to clicking a link included in an email with the subject line: `Account Expiration!!! Please Open Immediatelly!`. Luckily, the computer they clicked the link from did not have access to the Internet, so they were unable to reach the URL and nothing else happened. However, the security team would still like to know what the URL from this link was so they can add it to their blacklist and keep an eye on any attempted connections.

What is the URL included in the email with subject line `Account Expiration!!! Please Open Immediatelly!`?

*Flag format: full URL. Example: [https://icsjwgctf.com/scoreboard](https://icsjwgctf.com/scoreboard)*

## Write-up
- From the Malcomm `SMTP` dashboard, we identified an email with the subject line `Account Expiration!!! Please Open Immediately!` that corresponds to the root ID `CBIVUm1MPhhOO6pBC9`.
- To access the associated files in Malcomm, we can visit the following URL: [https://malcolm.icsjwgctf.com/extracted-files/](https://malcolm.icsjwgctf.com/extracted-files/).
- Specifically, there is a text file related to the email's root ID, which can be accessed here: [https://malcolm.icsjwgctf.com/extracted-files/preserved/SMTP-Fndvzf1WbdaLcOQRJc-CBIVUm1MPhhOO6pBC9-20230504180919.txt](https://malcolm.icsjwgctf.com/extracted-files/preserved/SMTP-Fndvzf1WbdaLcOQRJc-CBIVUm1MPhhOO6pBC9-20230504180919.txt).
- Alternatively, a conveniently scraped version of the file can be found here: [SMTP-Fndvzf1WbdaLcOQRJc-CBIVUm1MPhhOO6pBC9-20230504180919.txt](solution/SMTP-Fndvzf1WbdaLcOQRJc-CBIVUm1MPhhOO6pBC9-20230504180919.txt).
- Upon examining the contents of this file, we discovered the full URL associated with the malicious email.

Flag: `https://snnowpoint_updater.snow/password_change`
