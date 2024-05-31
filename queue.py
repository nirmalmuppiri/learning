#Implement a basic queue with the following methods:
#enqueue(), dequeue(), is_empty(), peek().

#last time: 04:12:29

class Queue:
    def __init__(self):
        self.array = []

    def enqueue(self, item):
        return self.array.append(item)

    def dequeue(self):
        return self.array.pop(0)

    def is_empty(self):
        if len(self.array) !=0:
            return False
        return True

    def peek(self):
        if self.is_empty():
            return []
        return self.array[0]

if __name__=='__main__':
    #Usecases:
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.peek()) #Should return 1
    q.dequeue()
    q.dequeue()
    print(q.peek()) #should return 1
    q.dequeue()
    print(q.peek()) #No error