# Password Cracking - 1
Category: Password Cracking

## Description
The flag is the password for this vault.

Attachments: [supersecrets.yml](attachments/supersecrets.yml)

## Write-up
- To make the contents of the `supersecrets.yml` file compatible with John The Ripper, we can use the command `ansible2john supersecrets.yml > supersecrets.hash`.
- The next step is to initiate John's attack using the command `john --wordlist=/usr/share/wordlists/rockyou.txt supersecrets.hash`.
- After the analysis by John, you can execute `john --show supersecrets.hash > password.txt` to obtain the password for the vault. The password will be saved in the `password.txt` file, and in this case, the password is `zebracrossing`.

Flag: `zebracrossing`
