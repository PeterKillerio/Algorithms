class Node:
    def __init__(self, value=None, next=None):
        self._value = value
        self._next = next

class LinkedList:
    def __init__(self):
        self.current = None
        self.next = None

    def print_values(self):
        curr = self.current
        while(curr != None):
            print(curr._value, " ", end='')
            if(curr._next != None):
                curr = curr._next
            else:
                print()
                return -1

    def insert_value(self, value):
        if(self.current == None):
            new_node = Node(value)
            self.current = new_node
        else:
            new_node = Node(value, self.current)
            self.current = new_node



    def insert_after(self, after, value):
        curr = self.current
        while (curr != None):
            if(curr._value == after):
                new_node = Node(value, curr._next)
                curr._next = new_node
                print("found")
            if (curr._next != None):
                curr = curr._next
            else:
                new_node = Node(value)
                curr = new_node
                return -1

ll = LinkedList()

ll.print_values()
ll.insert_value(5)
ll.print_values()
ll.insert_value(6)
ll.print_values()
ll.insert_value(7)
ll.print_values()
ll.insert_value(8)
ll.print_values()
ll.insert_value(9)
ll.print_values()
ll.insert_after(7, 11)
ll.print_values()

