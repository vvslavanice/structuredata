'''

Task 2

'''



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def set_next(self, new_next):
        self.next = new_next

class Stack:

    def __init__(self):
        self.head = None

    def isempty(self):
        if self.head == None:
            return True
        else:
            return False


    def pushitem(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    def pop(self):
        if self.isempty():
            return None
        else:
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data

    def choose(self):
        if self.isempty():
            return None
        else:
            return self.head.data

    def show(self):
        iternode = self.head
        if self.isempty():
            print("Stack Empty")
        else:
            while (iternode != None):
                print(iternode.data)
                iternode = iternode.next
            return


NewStack = Stack()

NewStack.pushitem(1)
NewStack.pushitem(2)
NewStack.pushitem(3)
NewStack.show()
print("Fifo element is ", NewStack.choose())

NewStack.pop()
NewStack.pop()
NewStack.show()
print("Fifo element is ", NewStack.choose())