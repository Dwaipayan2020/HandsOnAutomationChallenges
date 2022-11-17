a_num = ord('a')
z_num = ord('z')
f = open('new_file3.txt', 'w')
for i in range(a_num, z_num+1):
    f.write(f'{chr(i)} ')
f.close()
f1 = open('new_file4.txt', 'r')
print(f1.read())
f1.close()

