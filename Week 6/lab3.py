class Node(object):
    def __init__(self, data):
        self.parent = None
        self.left = None
        self.right = None
        self.data = data


    def set_parent(self, curr_node, parent):
        curr_node.parent = parent

class Tree(object):
    # Binary Search Tree
    # class constants
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

    def __init__(self):
        # Do not create any other private variables.
        # You may create more helper methods as needed.
        self.root = None

    def print(self):
        # Print the data of all nodes in order
        self.__print(self.root)


    def __print(self, curr_node):
        # Recursively print a subtree (in order), rooted at curr_node
        if curr_node is not None:
            self.__print(curr_node.left)
            print(str(curr_node.data), end=' ')  # save space
            self.__print(curr_node.right)
            

    def insert(self, data):
        # Find the right spot in the tree for the new node
        # Make sure to check if anything is in the tree
        # Hint: if a node n is None, calling n.data will cause an error
        node = Node(data)
        if self.root is None:
            self.root = node
            return
        parent = None
        curr = self.root
        # if ((curr.left is None) and (curr.right is None)):
        #     if (data > curr.data):
        #         curr.right = Node(data)
        #     elif (data < curr.data):
        #         curr.left = Node(data)
        while (curr != None):
            if curr.data > data:
                parent = curr
                curr = curr.left
            elif curr.data < data:
                parent = curr
                curr = curr.right
        if parent.data > data:
            parent.left = node
            node.set_parent(node, parent)
        elif parent.data < data:
            parent.right = node
            node.set_parent(node, parent)


    def min(self):
        # Returns the minimum value held in the tree
        # Returns None if the tree is empty
        if self.root is None:
            return None
        min = self.root.data
        curr = self.root
        while (curr != None):
            min = curr.data
            curr = curr.left

        return min


    def max(self):
        # Returns the maximum value held in the tree
        # Returns None if the tree is empty
        if self.root is None:
            return None
        max = self.root.data
        curr = self.root
        while (curr != None):
            max = curr.data
            curr = curr.right

        return max

    def __find_node(self, data):
        # returns the node with that particular data value else returns None
        if self.root is None:
            return None
        curr = self.root
        while (curr != None):
            if (curr.data == data):
                return curr
            elif (curr.data > data):
                curr = curr.left
            elif (curr.data < data):
                curr = curr.right
        return None

    def contains(self, data):
        # return True of node containing data is present in the tree.
        # otherwise, return False.
        # you may use a helper method __find_node() to find a particular node with the data value and return that node
        if self.root is None:
            return None
        curr = self.root
        while (curr != None):
            if (curr.data == data):
                return True
            elif (curr.data > data):
                curr = curr.left
            elif (curr.data < data):
                curr = curr.right
        return False

    def __iter__(self):
        # iterate over the nodes with inorder traversal using a for loop
        return self.inorder()

    def inorder(self):
        # inorder traversal : (LEFT, ROOT, RIGHT)
        return self.__traverse(self.root, Tree.INORDER)

    def preorder(self):
        # preorder traversal : (ROOT, LEFT, RIGHT)
        return self.__traverse(self.root, Tree.PREORDER)

    def postorder(self):
        # postorder traversal : (LEFT, RIGHT, ROOT)
        return self.__traverse(self.root, Tree.POSTORDER)

    def __traverse(self, curr_node, traversal_type):
        # helper method implemented using generators
        # all the traversals can be implemented using a single method

        #Yield data of the correct node/s
        if curr_node != None:
            if traversal_type == Tree.PREORDER:
                yield curr_node.data
                yield from self.__traverse(curr_node.left, Tree.PREORDER)
                yield from self.__traverse(curr_node.right, Tree.PREORDER)
            elif traversal_type == Tree.INORDER:
                yield from self.__traverse(curr_node.left, Tree.INORDER)
                yield curr_node.data
                yield from self.__traverse(curr_node.right, Tree.INORDER)
            elif traversal_type == Tree.POSTORDER:
                yield from self.__traverse(curr_node.left, Tree.POSTORDER)
                yield from self.__traverse(curr_node.right, Tree.POSTORDER)
                yield curr_node.data

    def find_successor(self, data):
        # Find the successor node
        # If the value specified by find_successor does NOT exist in the tree, then raise a KeyError
        # helper method to implement the delete method but may be called on its own
        # If the right subtree of the node is nonempty,then the successor is just 
        # the leftmost node in the right subtree.
        # If the right subtree of the node is empty, then go up the tree until a node that is
        # the left child of its parent is encountered. The parent of the found node will be the
        # successor to the initial node.
        # Note: Make sure to handle the case where the parent is None
    
    	# Return object of successor if found else return None


        if self.root is None:
            return None
        curr = self.__find_node(data)
        if self.contains(data) is False:
            raise KeyError
        #curr = self.__find_node(data)
        curr_p = curr.parent
        if curr.right is not None:
            curr = curr.right
            while curr.left is not None:
                curr = curr.left
            return curr
        while curr_p is not None and curr == curr_p.right:
            curr = curr_p
            curr_p = curr_p.parent
        # if curr_p.data == self.root.data and self.root.data > data:
        #     return self.root
        # elif curr_p.data != self.root.data:
        #     return None
        return curr_p




    def delete(self, data):
        # Find the node to delete.
        # If the value specified by delete does NOT exist in the tree, then don't change the tree and raise a KeyError
        # If you find the node and ...
        #  a) The node has no children, just set it's parent's pointer to None.
        #  b) The node has one child, make the nodes parent point to its child.
        #  c) The node has two children, replace it with its successor, and remove
        #       successor from its previous location.
        # Recall: The successor of a node is the left-most node in the node's right subtree.
        # Note: Make sure to handle the case where the parent is None
        if self.root is None:
            return None
        delete = self.__find_node(data)
        if delete is None:
            raise KeyError
        succ = self.find_successor(delete.data)
        parent = delete.parent
        # print(f"delte is {delete.data}")
        # print(f"succ is {succ.data}\n")
        #print(f"parent is {parent.data} \n")

        # if the node has no children
        if delete.left is None and delete.right is None:
            #print(f"{delete.data}")
            if delete is not self.root:  # check to make sure node isn't root, otherwise make root none
                if parent.left is delete:
                    parent.left = None
                else:
                    parent.right = None
            else:
                self.root = None
            return

        # if the node has only 1 child
        elif delete.left is None or delete.right is None:
            print(f"{delete.data}")
            if delete is self.root:  # check if node is root
                if delete.left is None:
                    self.root = delete.right
                else:
                    self.root = delete.left
            else:  # node is now not root
                if parent.right is delete and delete.right is None:  # splice the parent and child together
                    parent.right = delete.left
                elif parent.right is delete and delete.left is None:
                    parent.right = delete.right
                elif delete.left is delete and delete.right is None:
                    parent.left = delete.left
                else:
                    parent.right = delete.right
            return

        # if the node has 2 children
        elif delete.left is not None and delete.right is not None:
            #print(f"{delete.data}")
            store_succ = succ.data

            self.delete(succ.data)

            delete.data = store_succ









