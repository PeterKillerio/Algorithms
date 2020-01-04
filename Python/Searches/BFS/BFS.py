import queue
import time

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

def returnNeighbours(mat, pos):
    possibles = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    found_neigh = []
    for possible in possibles:
        search_pos = [possible[0] + pos[0], possible[1] + pos[1]]
        if (( search_pos[0] >= 0 and search_pos[0] < len(mat)) and ( search_pos[1] >= 0 and search_pos[1] < len(mat[0]))):
            found_neigh.append(search_pos)
    return found_neigh

def BFS(maze, search, stack, visited):
    global GLOBAL_END_FLAG, DELAY
    if not GLOBAL_END_FLAG:
        if maze[search[0]][search[1]] == "E":
            print("\n Found the end. \n")
            GLOBAL_END_FLAG = True
            return
        elif visited[search[0]][search[1]] != -1:
            visited[search[0]][search[1]] = -1
            maze[search[0]][search[1]] = "."
            printMatrix(maze)
            #
            time.sleep(DELAY)
            #
            print()
            to_search = returnNeighbours(maze, search)
            for s in to_search:
                stack.put(s)
            while not stack.empty():
                BFS(maze, stack.get(), stack, visited)
    return

# Start
mat = createSimpleMaze(maze_dimension, start_position, end_position)
visited = create2DArray(maze_dimension[0], maze_dimension[1])
stack = queue.Queue()
printMatrix(mat)
BFS(mat, start_position, stack, visited)

