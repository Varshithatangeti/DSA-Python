# //Implementing the stack using the arrays
stack=[]
stack.append('A')
stack.append('B')
stack.append('C')
stack.append('D')
print("stack",stack)

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