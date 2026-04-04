max_num = int(input())
max_index = 1

for i in range (2, 10):
    n = int(input())
    if (n > max_num):
        max_num = n
        max_index = i

print(f"{max_num}\n{max_index}")