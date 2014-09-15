class Node:
    def __init__(self, Data):
        self.Data = Data
        self.NextPointer = None
    
    def getData(self):
        return self.Data
    
    def setData(self, nextdata):
        self.Data = nextdata
    
    def getNextPointer(self):
        return self.NextPointer
    
    def setNextPointer(self, newpointer):
        self.NextPointer = newpointer
        
class Unordered_List:
    def __init__(self):
        self.Head = None
    
    def isEmpty(self):
        return self.Head == None
    
    def add(self, Data):
        temp = Node(data)
        temp.setNextPointer(self.Head)
        self.Head = temp
    
    def getList(self):
        
    
    def length(self):
    
    
    def search(self,Data):
        current = self.Head
        found = False
        while current and not found:
            if (current.getData()) == Data:
                found = True
            else:
                current = current.getNextPointer()
        return found
    
    def remove(self,Data):
        current, previous = self.Head
        
class Ordered_List(Undordered_List()):
    def __init__(self):
        super.__init__()

    def search(self):


    def add(self):




    
