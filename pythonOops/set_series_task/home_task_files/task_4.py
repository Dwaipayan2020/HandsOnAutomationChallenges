"""4. Write a program to read a file and copy it into a
new file"""
import contextlib


@contextlib.contextmanager
def opened(file_path, mode):
    # print('Inside Context Manager')
    f = open(file_path, mode, encoding='utf-8')
    yield f
    # print('closing the file')
    f.close()


text = input()
with opened('new_file_2130', 'w') as file:
    file.write(text)
with opened('new_file_2130', 'r') as file:
    file_content = file.read()
    # print(file_content)
file_content_lst = file_content.split()
lgt = len(file_content_lst)
lst = list()
for item in file_content:
    if str(item).islower():
        lst.append(str(item).upper())
    elif str(item).isupper():
        lst.append(str(item).lower())

new_text = ''.join(lst)
with opened('new_file_2131', 'w') as file:
    file.write(new_text)

with opened('new_file_2131', 'r') as file:
    new_file_content = file.read()
    print(new_file_content)
