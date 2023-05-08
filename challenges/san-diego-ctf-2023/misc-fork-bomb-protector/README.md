# Fork bomb protector
Category: Misc

## Description
We built a playground for people to try out Linux. We are tired of customer complaints about malicious fork bombs rummaging the server, hogging system resources, and bringing everything down to a crawl, so we built our own proprietary fork-bomb protector. As an "unintended" consequence of that, people cannot run commands normally. Our genius head of the engineering team suggests this to be a security "feature", not a bug, since this essentially turns our product into a restricted shell. Bye bye, RCEs!

Attachments: [nofork.py](attachments/nofork.py)

Connect via: `socat FILE:$(tty),raw,echo=0 TCP:nofork.sdc.tf:1337`

## Write-up
- Upon examining the attached file, we discovered that `fork`, `vfork`, and `clone` were forbidden.
- In a shell, when a command is evaluated, the shell forks a new process to run the command, which allows the shell to continue running while the command is executing.
- One option for executing shell commands in the same environment is to use a shell built-in command rather than an external command. Built-in commands are executed directly by the shell without forking a new process. Some examples of built-in commands in the Bash shell include `cd`, `echo`, and `pwd`. However, the range of available built-in commands is limited.
- Fortunately, we can use the `exec` command to replace the shell process with our specified command, which allows us to bypass the restrictions and retrieve the flag.
- The following commands demonstrate how to use `exec` to break out of the restrictions and retrieve the flag:
```
exec ls
exec cat flag.txt
```

Flag: `sdctf{ju5T_3xEc_UR_w4y_0ut!}`
