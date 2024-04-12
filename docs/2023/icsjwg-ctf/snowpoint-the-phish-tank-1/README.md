# The Phish Tank - 1
Category: Snowpoint

## Description
Snowpoint has an internal mail server, which is used by field engineers on computers that do not have access to the Internet. Some of these engineers have reported emails that look suspiciously like phishing attempts. The internal mail server is very basic, and because it is located on an internal network, the Snowpoint staff did not spend much time configuring security or encryption. Consequently, all emails are sent over unencrypted **SMTP**.

Network traffic from these emails is ingested into Malcolm. Since this network is not connected to the Internet, Snowpoint’s security team would like you to look at these emails and, if they do prove to be phishing emails, determine how they were sent from an internal network. The first step is identifying the source of the suspicious emails.

What is the IP address of the computer that sent the phishy emails?

*Flag format: IP Address. Example: **192.168.1.20***

## Write-up
- To identify potentially malicious or phishing emails, we can access the Malcomm `SMTP` dashboard.
- By examining the logs within the `SMTP - Logs` table, we discovered suspicious emails with subjects indicating potential phishing attempts. Two notable examples are emails with subjects `Annual Report Attached! Do not Miss!!` and `Account Expiration!!! Please Open Immediately!`.
- These emails originated from the sender's address `candice.abomasnow@snowpoint-field.org` and were sent from the IP address `10.140.1.105`.

Flag: `10.140.1.105`
