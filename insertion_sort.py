#time: 02:22:08

class InsertionSort:
    def __init__(self, array):
        self.arr = array

    def sort(self):
        for p2 in range(1, len(self.arr)):
            item = self.arr[p2]
            p1 = p2 - 1

            while p1 > 0 and item < self.arr[p1]:
                self.arr[p2] = self.arr[p1]
                p1 -= 1

            self.arr[p1 + 1] = item


if __name__ == '__main__':
    array = [5,4,2,3,6]
    x = InsertionSort(array)
    x.sort()
    print(array)
