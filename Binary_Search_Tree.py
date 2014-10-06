class BinaryTree:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None
    
    def getLeftChild(self):
        return self.left
    
    def getRightChild(self):
        return self.right
    
    def setRootVal(self, val):
        self.root = val
    
    def getRootVal(self):
        return self.root
    
    def insertLeft(self, val):
        if self.left != None:
            if val < self.left:
                self.left.insertLeft(val)
            else:
                self.left.insertRight(val)
        else:
            self.left = val
    
    def insertRight(self, val):
        if self.right != None:
            self.right.insertRight(val)
        else:
            self.right = val

if __name__ == "__main__":
    Tree = BinaryTree(5)
    leftChild = Tree.getLeftChild()
    print(leftChild)
    Tree.insertLeft(4)
    leftChild = Tree.getLeftChild()
    print(leftChild)
    Tree.insertLeft(3)
    
