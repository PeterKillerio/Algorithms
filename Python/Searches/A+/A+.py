import queue
import time
import math

class positionData():
    def __init__(self, coord, cost, end):
        self.coord = coord
        self.start_cost = cost
        self.whole_cost = calculateCost(coord, end)
    def __int__(self):
        return self.whole_cost
    def __lt__(self, other):
        return self.whole_cost < other.whole_cost

##############Parameters################
maze_dimension = [11, 11] # ROW, COL
start_position = [2, 2]
end_position = [8, 9]
GLOBAL_END_FLAG = False
DELAY = 0.1
########################################

def printMatrix(mat):
    for row in range(len(mat)):
        for col in range(len(mat[0])):
            print(mat[row][col], end=" ")
        print()

def create2DArray(size, depth):
  array = [0] * size
  for i in range(len(array)):
    array[i] = [0] * depth
  return array

def createSimpleMaze(size, start, end):
    mat = create2DArray(size[0], size[1])
    mat[start[0]][start[1]] = "S"
    mat[end[0]][end[1]] = "E"
    return mat

def returnNeighbours(mat, pos, end):
    possibles = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    found_neigh = []
    for possible in possibles:
        search_pos = [possible[0] + pos.coord[0], possible[1] + pos.coord[1]]
        if (( search_pos[0] >= 0 and search_pos[0] < len(mat)) and ( search_pos[1] >= 0 and search_pos[1] < len(mat[0]))):
            tempData = positionData(search_pos, pos.start_cost, end)
            found_neigh.append(tempData)
    return found_neigh

def A_star(maze, search, stack, visited, end):
    global GLOBAL_END_FLAG, DELAY
    if not GLOBAL_END_FLAG:
        if maze[search.coord[0]][search.coord[1]] == "E":
            print("\n Found the end. \n")
            GLOBAL_END_FLAG = True
            return
        elif visited[search.coord[0]][search.coord[1]] != -1:
            visited[search.coord[0]][search.coord[1]] = -1
            maze[search.coord[0]][search.coord[1]] = "."
            printMatrix(maze)
            print()
            #
            time.sleep(DELAY)
            #
            to_search = returnNeighbours(maze, search, end)
            for s in to_search:
                stack.put(s)
            while not stack.empty():
                A_star(maze, stack.get(), stack, visited, end)
    return

def calculateCost(curr, desired):
    return math.sqrt((curr[0]-desired[0])**2 + (curr[1]-desired[1])**2)

# Start
mat = createSimpleMaze(maze_dimension, start_position, end_position)
visited = create2DArray(maze_dimension[0], maze_dimension[1])
stack = queue.PriorityQueue()
printMatrix(mat)
startData = positionData(start_position, 0, end_position)
A_star(mat, startData, stack, visited, end_position)