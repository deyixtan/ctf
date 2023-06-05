# Secure Runner
Category: Misc

## Description
I made a service where people can upload C code to my server and run it! The best part is that it's completely secure! Try running the number guessing game I made :)

Connect via `cat program.c - | nc secure-runner.sdc.tf 1337`

Attachments: [program.c](attachments/program.c)

## Write-up
- We began by running the provided command in the description, which revealed to us that the remote server will execute the file we supply.
- We examined the source code of [program.c](attachments/program.c), but it did not reveal anything related to the flag, nor did it appear to be vulnerable to remote code execution to gain access to the flag.
- It seemed that the attack vector was the program that we provided as input to `nc`.
- We wrote a simple payload in C that executed `system("/bin/sh")` and attempted to supply this payload to `nc`. However, we received an error message indicating an invalid checksum.
- After experimenting with the payload, we discovered that the checksum was the `crc32` of the file content.
- We used a tool called [force32.py](solution/force32.py) by [Project Nayuki](https://www.nayuki.io/page/forcing-a-files-crc-to-any-value) to forge the `crc32` value of our [payload.c](solution/payload.c) file (to match with `program.c`'s), resulting in a similar C payload but with its `crc32` content forged. The resulting file was named [payload_forced.c](solution/payload_forced.c). The command used to generate the forged payload is `python3 force32.py payload.c 70 38DF65F2`.
- We supplied our forged payload to `nc` and popped a shell by using the following command: `cat payload_forged.c - | nc secure-runner.sdc.tf 1337`.
- We ran `ls`, it revealed a `flag.txt` file. We were able to retrieve the flag by running `cat flag.txt`.

Flag: `sdctf{n0w_th4t5_wh4t_i_ca1l_crcecurity!}`
