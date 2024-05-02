class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur = cur.children[c]

        cur.endofword = True

    def search(self,word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endofword
    
    def startswith(self,prefix):
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
    
    def print_trie(self, node=None, prefix=""):
            if node is None:
                node = self.root  

            if node.endofword:
                print(prefix)

            for char, child in node.children.items():
                self.print_trie(child, prefix + char)

# Example usage:
trie = Trie()
words = ["apple", "app", "apricot", "banana"]
for word in words:
    trie.insert(word)

val=trie.search('app')
print(val)