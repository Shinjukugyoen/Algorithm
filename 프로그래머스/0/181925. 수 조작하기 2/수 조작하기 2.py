def solution(numLog):
    moves = {
        1 : 'w',
        -1 : 's',
        10 : 'd',
        -10 : 'a'
    }
    num_move_Log = ''
    for i in range(len(numLog) - 1):
        num_move_Log += moves[numLog[i + 1] - numLog[i]]
    return num_move_Log