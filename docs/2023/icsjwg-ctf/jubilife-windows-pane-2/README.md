# Windows Pane - 2
Category: Jubilife

## Description
Due to this logon behavior, Jubilife would like to perform additional forensics on Abigail's machine. The attached prefetch data was extracted from their machine and Jubilife would like your assistance to find any evidence of a malicious executable.

What is the full directory path of the malicious backdoor executable?

*Flag format: full directory path of malicious executable. Example: **C:\Users\User\Desktop\Path.exe***

Note: A Windows machine or Windows VM is recommended for solving this challenge.

Attachments: [Prefetch.zip](attachments/Prefetch.zip)

## Writeup
- Since the provided attachments contain Windows Prefetch files, we can utilize a useful tool called `PECmd` to parse these files.
- Running `PECmd` on the Prefetch files will generate a parsed output file, which can be found here: [PECmd_output.txt](solution/PECmd_output.txt).
- During our analysis, we focused on identifying executable files (`.exe`) within the Prefetch data.
- We observed several entries in the parsed output marked as `(Executable: True)`, indicating that they are executable files.
- To narrow down our results, we decided to include only those entries that have the `(Executable: True)` attribute.
- Fortunately, within the filtered results, we discovered a file named `B@CKD00R.EXE` which was likely malicious located at the following path: `C:\USERS\ABIGAIL_FORBES\DESKTOP\SECRET\B@CKD00R.EXE`.

Flag: `C:\USERS\ABIGAIL_FORBES\DESKTOP\SECRET\B@CKD00R.EXE.`
