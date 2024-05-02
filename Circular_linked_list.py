class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def display(self):
        if self.is_empty():
            print("Circular linked list is empty.")
        else:
            current = self.head
            while True:
                print(current.data, end=" -> ")
                current = current.next
                if current == self.head:
                    break
            print()

# Example Usage:
circular_linked_list = CircularLinkedList()
circular_linked_list.append(1)
circular_linked_list.append(2)
circular_linked_list.append(3)
circular_linked_list.append(4)

print("Circular Linked List:")
circular_linked_list.display()
