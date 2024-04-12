# Chrome-Plated Nonsense - 1
Category: Jubilife

## Description
Jubilife’s security operations center (SOC) team is looking into anomalous traffic from an employee’s Windows machine. When asked if they had recently seen anything odd or made any changes to their machine, the employee admitted to installing two new Chrome extensions.

Jubilife would like you to review these Chrome extensions and determine whether they are causing the anomalous traffic and what, if any, malicious behavior they perform.

The first extension is named Chrome-Speedboost (see attached crx file). The employee installed this extension to speed up their web browsing, but based on traffic the Jubilife SOC team has seen, they believe this extension is exfiltrating information.

What are the IP address and port of the server the malicious extension is sending the exfiltrated data to?

*Flag format: IP address and port. Example: if the IP is 8.8.8.8 and the port is 53, the flag would be **8.8.8.8:53***

Attachments: [chrome-speedboost.crx](attachments/chrome-speedboost.crx)

## Write-up
- We can start by doing some forensics analysis on the file
- We can proceed by checking for embedded files, and extract them if present. This can be done using `binwalk -e chrome-speedboost.crx`.
- Within the list of extracted is a `background.js` which seems to be the script linked to a chrome extension. Within the script we manage to retrieve the IP and port used to send data to.

- To begin the forensics analysis of the file, we can perform various examination techniques.
- One approach is to check for any embedded files within the file. In this case, we can use the command `binwalk -e chrome-speedboost.crx` to extract any embedded files if present.
- Among the [list of extracted files](solution/_chrome-speedboost.crx.extracted.zip), we come across a file named `background.js`, which appears to be the script associated with a Chrome extension.
- By analyzing the contents of `background.js`, we are able to retrieve the IP address and port number used for data transmission.

Flag: `192.88.99.24:8080`
