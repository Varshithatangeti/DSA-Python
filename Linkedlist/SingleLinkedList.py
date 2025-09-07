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

'creating the node in the begining of the linked list'
new_node=node(60)

'here giving the address for the new node as n1 means L.head'
new_node.next=L.head

'so now the head of the new linked list the new node'
L.head=new_node

new_end = node(90)       # create new node
temp = L.head

while temp.next:         # loop until the last node
    temp = temp.next

temp.next = new_end      # attach new node at end

'creating the node in specific position'
position=1
data=100
np=node(data)
temp=L.head

'Loop to traverse the linked list until we reach the node'
'just before the desired position (position-1)'
for i in range(position - 1):
    temp = temp.next  

# Assign the given data value to the new node (np)
np.data = data  

# Link the new node's 'next' pointer to the current node's next
# This preserves the rest of the list after the insertion point
np.next = temp.next  

# Finally, link the previous node (temp) to the new node (np)
# This completes the insertion at the desired position
temp.next = np  

'deleting at the begining'
temp=L.head
L.head=temp.next
temp.next=None



'deleting at the end'
temp=L.head.next
previous=L.head
while temp.next is not None:
    temp=temp.next
    previous=previous.next
previous.next=None



temp=L.head
if temp is None:
    print("Empty")
while temp:
    print(temp.data,end="->")
    temp=temp.next






























# 'class'

# class node:
#     def __init__(self,value=0,next_node=None):
#         self.data=value
#         self.next=next_node
# p1=node(10,None)
# p2=node(20)
# p3=node()
# print(p1.data,end="->")
# print(p2.data,end="->")
# print(p3.data)
