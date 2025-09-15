'implementing the queue using the list'

# class Queue:
#     def __init__(self):
#         self.queue=[]
#     def enqueue(self,data):
#         return self.queue.append(data)
#     def is_empty(self):
#         return len(self.queue)==0
#     def dequeue(self):
#         if self.is_empty():
#             print("queue is empty")
#             return
#         return self.queue.pop(0)
#     def peek(self):
#         if self.is_empty():
#             print("the queue is empty")
#             return
#         return self.queue[0]
# Q=Queue()
# Q.enqueue(1)
# Q.enqueue(2)
# Q.enqueue(3)
# Q.dequeue()
# print(Q.peek())

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def enqueue(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
    def isEmpty(self):
        return self.head==None
    def dequeue(self):
        if self.isEmpty():
            print("No elements Exist for dequeue")
        else:
            self.head=self.head.next
    def peek(self):
        if self.isEmpty():
            print("No elements Exist")
        else:
            return self.head.data
q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.dequeue()
q.dequeue()

print(q.peek())

        