def solution(num_list):
    even_list = []
    odd_list = []
    for i in num_list:
        if i % 2 == 1:
            odd_list.append(str(i))
        else:
            even_list.append(str(i))
            
    return int("".join(odd_list)) + int("".join(even_list))