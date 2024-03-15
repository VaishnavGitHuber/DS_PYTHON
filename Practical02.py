class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # displaying the elements in the Linked List
    def display(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data , "-> ", end=" ")
                temp = temp.next
            print("NULL")

    # Inserting element at the last
    def addLast(self):
        newData = int(input("Enter the data: "))
        newNode = Node(newData)

        if self.head is None:
            self.head = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
    # Inserting element at the First
    def addFirst(self):
        if self.head is None:
            self.addLast()
            return
        else:
            newData = int(input("Enter the data: "))
            newNode = Node(newData)
            newNode.next = self.head
            self.head = newNode

LL = SinglyLinkedList()
LL.addFirst()
LL.addFirst()
print(LL.display())
