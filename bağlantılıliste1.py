#düğüm sınıfı
class  Node:
    def __init__(self,key):
        self.data=key
        self.next=None
#tekli bağlantılı liste
class LinkedList:
    def __init__(self):
        self.start=Node(None) #bağlantılı listenin başlangıç düğümünü işaret eder

if __name__=='__main__':
    list1=LinkedList() #list isimli bir nesne oluşturulyor 
    ans='y'
    while (ans=='Y' or ans=='y'):
        x=input('enter data to create the node')#klavyeden girilen veri x değişkeninde 
        newNode=Node(x) #klavyeden bir nesne var data adeğişkeninde kullanıcıdan alınan var
        if (list1.start==None):#list1
             list1.start=newNode
        
        else:
            temp=list1.start
            while(temp.next !=None):
                temp=temp.next
            temp.next=newNode
        ans=input("do you want to add more ( y | Y )")
        print("the element in the linked list array:",end=" ")
        printval=list1.start
        while printval is not None:
            print(printval.data,end=" ")
            printval=printval.next
        print ("\n")
 