class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
L=SLL()
n1=node(20)
L.head=n1
n2=node(30)
n1.next=n2
n3=node(50)
n2.next=n3

temp=L.head
if temp is None:
    print("Empty")
while temp:
    print(temp.data,end="->")
    temp=temp.next