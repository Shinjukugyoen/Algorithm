_ = int(input())
num_list = list(map(int, input().split()))
max_num = min_num = num_list[0]

for num in num_list:
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num
print(min_num, max_num)