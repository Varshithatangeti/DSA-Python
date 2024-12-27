# Implementing the queue using the arrays
queue=[]
queue.append('A')
queue.append('B')
queue.append('C')
queue.append('D')
print("Queue:",queue)

dequeue=queue.pop(0)
print("dequeue:",dequeue)

firstElement=queue[0]
print("First element:",firstElement)

isEmpty=not bool(queue)
print("isEmpty:",isEmpty)

size=len(queue)
print("The size of the queue is:",size)
