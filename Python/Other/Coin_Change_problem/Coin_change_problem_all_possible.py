import copy
import queue
# Breath first search way of finding all the combinations of coins you can make change with

class vein: # Node with its own dictionary and time tracker used for priority queue LOWER TIME - HIGHER PRIORITY
    def __init__(self, time, dict):
        self.dict = dict
        self.time = time
        self.value = 0
    def __lt__(self, other):
        return self.time < other.time

def spill(node, memory, qu, coins, result, desired_value):
    global TIME
    for coin in coins:
        TIME += 1
        new_node = vein(TIME, copy.deepcopy(node.dict))
        new_node.dict[coin] += 1
        new_node.value = node.value + coin

        if not new_node.dict in memory:
            memory.append(new_node.dict)
            if new_node.value < desired_value:
                if TIME % 100 == 0:
                    print(f"TIME: {TIME}.")
                qu.put(new_node)
            elif new_node.value == desired_value:
                result.append(new_node.dict)
            elif new_node.value > desired_value:
                break

coins = [1, 2, 5, 10, 20, 50] # Coins you have
dict = {1:0, 2:0, 5:0, 10:0, 20:0, 50:0}
result = [] # Memory to store results in
memory = [] # Memory to make use of memoization
desired = 40 # The amount you want to make change with
qu = queue.PriorityQueue()
TIME = 0

initial_vein = vein(0, dict) # Initial empty node
spill(initial_vein, memory, qu, coins, result, desired) # Generating all the other nodes and add them to priority queue

while not qu.empty():
    take_node = qu.get()
    spill(take_node, memory, qu, coins, result, desired)

for i in result:
    print(i)
print(f"Total possibilities: {len(result)}.")








