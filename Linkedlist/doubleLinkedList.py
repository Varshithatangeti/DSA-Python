class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DLL:
    def __init__(self):
        self.head=None

L=DLL()
n1=node(10)
L.head=n1
n2=node(20)
n1.next=n2
n2.prev=n1
n3=node(30)
n2.next=n3
n3.prev=n2
n3.next=None
temp=L.head
if L.head is None:
    print("Double linked list is empty")
else:
    while temp:
        print(temp.data,end="->")
        temp=temp.next