# class Node:
#     def __init__(self, data=None, next=None):
#         # Initialize the node with data and a pointer to the next node
#         self.data = data
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         # Initialize the linked list with an empty head
#         self.head = None

#     def insert_at_beginning(self, data):
#         # Insert a new node at the beginning of the list
#         new_node = Node(data, self.head)
#         self.head = new_node

#     def print_list(self):
#         # Print the contents of the linked list
#         if self.head is None:
#             print("Linked list is empty")
#             return
#         itr = self.head
#         llstr = ""
#         while itr:
#             llstr += str(itr.data) + " --> "  # Append the current node's data
#             itr = itr.next  # Move to the next node
#         llstr += "None"  # Indicate the end of the list
#         print(llstr)

#     def insert_at_end(self, data):
#         # Insert a new node at the end of the list
#         new_node = Node(data)
#         if self.head is None:  # If the list is empty, set head to the new node
#             self.head = new_node
#             return
#         itr = self.head
#         while itr.next:  # Traverse to the last node
#             itr = itr.next
#         itr.next = new_node  # Link the last node to the new node

#     def insert_values(self, data_list):
#         # Insert multiple values into the linked list
#         self.head = None  # Clear the list
#         for data in data_list:
#             self.insert_at_end(data)  # Insert each data value at the end

# # Example usage
# if __name__ == "__main__":
#     ll = LinkedList()  # Create a new linked list
#     ll.insert_at_beginning(5)  # Insert 5 at the beginning
#     ll.insert_at_end(79)  # Insert 79 at the end
#     ll.print_list()  # Print the linked list
class Node:
    def __init__(self, data=None, next=None):
        # Initialize the node with data and a pointer to the next node
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        # Initialize the linked list with an empty head
        self.head = None

    def print(self):
        # Print the contents of the linked list
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def get_length(self):
        # Return the number of nodes in the linked list
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_beginning(self, data):
        # Insert a new node with the given data at the beginning of the list
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        # Insert a new node with the specified data at the end of the list
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_at(self, index, data):
        # Insert a new node at the specified index in the list
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def remove_at(self, index):
        # Remove a node at the specified index
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_values(self, data_list):
        # Clear the current list and insert multiple values from a list
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.insert_at(1, "blueberry")
    ll.remove_at(2)
    ll.print()

    ll.insert_values([45, 7, 12, 567, 99])
    ll.insert_at_end(67)
    ll.print()

