import copy

# This is my implementation of hash table with open adressing for linear probing, quadratic and double hashing
# this implementation also contains automatic resizing which can be turned on in the argument of the hash table
# or changed manualy in the table object later on
# In this implementation if you try to resize the table to a smaller size, the table and there will be errors
# table will automatically double its size till there will be no errors (no matter if the automatic resizing is
# turned ON of OFF).

class hashTable:
    def __init__(self, size, openAdressing, automaticResizing): # Open adressing 0 - linear, 1 - quadratic, 2 - double hash
        # Automatic resing = True if you want to resize the table automatically if its not possible to insert element
        self.size = size
        self.tableUsed = [False] * size
        self.cellsUsed = 0
        self.table = [0] * size
        self.collisionHandling = openAdressing
        self.automaticResizing = automaticResizing


    def openAdressingLinear(self, value, action): # 0 - insert, 1 - find, 2 - delete
        position = self.tablePosition(value)
        collisionCount = 0
        while collisionCount <= self.size:
            position = self.checkPosition(position)
            if self.tableUsed[position]:
                if self.table[position] == value:
                    if action == 0:
                        return True
                    elif action == 1:
                        return position
                    elif action == 2:
                        self.table[position] = 0
                        return True
                    else:
                        return False
                else:
                    # Collision
                    position += 1
                    collisionCount += 1
            else:
                if action == 0:
                    self.table[position] = value
                    self.tableUsed[position] = True
                    self.cellsUsed += 1
                    return True
                elif action == 1:
                    return True
                elif action == 2:
                    return False
                else:
                    return False
        if self.automaticResizing:
            print(f"Cannot insert elemnt... Resizing to size {self.size*2}.")
            self.resize(self.size*2)
            return self.openAdressingLinear(value, action)
        return False
    def openAdressingQuadratic(self, value, action): # 0 - insert, 1 - find, 2 - delete
        positionOriginal = self.tablePosition(value)
        position = positionOriginal
        collisionCount = 0
        while collisionCount <= self.size:
            position = self.checkPosition(position)
            if self.tableUsed[position]:
                if self.table[position] == value:
                    if action == 0:
                        return True
                    elif action == 1:
                        return position
                    elif action == 2:
                        self.table[position] = 0
                        return True
                    else:
                        return False
                else:
                    # Collision
                    collisionCount += 1
                    position = positionOriginal + (collisionCount**collisionCount)
            else:
                if action == 0:
                    self.table[position] = value
                    self.tableUsed[position] = True
                    self.cellsUsed += 1
                    return True
                elif action == 1:
                    return True
                elif action == 2:
                    return False
                else:
                    return False
        if self.automaticResizing:
            print(f"Cannot insert elemnt... Resizing to size {self.size * 2}.")
            self.resize(self.size * 2)
            return self.openAdressingQuadratic(value, action)
        return False
    def openAdressingDoubleHash(self, value, action): # 0 - insert, 1 - find, 2 - delete
        positionOriginal = self.tablePosition(value)
        position = positionOriginal
        collisionCount = 0
        while collisionCount <= self.size:
            position = self.checkPosition(position)
            if self.tableUsed[position]:
                if self.table[position] == value:
                    if action == 0:
                        return True
                    elif action == 1:
                        return position
                    elif action == 2:
                        self.table[position] = 0
                        return True
                    else:
                        return False
                else:
                    # Collision
                    collisionCount += 1
                    position += self.secondHashPosition(value)
            else:
                if action == 0:
                    self.table[position] = value
                    self.tableUsed[position] = True
                    self.cellsUsed += 1
                    return True
                elif action == 1:
                    return True
                elif action == 2:
                    return False
                else:
                    return False
        if self.automaticResizing:
            print(f"Cannot insert elemnt... Resizing to size {self.size*2}.")
            self.resize(self.size*2)
            return self.openAdressingDoubleHash(value, action)
        return False
    def secondHashFunction(self, value):
        # There you can implement your second hash function for open adressing double hash
        return hash(value)
    def secondHashPosition(self, value):
        return (self.secondHashFunction(value) % self.size) - 1

    def cleanHashTable(self):
        self.tableUsed = [False] * self.size
        self.table = [0] * self.size
        return True
    def resize(self, newSize):
        totalErrors = 0
        if newSize < self.size:
            print("You are downsizing existing hash table, you might lose your data.")
        elif newSize == self.size:
            return True

        # Temp copying old data
        oldTempTable = copy.deepcopy(self.table)

        while True:
            self.size = newSize
            self.table = [0] * self.size
            self.tableUsed = [False] * self.size

            # Copying the data to the new table
            for data in oldTempTable:
                if not self.insert(data):
                    totalErrors += 1

            # Errors are relevant only if user doesnt have automatic resising
            # because if user has resizing enabled, errors correct themselved during inserting
            if not self.automaticResizing:
                if totalErrors == 0:
                    print()
                    print(f"Succefully resized to size: {newSize}.")
                    break
                else:
                    print()
                    print(f"During resizing there occurred {totalErrors} errors.")
                    print(f"Repeating resizing for size: {self.size*2}.")
                    totalErrors = 0
                    newSize *= 2
            else:
                break
        return True

    def tablePosition(self, value):
        return (self.hashFunction(value) % self.size) - 1
    def hashFunction(self, value):
        # There you can implement you first hash function for open adressing
        return hash(value)
    def checkPosition(self, position):
        if position < len(self.table) and position >= 0:
            return position
        else:
            return (position % self.size) - 1
    def insert(self, value):
        if self.collisionHandling == 0:
            return self.openAdressingLinear(value, 0)
        elif self.collisionHandling == 1:
            return self.openAdressingQuadratic(value, 0)
        elif self.collisionHandling == 2:
            return self.openAdressingDoubleHash(value, 0)
    def findElement(self, value):
        if self.collisionHandling == 0:
            return self.openAdressingLinear(value, 1)
        elif self.collisionHandling == 1:
            return self.openAdressingQuadratic(value, 1)
        elif self.collisionHandling == 2:
            return self.openAdressingDoubleHash(value, 1)
    def deleteElement(self, value):
        if self.collisionHandling == 0:
            return self.openAdressingLinear(value, 2)
        elif self.collisionHandling == 1:
            return self.openAdressingQuadratic(value, 2)
        elif self.collisionHandling == 2:
            return self.openAdressingDoubleHash(value, 2)


hT = hashTable(20, 2, True)

for i in range(10):
    print(hT.insert((i+1)*3))
    print(hT.table)

print()
print("Finding element 52...")
print(hT.findElement(52))
print("Deleting element 100...")
print(hT.deleteElement(100))
print()
print(hT.table)
print()
print("Resing...")
print(hT.resize(30))
print()
print(hT.table)
print()
print("Downsizing...")
print(hT.resize(5))
print()
print(hT.table)
