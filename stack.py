# //Implementing the stack using the arrays
stack=[]
stack.append('A')
stack.append('B')
stack.append('C')
stack.append('D')
print("stack",stack)
# this is a comment
# POP
element=stack.pop()
print("Pop: ", element)

# Peek
topElement = stack[-1]
print("Peek: ", topElement)

# isEmpty
isEmpty = not bool(stack)
print("isEmpty: ", isEmpty)

# Size
print("Size: ",len(stack))
# Push:adds a new element on the stack.
# pop:removes and return the top element from the stack
# peek:returns the top element on the stack
# isempty:checks if the stack is empty
# size:finds the number of elements in the stack
