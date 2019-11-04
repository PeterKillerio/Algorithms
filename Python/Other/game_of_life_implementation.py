import time

# Define number of iterations for the game of life
numberOfIterations = 50
# Define delay between iterations in seconds
pauseTime = 0.2

# Define your own grid
a = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
   ]
# ALL DONE

def create2DArray(size, depth):
    array = [0]*size
    for i in range(len(array)):
        array[i] = [0]*depth
    return array

def isDefined(array, idxY, idxX):
    sizeY = len(array) -1
    sizeX = len(array[0]) -1

    if(idxX >= 0 and idxX <= sizeX):
        if(idxY >= 0 and idxY <= sizeY):
            return True
    return False

def countNeighbors(array, idxY, idxX):
    allNeighbors = []

    plusMinusOne = [1, -1, 0]
    for i in plusMinusOne:
        for l in plusMinusOne:
            allNeighbors.append([i, l])

    #delete last item 0,0
    allNeighbors.pop()

    numberOfNeighbors = 0
    for i in allNeighbors:

        indexY = idxY + i[0]
        indexX = idxX + i[1]

        if(isDefined(array, indexY, indexX)):
            if(array[indexY][indexX] == 1):
                numberOfNeighbors += 1

    return numberOfNeighbors

def printBeautifiedArray(array):
    for r in range(len(array)):
        for c in range(len(array[0])):
            toPrint = ""
            if(array[r][c] == 1): toPrint = "O"
            else: toPrint = "."
            print(toPrint + " ", end='')
        print("")



sizeY = len(a)
sizeX = len(a[0])

#numberOfIterations = 50

startGrid = a
for i in range(numberOfIterations):
    time.sleep(pauseTime)
    lifeGrid = create2DArray(sizeY, sizeX)

    for y in range(len(startGrid)):
        for x in range(len(startGrid[0])):
            #Count all neighbors
            numberOfNeighbors = countNeighbors(startGrid, y, x)
            #Am I alive?
            alive = False
            if(startGrid[y][x] == 1): alive = True

            if(numberOfNeighbors == 3):
                lifeGrid[y][x] = 1
            elif(numberOfNeighbors == 2):
                if(alive): lifeGrid[y][x] = 1
            else:
                lifeGrid[y][x] = 0

    printBeautifiedArray(startGrid)
    print("***********************")

    startGrid = lifeGrid