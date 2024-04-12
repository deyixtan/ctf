# The Phish Tank - 3b
Category: Snowpoint

## Description
An additional email sent from that same suspicious IP address contained an attached PDF document. The user who opened this document started to fill out the form, but became suspicious and reported it to Snowpoint’s security team instead of hitting the submit button.

The Snowpoint security team would like you to download the attached PDF document and determine what would happen if the submit button was clicked.

Where would the sensitive information provided in the form be sent?

*Flag format: email address. Example: [icsjwgctf@gmail.com](icsjwgctf@gmail.com)*

## Write-up
- Expanding on the findings from [The Phish Tank - 2](../snowpoint-the-phish-tank-2/README.md), we proceeded with our investigation into the SMTP-related files within the [https://malcolm.icsjwgctf.com/extracted-files/](https://malcolm.icsjwgctf.com/extracted-files/) directory.
- During our search, we identified a relevant `.pdf` file associated with the `SMTP` category. It can be accessed at the following location: [https://malcolm.icsjwgctf.com/extracted-files/preserved/SMTP-F5Jne44ZcJTJIP7Dd7-CW3dJj4z4tRWk9d65g-20230504183014.pdf](https://malcolm.icsjwgctf.com/extracted-files/preserved/SMTP-F5Jne44ZcJTJIP7Dd7-CW3dJj4z4tRWk9d65g-20230504183014.pdf).
- As an alternative, a conveniently scraped version of the file can be found here: [SMTP-F5Jne44ZcJTJIP7Dd7-CW3dJj4z4tRWk9d65g-20230504183014.zip](solution/SMTP-F5Jne44ZcJTJIP7Dd7-CW3dJj4z4tRWk9d65g-20230504183014.zip).
- To conduct dynamic malware analysis, we proceeded to upload the `.pdf` file to `Hybrid Analysis`.
- During the analysis, the field labeled `Found a potential E-Mail address in binary/memory` detected the pattern `upiter47@galactic.plat`.
- Based on this discovery, we made an informed guess that the flag is `jupiter47@galactic.plat`, and our assumption turned out to be correct.

Flag: `jupiter47@galactic.plat`
