class Node(object):
    def __init__(self, data):
        self.parent = None
        self.left = None
        self.right = None
        self.data = data


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
        if self.root is None:
            self.root = Node(data)
            return
        new_node = Node(data)
        new_parent = None
        curr = self.root
        # if ((curr.left is None) and (curr.right is None)):
        #     if (data > curr.data):
        #         curr.right = Node(data)
        #     elif (data < curr.data):
        #         curr.left = Node(data)
        while (curr != None):
            if (curr.left is None) and (data < curr.data):
                curr.left = new_node
                new_node.parent = new_parent
                break
            elif (curr.right is None) and (data > curr.data):
                curr.right = new_node
                new_node.parent = new_parent
                break
            elif (curr.left != None) and (data < curr.data):
                new_parent = curr
                curr = curr.left
            elif (curr.right != None) and (data > curr.data):
                new_parent = curr
                curr = curr.right
        if ((curr.left is None) and (curr.right is None)):
            if (data > curr.data):
                curr.right = new_node
                new_node.parent = new_parent
            elif (data < curr.data):
                curr.left = new_node
                new_node.parent = new_parent

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
        pass

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
        if self.contains(data) is False:
            raise KeyError
        curr = self.__find_node(data)
        # tree = Tree
        # tree.root = curr
        curr_p = curr.parent
        print(f"{curr.data}")
        print(f"{curr.parent.data}")
        print(f"{curr.left.data}")
        print(f"{curr.right.data}")
        if curr.right is not None:
            curr = curr.right
            while curr.left is not None: #just part
                curr = curr.left
            return curr#not actual conditional
        print(f"{curr_p.data}")
        while curr_p is not None and curr == curr_p.right:
            curr = curr_p
            curr_p = curr_p.parent
        if curr_p.data == self.root.data:
            return self.root
        return curr_p





        # if self.root is None:
        #     return None
        # if self.contains(data) is False:
        #     raise KeyError
        # curr = self.__find_node(data)
        # curr_right = curr.right
        # if curr.right is not None:
        #     while (curr != None):
        #         curr = curr.right
        #         if curr.left is not None:
        #             return curr.left
        #     return curr_right
        #     #return curr.min()
        #     #return curr.min()
        # else: #should find if a nodes data is smaller than current succ but greater than data
        #     curr = self.__find_node(data)
        #     while(curr != self.root.right and curr != self.root.left):
        #         curr = curr.parent
        #         if (curr.parent.left is not None):
        #             if curr.parent.left == curr:
        #                 return curr
        # return None


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
        del_node = self.__find_node(data)
        if del_node.data > del_node.parent.data:
            if del_node.left is None and del_node.right is None:
                del_node.right = None
            elif del_node.left is None and del_node.right is not None:
                del_node.parent.right = del_node.right
            elif del_node.right is None and del_node.left is not None:
                del_node.parent.right = del_node.left

        elif del_node.data > del_node.parent.data:
            if del_node.left is None and del_node.right is None:
                del_node.parent.left = None
            elif del_node.left is None and del_node.right is not None:
                del_node.parent.left = del_node.right
            elif del_node.right is None and del_node.left is not None:
                del_node.parent.left = del_node.left







