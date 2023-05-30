class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node != None:
            print(current_node.value)
            current_node = current_node.next
my_list = LinkedList()

my_list.add_node(5)
my_list.add_node(10)
my_list.add_node(15)

my_list.print_list()
