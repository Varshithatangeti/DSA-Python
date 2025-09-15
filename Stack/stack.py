# MAX_SIZE = 3  # You can change this value as needed

# def is_empty(stack):
#     return len(stack) == 0

# def is_full(stack):
#     return len(stack) == MAX_SIZE
# from collections import deque
# stack=deque()
# stack=[]
# stack.append("Hello")
# stack.append("Varshitha")
# stack.append("How are you")
# print(stack)
# print(stack.pop())
# print(stack)


# from queue import LifoQueue
# max_size=2
# stack=LifoQueue()
# stack.put("varshitha")
# stack.put("how are youuuuu")
# print(stack.qsize())
# print(stack.full())
# print(stack.empty())
'implementing the stack using list'
# class stack:
#     def __init__(self):
#         self.stack = []
#     def push(self, data):
#         self.stack.append(data)
#     def is_Empty(self):
#         return len(self.stack) == 0
#     def Pop(self):
#         if self.is_Empty():
#             return "stack is empty"
#         else:
#             return self.stack.pop()
#     def peek(self):
#         if self.is_Empty():
#             return "stack is empty"
#         return self.stack[-1]

# Stack = stack()
# Stack.push(1)
# Stack.push(2)
# Stack.push(3)
# Stack.Pop()
# print(Stack.peek())

'implementing using linkedlist'
# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Stack:
#     def __init__(self):
#         self.head=None
#     def push(self,data):
#         newNode=node(data)
#         if self.head==None:
#             self.head=newNode
#         else:
#             newNode.next=self.head
#             self.head=newNode
#     def pop(self):
#         if self.head==None:
#             print("stack is empty")
#         else:
#             self.head=self.head.next
#     def peek(self):
#         if self.head==None:
#             return "empty"
#         else:
#             return self.head.data
# stack=Stack()
# stack.push(1)
# stack.push(2)
# stack.pop()
# print(stack.peek())


