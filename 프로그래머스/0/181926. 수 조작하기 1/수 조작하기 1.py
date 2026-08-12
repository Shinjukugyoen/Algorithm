def solution(n, control):
    moves = {    "w" : 1,
        "s" : -1,
        "d" : 10,
        "a" : -10
            }

    for i in control:
        n += moves[i]
    return n