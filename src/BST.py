
class Node:
    def __init__(self, value = None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
  
  #Binary Search
    def find(self, value):
        node=self
        while node:
            if value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
            else:
                return node.value
    def min(self):
        node=self
        while node and node.left:
            node = node.left
        return node
    def max(self):
        node=self
        while node and node.right:
            node = node.right
        return node

    def inorder_traversal(self):
        self.__listOfNodes = []
        self.__inorderTraversal(self)
        print(self.__listOfNodes)

    def __inorderTraversal(self, node):
        if node!=None:
            self.__inorderTraversal(node.left)
            self.__listOfNodes.append(node.value)
            self.__inorderTraversal(node.right)  
    def insert(self, value, node=None, root=True):
        
        if root:
            node = self
        if node is None:
            return Node(value)
        if self.value is None:
            self.value = value
            return self
        
        if value < node.value:
            node.left = self.insert(value, node.left, False)

        elif value > node.value:
            node.right = self.insert(value, node.right, False)
        else:
            #Duplicate value, ignore it
            return node
        return node
    
    
    def minValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while(current.left is not None):
            current = current.left

        return current 
    
    def delete(self, value, node=None, root=True):
        if root:
            node=self
        #best Case
        if node is None:
            return None

        if value < node.value:
            node.left = self.delete(value, node.left, False)
        elif value > node.value:
            node.right = self.delete(value, node.right, False)

        else:
            # Node with only one child or no child
            if node.left is None:
                temp = node.right
                node = None
                return temp
    
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            
            # Node with two children:
            # Get the inorder successor
            # (smallest in the right subtree)
            temp = self.minValueNode(node.right)

            # Copy the inorder successor's
            # content to this node
            node.value = temp.value

             # Delete the inorder successor
            node.right = self.delete(temp.value,node.right, False)
        return node   

               
            






# class Node(object):
#     def __init__(self, data):
#         self.data = data
#         self.leftChild = None
#         self.rightChild = None

#     def insert(self, data):
#         ''' For inserting the data in the Tree '''
#         if self.data == data:
#             return False        # As BST cannot contain duplicate data

#         elif data < self.data:
#             ''' Data less than the root data is placed to the left of the root '''
#             if self.leftChild:
#                 return self.leftChild.insert(data)
#             else:
#                 self.leftChild = Node(data)
#                 return True

#         else:
#             ''' Data greater than the root data is placed to the right of the root '''
#             if self.rightChild:
#                 return self.rightChild.insert(data)
#             else:
#                 self.rightChild = Node(data)
#                 return True

#     def minValueNode(self, node):
#         current = node

#         # loop down to find the leftmost leaf
#         while(current.leftChild is not None):
#             current = current.leftChild

#         return current

#     def maxValueNode(self, node):
#         current = node

#         # loop down to find the leftmost leaf
#         while(current.rightChild is not None):
#             current = current.rightChild

#         return current


#     def delete(self, data, root):
#         ''' For deleting the node '''
#         if not self:
#             return self

#         # if current node's data is less than that of root node, then only search in left subtree else right subtree
#         if data < self.data:
#             self.leftChild = self.leftChild.delete(data,root)
#         elif data > self.data:
#             self.rightChild = self.rightChild.delete(data,root)
#         else:
#             # deleting node with one child
#             if self.leftChild is None:

#                 if self == root:
#                     temp = self.minValueNode(self.rightChild)
#                     self.data = temp.data
#                     self.rightChild = self.rightChild.delete(temp.data,root) 

#                 temp = self.rightChild
#                 self = None
#                 return temp
#             elif self.rightChild is None:

#                 if self == root:
#                     temp = self.maxValueNode(self.leftChild)
#                     self.data = temp.data
#                     self.leftChild = self.leftChild.delete(temp.data,root) 

#                 temp = self.leftChild
#                 self = None
#                 return temp

#             # deleting node with two children
#             # first get the inorder successor
#             temp = self.minValueNode(self.rightChild)
#             self.data = temp.data
#             self.rightChild = self.rightChild.delete(temp.data,root)

#         return self
    
    

#     def find(self, data):
#         ''' This function checks whether the specified data is in tree or not '''
#         if(data == self.data):
#             return True
#         elif(data < self.data):
#             if self.leftChild:
#                 return self.leftChild.find(data)
#             else:
#                 return False
#         else:
#             if self.rightChild:
#                 return self.rightChild.find(data)
#             else:
#                 return False

#     def preorder(self):
#         '''For preorder traversal of the BST '''
#         if self:
#             print(str(self.data), end = ' ')
#             if self.leftChild:
#                 self.leftChild.preorder()
#             if self.rightChild:
#                 self.rightChild.preorder()

#     def inorder(self):
#         ''' For Inorder traversal of the BST '''
#         if self:
#             if self.leftChild:
#                 self.leftChild.inorder()
#             print(str(self.data), end = ' ')
#             if self.rightChild:
#                 self.rightChild.inorder()

#     def postorder(self):
#         ''' For postorder traversal of the BST '''
#         if self:
#             if self.leftChild:
#                 self.leftChild.postorder()
#             if self.rightChild:
#                 self.rightChild.postorder()
#             print(str(self.data), end = ' ')

# class Tree(object):
#     def __init__(self):
#         self.root = None

#     def insert(self, data):
#         if self.root:
#             return self.root.insert(data)
#         else:
#             self.root = Node(data)
#             return True

#     def delete(self, data):
#         if self.root is not None:
#             return self.root.delete(data,self.root)

#     def find(self, data):
#         if self.root:
#             return self.root.find(data)
#         else:
#             return False

#     def preorder(self):
#         if self.root is not None:
#             print()
#             print('Preorder: ')
#             self.root.preorder()

#     def inorder(self):
#         print()
#         if self.root is not None:
#             print('Inorder: ')
#             self.root.inorder()

#     def postorder(self):
#         print()
#         if self.root is not None:
#             print('Postorder: ')
#             self.root.postorder()





# tree = Node(1)
# tree.insert(10)
# tree.insert(12)
# tree.insert(5)
# tree.insert(4)
# tree.insert(20)
# tree.insert(8)
# tree.insert(7)
# tree.insert(15)
# tree.insert(13)
# print(tree.find(1))
# print(tree.find(12))
#     ''' Following tree is getting created:
#                     10
#                  /      \
#                5         12
#               / \           \
#             4     8          20
#                  /          /
#                 7         15
#                          /
#                        13
#     '''

# tree.preorder_traversal()
# tree.inorder_traversal()
# tree.postorder_traversal()
# print('\n\nAfter deleting 20')
# tree.delete(20)
# tree.inorder_traversal()
# tree.preorder_traversal()
# print('\n\nAfter deleting 10')
# tree.delete(10)
# tree.inorder_traversal()
# tree.preorder_traversal()


