n = int(input())
int_array = list(map(int, input().split()))   
v = int(input())
v_count = 0

for i in range(n):
    if v == int_array[i]:
        v_count += 1 
   
print(v_count) 