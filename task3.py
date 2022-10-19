'''

О це трохи подивився, але я спробую потім щось схоже зробити

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

class Queue:

    def __init__(self):
        self.front = self.back = None

    def isEmpty(self):
        return self.front == None

    def append(self, item):
        temp = Node(item)

        if self.back == None:
            self.front = self.back = temp
            return
        self.back.next = temp
        self.back = temp

    def pop(self):
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next

        if (self.front == None):
            self.back = None

if __name__ == '__main__':
    q = Queue()
    q.append(1)
    q.append(2)
    q.append(3)
    q.pop()
    q.append(5)
    q.append(6)
    q.append(7)
    q.pop()
    print("Queue Front " + str(q.front.data))
    print("Queue back " + str(q.back.data))