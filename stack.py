#Implement a basic stack with the methods pop(), push(), is_empty(), peek().
#02:14:43

class Stack:
    def __init__(self):
        self.arr = []

    def push(self, item):
        return self.arr.append(item)

    def pop(self):
        if self.is_empty():
            return []
        return self.arr.pop()

    def is_empty(self):
        if len(self.arr) !=0:
            return False
        return True

    def peek(self):
        if self.is_empty():
            return []
        return self.arr[-1]

if __name__=='__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(f"Top item (peek): {s.peek()}") # should be 3.
    s.pop()
    s.pop()
    print(f"Top item (peek): {s.peek()}") # should be 1.
    s.pop()
    s.pop()
