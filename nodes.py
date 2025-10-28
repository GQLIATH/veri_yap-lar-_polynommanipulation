class Node:
    def __init__(self, key):
        self.data = key
        self.next = None


class LinkedList:
    def __init__(self):
        self.start = None

    def listPrint(self):
        print("Elements in the linked list:", end=" ")
        temp = self.start
        if temp is None:
            print("List is empty")
        else:
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next
            print()

    def insertBegin(self, newdata):
        newnode = Node(newdata)
        newnode.next = self.start
        self.start = newnode

    def inserEnd(self, newdata):
        newnode = Node(newdata)
        if self.start is None:
            self.start = newnode
        else:
            temp = self.start
            while temp.next:
                temp = temp.next
            temp.next = newnode

    def insertAfter(self, key, newdata):
        temp = self.start
        while temp is not None and temp.data != key:
            temp = temp.next
        if temp is None:
            print(f"{key} not found in the list.")
        else:
            newnode = Node(newdata)
            newnode.next = temp.next
            temp.next = newnode


def menu():
    print("\n---- Menu ----")
    print("1. Create a single linked list (first node)")
    print("2. Insert at beginning")
    print("3. Insert at end")
    print("4. Insert after a given data")
    print("11. Exit")
    opt = int(input("Enter your choice: "))
    return opt


if __name__ == '__main__':
    list1 = LinkedList()
    i = 1
    while 1 <= i <= 10:
        i = menu()
        if i == 1:
            x = input("Enter data for the first node: ")
            list1.start = Node(x)
            list1.listPrint()
        elif i == 2:
            x = input("Enter data to insert at beginning: ")
            list1.insertBegin(x)
            list1.listPrint()
        elif i == 3:
            x = input("Enter data to insert at end: ")
            list1.inserEnd(x)
            list1.listPrint()
        elif i == 4:
            y = input("Enter data after which new node is to be inserted: ")
            x = input("Enter data for new node: ")
            list1.insertAfter(y, x)
            list1.listPrint()
        elif i == 11:
            print("Exiting program...")
            break
        else:
            print("Invalid choice, please try again.")
