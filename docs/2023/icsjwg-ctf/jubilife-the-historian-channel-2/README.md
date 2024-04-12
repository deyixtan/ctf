# The Historian Channel - 2
Category: Jubilife

## Description
Jubilife’s SOC looked for other suspicious events around the time of the successful brute force login and noticed earlier activity from the suspicious user (IP address 192.168.4.146) in the web server logs. It looks like this user attempted to access information on the webserver without logging in, and it is possible that they succeeded in reading files they were not supposed to have access to due to a misconfiguration.

What is the name of the file (full path) that the suspicious user accessed from the webserver?

*Flag format: full path of file. Example: if the file accessed was /folder/file.txt, the flag would be **/folder/file.txt***

Attachments: [access.log](attachments/access.log)

## Write-up
- According to the information obtained in [The Historian Channel - 1](../jubilife-the-historian-channel-1/README.md), the last successful login occurred at `04/May/2023:12:22:50`.
- Therefore, the unauthorized configuration access must have taken place before that timestamp.
- A few minutes before the successful brute-force attempt at `04/May/2023:12:06:58`, there is a `GET` request to `/jubilifehistorian/config.ini` with a status code of `200`, indicating unauthorized configuration access.
- The specific request in the log is as follows: `192.168.4.146 - - [04/May/2023:12:06:58 -0500] "GET /jubilifehistorian/config.ini HTTP/1.1" 200 1635 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"`.
- The configuration file accessed is at `/jubilifehistorian/config.ini`.

Flag: `/jubilifehistorian/config.ini`
