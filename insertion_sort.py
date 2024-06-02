#time: 01:40:00

class InsertionSort:
    def __init__(self, a):
        self.a = a

    def sort(self):
        for i in range(1, len(self.a)):
            item = self.a[i]
            j = i -1
            while j>=0 and item < self.a[j]:
                self.a[j+1] = self.a[j]
                j -=1

            self.a[j+1] = item

if __name__ == '__main__':
    array = [5,4,2,3]
    x = InsertionSort(array)
    x.sort()
    print(array)
