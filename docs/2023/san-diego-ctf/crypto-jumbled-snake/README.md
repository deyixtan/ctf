# Jumbled snake
Category: Crypto

## Description
Can you unravel the jumbled snake?

Attachments: [print_flag.py.enc](attachments/print_flag.py.enc) [jumble.py](attachments/jumble.py)

## Write-up
- Our objective in this challenge is to obtain the original, decoded version of `print_flag.py` by decoding `print_flag.py.enc`.
- The code snippet in `jumble.py` indicates that the encoded content of `print_flag.py` starts from the second line in `print_flag.py.enc`, as seen in the following code:
```
dst.write(doc + '\n')
dst.write(subs(src.read(), key))
```
- Furthermore, `jumble.py` contains the shebang `#! /usr/bin/env python3`, which is likely used in `print_flag.py`.
- To begin decoding the file, we can use a hexdump tool to examine the encoded file content and attempt to map it to the given shebang. By doing so, we can partially decode `print_flag.py`.
- We can further improve our mapping by solving the characters in `{'the_quick_brown_fox_jumps_over_the_lazy_dog': 123456789.0, 'items':[]}`, which is part of `decode_flag.__doc__`.
- We can then continue refining our mapping by solving the characters in `check.__doc__`.
- Using these information, our mapping can be used to obtain the fully decoded [`print_flag.py`](solution/print_flag.py).
- Within `print_flag.py`, the value of the variable `coded_flag` can be base64 decoded to obtain the flag.
- The script to fully decode `print_flag.py.enc` can be found [here](solution/solve.py).

Flag: `sdctf{U_unRav3led_tH3_sn3k!}`
