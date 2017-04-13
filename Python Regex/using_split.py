import re


num = input()
num_list = re.split(r'[.,]?', num)
for entry in num_list:
    if entry:
        print(entry)
