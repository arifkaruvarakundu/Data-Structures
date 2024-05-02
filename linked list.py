class Node:
    def __init__(self,data):
        self.data=data 
        self.ref=None
# -------------------------------------------------------------------------------------#
class LinkedlIst:
    def __init__(self):
        self.head=None
    def printLL(self):
        if self.head is None:
            print("Empty linked list")
        else:
            n=self.head
            while(n is not None):
                print(n.data,"--->",end=" ")
                n=n.ref
#--------------------------------------------------------------------------------------#
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
#--------------------------------------------------------------------------------------#
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
#--------------------------------------------------------------------------------------#
    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n=n.ref
        if n is None:
            print('element not present in the linked list')
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
#--------------------------------------------------------------------------------------#
    def add_before(self,data,x):
        if self.head==None:
            print('empty linked list')
            return
        if self.head.data==x:
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref
        if n.ref is None:
            print("Node not present in the linkedlist")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
#----------------------------------------------------------------------------------------#
    def delete_by_value(self,x):
        if self.head is None:
            print('empty linkedlist')
            return
        if self.head==x:
            self.head=self.head.ref
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref
        if n.ref is None:
            print('node is not present in the linked list')
        else:
             n.ref=n.ref.ref
#----------------------------------------------------------------------------------------#
LL1=LinkedlIst()  
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_after(500,20)
LL1.add_before(300,20)
LL1.delete_by_value(20)
LL1.add_end(100)
LL1.add_begin(30)
LL1.printLL()

