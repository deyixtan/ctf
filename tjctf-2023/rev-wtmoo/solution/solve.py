encoded = list("8.'8*{;8m33[o[3[3[%\")#*\\}")

decoded = ""
for c in encoded:
    if c == "{" or c == "}":
        decoded += c
        continue

    new_c = ord(c) + 60
    if new_c >= 97 and new_c <= 122:
        decoded += chr(new_c)
        continue

    new_c = ord(c) - 32
    if new_c >= 65 and new_c <= 90:
        decoded += chr(new_c)
        continue
    
    new_c = ord(c) - 43
    if new_c >= 48 and new_c <= 52:
        decoded += chr(new_c)
        continue

    new_c = ord(c) + 21
    if new_c >= 53 and new_c <= 57:
        decoded += chr(new_c)
        continue

print(decoded)
