#time: 01:14:93

class InsertionSort:
    def __init__(self, a):
        self.a = a

    def sort(self):
        for p2 in range(1, len(self.a)):
            item = self.a[p2]
            p1 = p2 - 1

            while p1 >= 0 and item < self.a[p1]:
                self.a[p2] = self.a[p1]
                p1 -=1

            self.a[p1 + 1] = item


if __name__ == '__main__':
    array = [5,4,2,3]
    x = InsertionSort(array)
    x.sort()
    print(array)
