# Turtle Shell
Category: Pwn

## Description
A turtle without it's shell is a sad sight to see

Connect via: `nc turtle.sdc.tf 1337`

Attachments: [Dockerfile](attachments/Dockerfile), [turtle-shell](attachments/turtle-shell)

## Write-up
- The first step in solving this challenge was to check which protection mechanisms were enabled using `checksec`. It turned out that none were enabled, which made the challenge easier to exploit.
- Next, we opened up the binary [turtle-shell](attachments/turtle-shell) in Ghidra and analyzed the code. We found that the program takes user input of size `50` and then checks if a constant buffer (needle) exists within our user input (haystack).
- As long as the user input cannot be found in the constant buffer, the program will start executing our input. We can write shell code to our buffer and have it executed.
- We created a Python script to automate this process, which can be found [here](solution/solve.py).
- After running the script and popping a shell, we were able to find the flag in `flag.txt` in the current working directory.

Flag: `sdctf{w0w_y0u_m4d3_7h3_7urT13_c0m3_0u7_0f_1t5_5h3l1}`
