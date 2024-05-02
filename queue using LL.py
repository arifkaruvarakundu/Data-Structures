class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear  = None

    def enqueue(self,data):
        if self.front is None:  # case 1 if queue is empty.
            print("Queue is empty")
            new = Node(data)
            self.front = new
            self.rear = new
        else:                  #case 2 if queue is not empty.
            new = Node(data)
            self.rear.next = new
            self.rear= new

    def dequeue(self):
        if self.front is None: #case1 queue is empty.
            print("queue is empty")
        elif self.front==self.rear: # case 2  queue have only one element.
            print("poped data :",self.front.data)
            self.front == None

        else:                # case 3 queue has more than one element.
            temp = self.front
            print("poped data:",self.front.data)
            self.front = temp.next
            temp = None

    def display(self):
        if self.front is None: # case 1 queue is empty.
            print("Queue is empty")
        else:
            temp = self.front
            while temp:  # case 2 queue has one or more element.
                print(temp.data)
                temp = temp.next
            print("front:",self.front.data)
            print("rear:", self.rear.data)


queue_1 = Queue()
queue_1.enqueue(10)
queue_1.enqueue(20)
queue_1.enqueue(30)
queue_1.enqueue(40)
queue_1.enqueue(50)
queue_1.enqueue(60)
queue_1.enqueue(70)
queue_1.enqueue(80)
queue_1.enqueue(90)
queue_1.enqueue(100)

queue_1.dequeue()
queue_1.dequeue()

queue_1.display()


