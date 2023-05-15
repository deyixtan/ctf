# Windows Pane - 1
Category: Jubilife

## Description
Jubilife's information technology (IT) team has seen unusual login event activity and would like your help identifying any suspicious activity in the attached logs.

Jubilife has a strict company policy that each employee is assigned a single device and unique user account, and is only permitted to access the network from their device.

This policy is in place to help IT by limiting each user to only be logged into one device at any given time; therefore, no user can be logged in twice at the same time.

What is the username of the account that is noncompliant with this company policy?

*Flag format: username of the noncompliant account. If the username is MARK_ZUCKER, the flag would be **MARK_ZUCKER***

Attachments: [LogonEvents.csv](attachments/LogonEvents.csv)

## Writeup
- According to the given description, it is stated that each user can only be logged into one device simultaneously.
- The objective is to identify the username that is noncompliant with this company policy by detecting instances of two consecutive logon events without a logoff event in between. In other words, we are looking for situations where a user logs into multiple devices without properly logging out from the initial device.
- To achieve this, we plan to utilize Python for parsing the CSV file that contains the logon events. Our approach involves grouping the events based on the username, sorting the events chronologically, and then analyzing each group events sequentially to identify consecutive logons.
- The mentioned process is written in the [solve.py](solution/solve.py) script.

Flag: `ABIGAIL_FORBES`
