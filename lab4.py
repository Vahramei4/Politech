class Queue:
    def __init__(self, size):
        self.items = [None] * size
        self.head = 0
        self.tail = 0
        
    def enqueue(self, element):
        if (self.tail + 1 < self.get_size()):
            self.items[self.tail] = element
            self.tail += 1
        else:
            self.tail = 0
            self.items[self.get_size() - 1] = element

    def dequeue(self):
        if (self.head + 1 < self.get_size()):
            value = self.items[self.head]
            self.items[self.head] = None
            self.head += 1
            return value
        else:
            value = self.items[self.head]
            self.items[self.head] = None
            self.head = 0
            return value

    def get_size(self):
        return len(self.items)


def maxElementInversion(array):
    maxIndex = array.index(max(array))
    array[maxIndex] = -array[maxIndex]

def insertArrayIntoQueue(array, queue):
    for element in array:
        maxElement = max(array)
        queue.enqueue(maxElement)
        maxElementInversion(array)

def extractElementsFromQueue(queue):
    while True:
        extracted = queue.dequeue()
        if (extracted == None):
            break

        print(extracted)

array = [70, 20, 90, 40, 100, 60, 10, 80, 30, 50]
queue = Queue(10)

insertArrayIntoQueue(array, queue)
extractElementsFromQueue(queue)


    
