class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=Node(1)
root.left=Node(2)
root.left.left=Node(4)
root.left.right=Node(5)


root.right=Node(3)
root.right.right=Node(6)


def IoT(root):
    if root==None:
        return
    
    IoT(root.left)
    IoT(root.right)
    print(root.data,end=" ")

IoT(root)
'''pre-order traversal[root,left,right]'''
# def pre_o_t(root):
#     if root==None:
#         return 
#     print(root.data,end=" ")
#     pre_o_t(root.left)
#     pre_o_t(root.right)
# pre_o_t(root)

'''post-order traversal[left,right,root]'''
# def pre_o_t(root):
#     if root==None:
#         return 
#
#     pre_o_t(root.left)
#     pre_o_t(root.right)
#     print(root.data,end=" ")
# pre_o_t(root)