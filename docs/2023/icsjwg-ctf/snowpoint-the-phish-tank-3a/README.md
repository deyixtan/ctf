# The Phish Tank - 3a
Category: Snowpoint

## Description
The suspicious IP address sent another email, which contained a Microsoft Word document attachment. The user who attempted to open this document saw the banner warning that the document contained macros and immediately closed the document and reported it to Snowpoint’s security team.

The Snowpoint team would like your assistance extracting this Microsoft Word document and analyzing the macros it contains. Based on initial analysis, they believe it is an `msfvenom` created macro that attempts to make reverse TCP connection back to another computer. Since this is an internal network, they are confident the IP address starts with `10.140`.

What IP address does this macro attempt to connect to?

*Flag format: IP Address. Example: **10.140.1.1***

## Write-up
- Building upon the findings from [The Phish Tank - 2](../snowpoint-the-phish-tank-2/README.md), we continued our investigation into the SMTP-related files within the [https://malcolm.icsjwgctf.com/extracted-files/](https://malcolm.icsjwgctf.com/extracted-files/) directory.
- During our search, we came across a `.docx` file associated with the `SMTP` category. The file can be accessed at the following location: [https://malcolm.icsjwgctf.com/extracted-files/preserved/SMTP-FNYyzR1GG2L5WnBFx3-CTN9Fg3Os5dY2dpYJj-20230504181928.docx](https://malcolm.icsjwgctf.com/extracted-files/preserved/SMTP-FNYyzR1GG2L5WnBFx3-CTN9Fg3Os5dY2dpYJj-20230504181928.docx).
- Alternatively, a conveniently scraped version of the file can be found here: [SMTP-FNYyzR1GG2L5WnBFx3-CTN9Fg3Os5dY2dpYJj-20230504181928.zip](solution/SMTP-FNYyzR1GG2L5WnBFx3-CTN9Fg3Os5dY2dpYJj-20230504181928.zip).
- To perform static and dynamic malware analysis, we proceeded to upload the `.docx` file to VirusTotal.
- Upon analyzing the behavior of the malware, we observed an attempt to access an internal IP address (`10.140.1.15`). The detailed report can be found at the following link: [https://www.virustotal.com/gui/file/0ffc5a32b575a8824c7760cdce4f44e102ac673ee8cb5ac8c5060df49c88e066/behavior](https://www.virustotal.com/gui/file/0ffc5a32b575a8824c7760cdce4f44e102ac673ee8cb5ac8c5060df49c88e066/behavior).

Flag: `10.140.1.15`
