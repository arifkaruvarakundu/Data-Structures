class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    def search(self, data):
        if self.key == data:
            print("Node is found")
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present in tree")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present in tree")

    def preorder(self):
        print(self.key, end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def Inorder(self):
        if self.lchild:
            self.lchild.Inorder()
        print(self.key, end=" ")
        if self.rchild:
            self.rchild.Inorder()

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key, end=" ")

    def findmin(self, node):
        current = node
        while current.lchild:
            current = current.lchild
        return current

    def deleteNode(self, root, data):
        if not root:
            return root

        elif data < root.key:
            root.lchild = self.deleteNode(root.lchild, data)

        elif data > root.key:
            root.rchild = self.deleteNode(root.rchild, data)

        else:
            # leaf
            if not root.lchild and not root.rchild:
                root = None

            # 1 child
            elif not root.lchild:
                root = root.rchild

            elif not root.rchild:
                root = root.lchild

            else:
                min_right_subtree = self.findmin(root.rchild)
                root.key = min_right_subtree.key
                root.rchild = self.deleteNode(root.rchild, min_right_subtree.key)

        return root


root = BST(10)

lst = [6, 3, 1, 6, 98, 3, 7]

for item in lst:
    root.insert(item)

print("Inorder")
root.Inorder()

print("\nPreorder")
root.preorder()

print("\nPostorder")
root.postorder()

root.deleteNode(root, 3)
print("\nAfter deleting 3")
root.Inorder()
