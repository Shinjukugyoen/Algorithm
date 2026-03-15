n = int(input())
num_list = list(map(int, input().split()))
MAX_num = MIN_num = num_list[0]

for num in num_list:
    if num < MIN_num:
        MIN_num = num
    if num > MAX_num:
        MAX_num = num
print(MIN_num, MAX_num)