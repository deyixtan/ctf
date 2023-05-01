from pwn import *
from ctypes import CDLL

p = remote("tamuctf.com", 443, ssl=True, sni="unlucky")

main_addr = p.recvline().decode().split(" ")[-1][2:]
seed_addr = int(main_addr, 16) + 0x2EC3

libc = CDLL("libc.so.6")
libc.srand(seed_addr)

for i in range(1, 8):
    print(p.recvline().decode(), end="")

    ans = libc.rand()
    p.sendline(str(ans).encode())
    print(ans)

p.interactive()
