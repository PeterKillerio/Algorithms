import copy
import queue

class vein:
    def __init__(self, dict):
        self.dict = dict
        self.value = 0
    def __lt__(self, other):
        return self.value > other.value

def spill(node, memory, qu, coins, result, desired_value):
    for coin in coins:
        new_node = vein(copy.deepcopy(node.dict))
        new_node.dict[coin] += 1
        new_node.value = node.value + coin

        if not new_node.dict in memory:
            memory.append(copy.deepcopy(new_node.dict))
            if new_node.value < desired_value:
                qu.put(new_node)
            elif new_node.value == desired_value:
                result.append(new_node.dict)
                return True
            elif new_node.value > desired_value:
                break
    return False

Found = False # Found the change FLAG
result = [] # Memory to save result in
repetitions = 0 # Keep the count of the resets we did
qu = queue.PriorityQueue() # Priority queue where we are considering the highest value as the highest priority
coins = [1, 2, 5, 10, 20, 50] # AVAILABLE COIN VALUES
dict = {1:0, 2:0, 5:0, 10:0, 20:0, 50:0}
desired_main = 196589  # NUMBER TO CHANGE

multiple = desired_main // coins[-1] # What is the biggest amount we can make with the most valuable coin

while not Found:
    if repetitions > 1: # It should be possible to make change with these coins because desired left is biggest than the highest coin in the sack
        print("Not possible to make change with these coins.")
        break

    desired_left = (desired_main - (multiple * coins[-1]))  # Use the amount left to calculate change
    initial_vein = vein(copy.deepcopy(dict))  # Initial node with its own coin change to use memoization
    memory = [] # Reset memoization memory

    spill(initial_vein, memory, qu, coins, result, desired_left) # Start initial generation of nodes
    while not qu.empty():
        take_node = qu.get()
        if spill(take_node, memory, qu, coins, result, desired_left):
            Found = True
            break
    if not Found:
        multiple -= 1 # We cant exchange with these amount of 50 coins (highest coins), take one highest coin away and try again
        repetitions += 1

if Found:
    result[0][50] = multiple
    print(result)










