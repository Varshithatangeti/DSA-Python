'creation of node'
class node:
    def __init__(self,data):    
        self.data=data
        self.next=None
'creation of linked list'
class SLL:
    def __init__(self):
        self.head=None
'creating object for linked list'
L=SLL()

'adding the data to the linked list'
n1=node(20)

'giving the head is n1 node'
L.head=n1

n2=node(30)

'assigning the node2 as the address of n1'
n1.next=n2
n3=node(50)
n2.next=n3

# 'creating the node in the begining of the linked list'
# new_node=node(60)

# 'here giving the address for the new node as n1 means L.head'
# new_node.next=L.head

# 'so now the head of the new linked list the new node'
# L.head=new_node

new_end = node(90)       # create new node
temp = L.head

while temp.next:         # loop until the last node
    temp = temp.next

temp.next = new_end      # attach new node at end


temp=L.head
if temp is None:
    print("Empty")
while temp:
    print(temp.data,end="->")
    temp=temp.next