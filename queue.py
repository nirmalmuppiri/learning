#Implement a basic queue with the following methods:
#enqueue(), dequeue(), is_empty(), peek().

#last time: 01:33:73

class Queue:
    def __init__(self):
        self.a = []

    def is_empty(self):
        if len(self.a) !=0:
            return False
        return True

    def peek(self):
        if self.is_empty():
            return []
        return self.a[0]

    def dequeue(self):
        if self.is_empty():
            return []
        return self.a.pop(0)

    def enqueue(self,item):
        return self.a.append(item)

if __name__=='__main__':
    #Usecases:
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.peek()) #Should return 1
    q.dequeue()
    q.dequeue()
    print(q.peek()) #should return 3
    q.dequeue()
    print(q.peek()) #No error