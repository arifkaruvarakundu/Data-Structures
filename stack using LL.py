class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.top = None
    
    def push(self,data):
        if self.top is None:
            print("empty stack going to push")
            new = Node(data)
            self.top = new
        else:
            new = Node(data)
            new.next = self.top
            self.top = new

    def pop(self):
        if self.top is None:
            print("empty stack")
        elif self.top.next is None:
            print("poped element",self.top.data)
            self.top = None
        else:
            temp = self.top
            print("poped element is :",self.top.data)
            self.top = temp.next
            temp = None

    def display(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Element of stack are :")
            temp = self.top 
            while temp:
                print(temp.data)
                temp= temp.next

            print('Top of the stack is :',self.top.data)

        



stack_1 = stack()
stack_1.push(10)
stack_1.push(20)
stack_1.push(30)
stack_1.push(40) 
stack_1.push(50)
stack_1.push(60)
stack_1.push(70)
stack_1.pop()
stack_1.pop()
stack_1.display()





    