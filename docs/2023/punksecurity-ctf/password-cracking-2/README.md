# Password Cracking - 2
Category: Password Cracking

## Description
The flag is the password for this vault.

Attachments: [keepass.kdbx](attachments/keepass.kdbx)

## Write-up
- To make the contents of the `keepass.kdbx` file compatible with John The Ripper, we can use the command `keepass2john keepass.kdbx > keepass.hash`.
- The next step is to initiate John's attack using the command `john --wordlist=/usr/share/wordlists/rockyou.txt keepass2john.hash`.
- After the analysis by John, you can execute `john --show keepass2john.hash > password.txt` to obtain the password for the vault. The password will be saved in the `password.txt` file, and in this case, the password is `zebracakes`.

Flag: `zebracakes`
