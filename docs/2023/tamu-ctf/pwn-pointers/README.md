# Pointers
Category: Pwn

## Description
Author: `anomie`

I've been messing with pointers lately which never goes wrong, right?

Attachments: [pointers.zip](attachments/pointers.zip)

## Write-up
- By examining the code, we can identify that a buffer overflow can be exploited in the `vuln()` function.
- The buffer in `vuln()` is of size 8, and we can read up to 10 bytes. Therefore, we can overwrite 2 bytes of the saved rbp.
- The line `void (*poggers)() = func_ptrs[0];` assigns a function pointer from an offset relative to rbp.
- By carefully manipulating the saved rbp in `vuln()`, we can make `func_ptrs[0]` reference the `win()` function.
- Consequently, when `poggers()` is called, it will execute `win()`.

The solve script can be found [here](solution/solve.py).

Flag: `gigem{small_overflows_are_still_effective}`
