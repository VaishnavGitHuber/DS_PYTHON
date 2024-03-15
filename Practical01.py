class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def display(self):
        if self.head is None:
            print("Linked List is empty")

        temp = self.head
        while temp:
            print(temp.data, "--> ",end = "")
            temp = temp.next
        print("NULL")

    def insertElement(self):
        newdata = int(input("Enter the data: "))
        newNode = Node(newdata)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode



LL = SinglyLinkedList()
LL.insertElement()
LL.insertElement()
LL.insertElement()
print(LL.display())