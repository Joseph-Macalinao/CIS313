class Node(object):

    def __init__(self, data):
        self.parent = None
        self.left = None
        self.right = None
        self.data = data

    def set_parent(self, curr_node, parent):
        '''
        sets the parent of a node
        :param curr_node: the node to give a parent
        :param parent: the new parent of the node
        :return: none
        '''
        curr_node.parent = parent


class Tree(object):
    '''
    Implementation of a binary search tree along with often used methods. Also able to traverse through tree
    Attr:
    The orders labeled as 1,2,3
    Preorder: 1
    Inorder: 2
    Postorder: 3

    self.root: Node - starts as None in initialization

    ~~~~~~~~~~~~~~~~~~~~
    Methods - all with self arg
    print()
    calls __print to recursively call print on nodes
    :arg na
    :return na

    __print()
    recursively calls itself to print inorder
    :arg curr_node: Node - where to print from
    :return na

    insert()
    inserts data into a bst tree while making sure the structure stays intact
    :arg data: int: the number to be placed into a tree
    :return na

    min()
    finds the smallest value in a given bst
    :arg na
    :return returns the smallest value in a tree

    max()
    finds the largest value in a given bst
    :arg na
    :return returns the largest value in a tree

    __find_node()
    finds a node in a tree given a data point to match against, returns None otherwise
    :arg data: int - the value to check against for each
    :return the node which matches value, returns None if node doesn't exist

    contains()
    calls find_node to see if a node exists in a tree
    :arg data: int - the value to check is in given bst tree
    :return Boolean

    __iter__()
     goes through bst using a for loop inorder
    :arg na
    :return the list of a inorder bst

    inorder()
    helper function for the traverse method to go through tree inorder
    :arg na
    :return: returns a given tree traversed, Inorder

    preorder()
    helper function for the traverse method to go through tree preorder
    :arg na
    :return returns a given tree traversed, Preorder

    postorder()
    helper function for the traverse method to go through tree postorder
    :arg na
    :return returns a given tree traversed, Postorder

    __traverse()
    traverses through a tree and yields data on each node depending on the traversal type: Pre, In, Post
    :arg curr_node, Traversal_Type: Node, Traversal - curr_node is the node to traverse from recursively,
    Traversal Type is the order in which nodes are yielded, either:
     In: left, root, right
     Pre: root, left, right
     Post: left, right, root
    :return

    __find_successor()
    gives the successor to a node in a bst, keyError risen if node to find for doesn't exist
    :arg data: int - value to check that has a successor
    :return: the node of which is a successor to the given data: may raise a keyError if initial data given
    doesn't find a node in bst matching

    delete()
    deletes a node from a bst when given the data point to delete, raises KeyError if node doesn't exist
    :arg data: int - the value of a node to delete
    :return None, may raise keyError if node doesn't exist

    '''
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
        return self.__find_node(data) is not None

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

        # Yield data of the correct node/s
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
        if self.contains(data) == False:
            raise KeyError
        if self.root is None:
            return None
        curr = self.__find_node(data)

        curr_p = curr.parent
        if curr.right is not None:
            curr = curr.right
            while curr.left is not None:
                curr = curr.left
            return curr
        while curr_p is not None and curr == curr_p.right:
            curr = curr_p
            curr_p = curr_p.parent
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
        if self.contains(data) is False:
            raise KeyError
        if self.root is None:
            return None
        delete = self.__find_node(data)

        succ = self.find_successor(data)
        parent = delete.parent

        # if the node has no children
        if delete.left is None and delete.right is None:
            # print(f"{delete.data}")
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
            if delete is self.root:  # check if node is root
                if delete.left is None:
                    self.root = delete.right
                else:
                    self.root = delete.left
            else:  # node is now not root
                if parent.right is delete and delete.right is None:  # splice the parent and child together
                    delete.left.parent = parent
                    parent.right = delete.left

                elif parent.right is delete and delete.left is None:  # splicing the parent with the nodes right child
                    delete.right.parent = parent
                    parent.right = delete.right

                elif parent.left is delete and delete.right is None:  # splicing the parent with the nodes left child
                    delete.left.parent = parent
                    parent.left = delete.left

                elif parent.left is delete and delete.left is None:
                    delete.right.parent = parent
                    parent.right = delete.right

            return

        # if the node has 2 children
        elif delete.left is not None and delete.right is not None:
            store = succ.data
            self.delete(succ.data)
            delete.data = store
            return

        return