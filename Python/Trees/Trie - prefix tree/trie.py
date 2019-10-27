class Node:
    def __init__(self, value = None):
        self.value = value
        self.Nodes = []

    IsWord = False

    def InsertWord(self, Word):
        found = False
        index = 0
        for node in self.Nodes:
            if (Word[0] == node.value):
                index = self.Nodes.index(node)
                found = True
                break
        if(len(Word) > 1):
            if(found):
                self.Nodes[index].InsertWord(Word[1:])
            else:
                newNode = Node(Word[0])
                self.Nodes.append(newNode)
                newNode.InsertWord(Word[1:])
        else:
            if(found):
                if(self.Nodes[index].IsWord == False):
                    self.Nodes[index].IsWord = True
            else:
                newNode = Node(Word[0])
                self.Nodes.append(newNode)
                newNode.IsWord = True

    def IsThereThisWord(self, Word):

        found = False
        index = 0
        for node in self.Nodes:

            if (Word[0] == node.value):
                index = self.Nodes.index(node)
                found = True
                break
        if(len(Word) > 1):
            if(found):
                return self.Nodes[index].IsThereThisWord(Word[1:])
            else:
                return 0
        else:
            if(found):
                if(self.Nodes[index].IsWord):
                    return 1
                else:
                    return 0
            else:
                return 0
class NodeList:
    def __init__(self):
        self.root = Node()

    def InsertWord(self, Word):
        found = False
        index = 0
        for node in self.root.Nodes:

            if (Word[0] == node.value):
                index = self.root.Nodes.index(node)
                found = True
                break
        if(len(Word) > 1):
            if(found):
                self.root.Nodes[index].InsertWord(Word[1:])
            else:
                newNode = Node(Word[0])
                self.root.Nodes.append(newNode)
                newNode.InsertWord(Word[1:])
        else:
            if (found):
                if(self.root.IsWord == False):
                    self.root.IsWord = True
            else:

                newNode = Node(Word[0])
                self.root.Nodes.append(newNode)
                newNode.IsWord = True


    def IsThereThisWord(self, Word):
        found = False
        index = 0
        for node in self.root.Nodes:
            if (Word[0] == node.value):
                index = self.root.Nodes.index(node)
                found = True
                break
        if(len(Word) > 1):
            if(found):
                return self.root.Nodes[index].IsThereThisWord(Word[1:])
            else:
                return 0
        else:
            if(found):
                if(self.root.IsWord):
                    return 1
                else:
                    return 0
            else:
                return 0

    def PrintAllNodeValues(self):
        print(len(self.root.Nodes))
        #for node in self.root.Nodes:
         #   print(node.value)


# TEST

testList = NodeList()
print(testList.IsThereThisWord("car"))
testList.InsertWord("car")
print(testList.IsThereThisWord("car"))
testList.InsertWord("bus")
testList.InsertWord("cars")
print(testList.IsThereThisWord("carss"))
testList.InsertWord("carwash")
print(testList.IsThereThisWord("carwasher"))
testList.InsertWord("carwasher")
print(testList.IsThereThisWord("carwasher"))