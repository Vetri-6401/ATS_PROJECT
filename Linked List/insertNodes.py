#create d singly Linked List
#1.create Nodes
#2.create Linked Lists
#3.add Nodes to the Linked List
#4.print(Linked List)
class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList():
    def __init__(self):
        self.head=None   # initialize head as None initially

    def insert(self,Newnode):
        
        #head==>vetri-->None
        if self.head is None:
            self.head=Newnode # chack if the head node is empty if yes make the new node as head Node
        else:
            #head=>vetri-->Ben-->None || Vetri--> Veeravel not we want
            #Here we need to break the pointer Vel to None and mnake it pointer to veeravel so we need to traverse whole linked list
            '''self.head.next=Newnode ''' # Not and ideal way next means location not an element/data
            LastNode=self.head
            while True:
                if LastNode.next is None: #Vel.next is None 
                    break
                LastNode=LastNode.next #head-->vetri-->Vel not None---> so assigning Last Node == Vel-->None
            LastNode.next=Newnode # After the breaking the Loop

    def printnode(self):
        #--head=>Vetri--->Vel--->Veeravel-->
        currentnode=self.head
        while True:
            if currentnode is None:
                break
            print(currentnode.data)
            currentnode=currentnode.next


#Node=> data,Next
firstNode=Node("vetri")
#firstNode.data=>Vetri , firstNode.Next=>None
# print(firstNode.data)
linkedlist=LinkedList()
#insert a firstNode
linkedlist.insert(firstNode)
#Second Node
SecondNode=Node("vel")
linkedlist.insert(SecondNode)
ThirdNode=Node("veeravel")
linkedlist.insert(ThirdNode)
linkedlist.printnode()
