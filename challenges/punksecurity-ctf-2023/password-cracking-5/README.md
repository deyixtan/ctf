# Password Cracking - 5
Category: Password Cracking

## Description
`fd217a229b674ae4bcb82a0bb4751e11`

The flag is the password corresponding with this hash.

## Write-up
- The hash content can be saved inside a file called `hash.hash`.
- The next step is to initiate John's attack using the command `john --format=Raw-MD5 --wordlist=/usr/share/wordlists/rockyou.txt hash.hash`.
- After the analysis by John, you can execute `john --show --format=Raw-MD5 hash.hash > password.txt` to obtain the password for the vault. The password will be saved in the `password.txt` file, and in this case, the password is `16drunkzebras`.

Flag: `16drunkzebras`
