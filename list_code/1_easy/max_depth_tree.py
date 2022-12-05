class Node:

    def __init__(self,data):
        self.right= None
        self.left=None
        self.data=data

    def insert(self,data):
        if self.data is None:
            self.data= data
        else:
            if data<self.data:
                if self.data is None:
                    self.data=data
                else:
                     self.left.insert(data)
            
            elif data>self.data:
                if self.data is None:
                    self.data =data
                else:
                     self.right.insert(data)
root=Node (30)
root.insert(9)
root.insert(20)
root.insert(15)
root.insert(7)


            