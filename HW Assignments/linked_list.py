# Isaiah Lugo
# Week 8 Assignment - Linked Lists Implentation


# import modules
import sys

# implement a Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# implement a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # insert a node at the beginning of the linked list
    def insertAtBeginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # delete a node at the beginning of the linked list
    def deleteAtBeginning(self):
        if self.head is not None:
            self.head = self.head.next

    # insert a node at the end of the linked list
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # delete a node at the end of the linked list
    def deleteAtEnd(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None

    # insert a node at the given index in the linked list
    def insertAtIndex(self, data, index):
        if index < 0:
            return
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(index - 1):
            if current is None:
                return
            current = current.next
        new_node.next = current.next
        current.next = new_node

    # delete a node at the given index in the linked list
    def deleteAtIndex(self, index):
        if index < 0 or self.head is None:
            return
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(index - 1):
            if current is None or current.next is None:
                return
            current = current.next
        if current.next is None:
            return
        current.next = current.next.next

    # traverse the linked list and print the data from each node
    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def main(argv):
    # create a new linked list object
    linked_list = LinkedList()

    # Insert nodes at the beginning
    linked_list.insertAtBeginning('working')
    linked_list.insertAtBeginning('is')
    linked_list.insertAtBeginning('list')
    linked_list.insertAtBeginning('the')
    linked_list.insertAtBeginning('now')
    linked_list.insertAtBeginning('maybe')

    # Insert a node at the end of the list
    linked_list.insertAtEnd('correctly')

    # Insert a node at index 3
    linked_list.insertAtIndex('linked', 3)

    # Delete the first node in the list
    linked_list.deleteAtBeginning()

    # Delete the last node in the list
    linked_list.deleteAtEnd()

    # Delete the node at index 2
    linked_list.deleteAtIndex(2)

    # Print the current list
    linked_list.printList()

# program will begin here
if __name__ == '__main__':
    main(sys.argv)
