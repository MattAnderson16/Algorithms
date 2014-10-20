import pdb

class BinaryTree:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None

    def __str__(self):
        return str({"Root":self.root,"Left":self.left,"Right":self.right})
    
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
            self.left = BinaryTree(self.left)
            if val < self.left.root:
                self.left.insertLeft(val)
            else:
                self.left.insertRight(val)
        else:
            self.left = val
    
    def insertRight(self, val):
        if self.right != None:
            self.right = BinaryTree(self.right)
            if val < self.right:
                self.right.insertLeft(val)
            else:
                self.right.insertRight(val)
        else:
            self.right = val

if __name__ == "__main__":
    Tree = BinaryTree(5)
    print(Tree)
##    leftChild = Tree.getLeftChild()
##    print(leftChild)
    Tree.insertLeft(4)
##    leftChild = Tree.getLeftChild()
##    print(leftChild)
    pdb.set_trace()
    Tree.insertLeft(3)
##    leftChild = Tree.getLeftChild()
##    print(leftChild)
    print(Tree)
    
