class Node:
    def __init__(self,key):
        self.data=key
        self.next=None
class LinkedList:
    def __init__(self):
        self.start=Node(None)
    def listPrint(self):
        print("the element in the linked list ;",end=" ")
        temp=self.start
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.next
    def insertBegin(self,newdata):
        newnode=Node(newdata)
        if (self.start==None):
            self.start=newnode
        else:
            newnode.next=self.start
            self.start=newnode
def menu():
    print("\n----Menu----\n")
    print("1.creapte a single linked list")
    print("2. insert at beginning")
    print("11. for exit")
    opt=int(input("enter a valid menu data for choice "))
    return opt
if __name__=='__main__':
    list1=LinkedList()
    i=1
    while (i>0 and i<=10):
        i=menu()
        if i==1:
         x=input("enter data to create firs nde:")
         list1.start=Node(x)
         list1.listPrint()
        elif(i==2):
            x=input("enter data to create node")
            list1.insertBegin(x)
            list1.listPrint()
        else:
            print(end="")