# This recursive algorithm takes an input of 3 numbers
# N_round number stands for round brackets pairs
# M_blocky number stands for square brackets pairs
# O_curly number stands for curly brackets pairs

# The output is all the correctly generated brackets 

def rec_create(total, used, priority_q, state):
    if len(state) >= ((total[0]+total[1]+total[2])*2):
        for w in state:
            print(w, end='')
        print()

    priority = -1
    if len(priority_q) != 0:
        priority = priority_q[-1]

    for i in range(len(used)):
        if priority == i:
            new_used = used.copy()
            new_queue = priority_q.copy()
            new_queue.pop()
            new_state = state.copy()
            new_state.append(brackets[priority][1])
            rec_create(total, new_used, new_queue, new_state)
        if used[i] < total[i]:
            new_used = used.copy()
            new_used[i] += 1
            new_queue = priority_q.copy()
            new_queue.append(i)
            new_state = state.copy()
            new_state.append(brackets[i][0])
            rec_create(total, new_used, new_queue, new_state)

brackets = ["()", "[]", "{}"]

N_round = int(input())
M_blocky = int(input())
O_curly = int(input())

total_brack = [N_round, M_blocky, O_curly]
used_brack = [0, 0, 0]
priority_queue, current_state = [], []

rec_create(total_brack, used_brack, priority_queue, current_state)