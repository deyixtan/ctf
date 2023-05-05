# Password Cracking - 4
Category: Password Cracking

## Description
`$6$XM4TZ5vb6W/0SjIl$PsddDrA8bOKbVXApHrz9NKaF9BH92Fs1aKn6MFHelf1he8z7rbR9Af12FqynqlU2lHILU/FgNaDVUFCK2yc4B0`

The flag is the password corresponding with this hash.

## Write-up
- The hash content can be saved inside a file called `hash.hash`.
- The next step is to initiate John's attack using the command `john --wordlist=/usr/share/wordlists/rockyou.txt hash.hash`.
- After the analysis by John, you can execute `john --show hash.hash > password.txt` to obtain the password for the vault. The password will be saved in the `password.txt` file, and in this case, the password is `zebrasrule`.

Flag: `zebrasrule`
