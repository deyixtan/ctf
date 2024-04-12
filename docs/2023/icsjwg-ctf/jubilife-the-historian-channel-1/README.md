# The Historian Channel - 1
Category: Jubilife

## Description
Jubilife’s security operations center (SOC) team has noticed some alarms are missing from a historian dashboard on one of the internal ICS networks. This historian runs an Apache web server to host its database and allows users to query various settings, statuses, alarms, and warnings from devices on the network.

In these challenges, you will work with Jubilife’s SOC team to review the historian’s Apache logs and determine whether there is evidence of adversarial activity, and figure out how the alarms were deleted from the database.

Attached is the historian’s `access.log` file from the time period the SOC team would like you to review. Most users logged into the historian’s web server on their first attempt, if not their second or third, but one user repeatedly failed in an apparent brute force attempt before eventually logging in successfully.

What time did the suspicious user successfully login?

*Flag format: timestamp of the successful login from the suspicious user, without the timezone. Example: if the timestamp was [04/May/2023:09:24:56 -0500], the flag would be **04/May/2023:09:24:56***

Attachments: [access.log](attachments/access.log)

## Write-up
- To identify the group of requests related to the brute-force login process, we can search for `POST` requests made to `/login.php`.
- The last round of brute-force attempts appears to have started around the timestamp: `04/May/2023:12:21:38`.
- The last `POST` request to `/login.php` indicating a successful login is as follows: `192.168.4.146 - - [04/May/2023:12:22:50 -0500] "POST /login.php HTTP/1.1" 302 374 "http://jubilifehistorian/login.php" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"`.
- The timestamp for the last successful login `POST` request is `04/May/2023:12:22:50`.

Flag: `04/May/2023:12:22:50`
