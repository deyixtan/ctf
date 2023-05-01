# Unlucky
Category: Pwn

## Description
Author: `nhwn`

Luck won't save you here. Have fun trying to get the flag!

Attachments: [unlucky.zip](attachments/unlucky.zip)

## Write-up
- The binary has the PIE (Position Independent Executable) security mechanism disabled.
- We are provided with the address of the `main()` function.
- By calculating the offset of the `static int seed` variable from `main()`, we can determine its address on the remote server.
- The address of `seed` is used as a parameter for the `srand()` function.
- Once we know our `srand()` parameter, we can get the answers to the 8 questions, leading us to our flag.

The solve script can be found [here](solution/solve.py).

Flag: `gigem{1_n33d_b3tt3r_3ntr0py_s0urc3s}`
