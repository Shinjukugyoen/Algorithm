n, x = map(int, input().split())

num_array = list(map(int, input().split()))
for num in num_array:
    if num < x:
        print(num, end = " ")