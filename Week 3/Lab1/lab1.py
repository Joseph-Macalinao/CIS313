from typing import Any


class Node(object):
    """
    A class to represent a node.

    ...

    Attributes
    ----------
    data : int or float
        An individual character or number to be stored in a node
    next_node : object of class Node
        A pointer to the next node in a stack or queue

    Methods
    -------
    setData(data):
        Updates the value of data attribute of Node
    setNext(next_node):
        Updates the value of next_node attribute of Node
    getData():
        Returns the value of data attribute
    getNext():
        Returns the value of next_node attribute
    """
    def __init__(self, data = None, next_node = None):
        """
        Constructs (or initializes) the attributes for an object of the class

        ...

        Parameters
        ----------
        data : int or float
            An individual character or number to be stored in a node
        next_node : object of class Node
            A pointer to the next node in a stack or queue

        """
        self.__data = data
        self.__next_node = next_node

    def setData(self, data):
        '''Set the "data" data field to the corresponding input.'''
        self.__data = data

    def setNext(self, next_node):
        '''Set the "next_node" data field to the corresponding input.'''
        self.__next_node = next_node

    def getData(self):
        '''Return the "data" data field.'''
        return self.__data

    def getNext(self):
        '''Return the "next_node" data field.'''
        return self.__next_node

class Queue(object):
    """A class to represent a node.

    ...

    Attributes
    ----------
    head : Node object
        first node in line to be dequeued
    tail : object of class Node
        last node to be queued

    Methods
    -------
    enqueue(self, newData)
        enqueues items to the queue

    dequeue(self)
        takes head of queue and returns its value while setting the next node as the new head

    isEmpty(self)
        checks to see if the queue is empty
    """

    def __init__(self):
        self.__head = None
        self.__tail = None

    def __str__(self):
        '''Loop through your queue and print each Node's data.'''
        str_list = []

        if self.__head is None:
            return None
        else:
            next = self.__head
            while (next != None):
                str_list.append(next.getData())
                next = next.getNext()

        return str(str_list)

    def enqueue(self, newData):
        '''Create a new node whose data is newData and whose next node is null
        Update head and tail.'''
        # Hint: Think about what's different for the first node added to the Queue
        node = Node(data=newData)
        if self.__head is None:
            self.__head = node
            self.__tail = node
            return
        else:
            self.__tail.setNext(node)
            self.__tail = node


    def dequeue(self):
        '''Return the head of the Queue
        Update head.'''
        #  Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #          to hold important information
        #  Hint: Return null on a empty Queue
        # Hint: Return the element(data) that is dequeued.
        if self.__head == None:
            raise Exception("Empty")


        front = self.__head
        self.__head = self.__head.getNext()

        if self.__head is None:
            self.__tail = None
        return front.getData()



    def isEmpty(self):
        '''Check if the Queue is empty.'''
        return self.__head == None



class Stack(object):
    """A class to represent a node.

    ...

    Attributes
    ----------
    head : Node object
        "top" object in the stack


    Methods
    -------
    push(newData):
        pushes new node on top of stack

    pop(next_node):
        pops off top node from stack and returns its value

    isEmpty():
        checks to see if the stack is empty
    """
    def __init__(self):
        ''' We want to initialize our Stack to be empty.
        (ie) Set top as null'''
        self.__head = None
        '''
        1) head points to a node
        2)head -> next value'''

    def __str__(self):
        '''Loop through your stack and print each Node's data.'''
        str_list = []


        if self.__head is None:
            return None
        else:
            next = self.__head
            while(next != None):
                str_list.append(next.getData())
                next = next.getNext()

        return str(str_list)

    def push(self, newData):
        '''We want to create a node whose data is newData and next node is top.
        Push this new node onto the stack
        Update top'''
        node = Node(data=newData)
        if self.__head is None:
            self.__head = node
        else:
            node.setNext(self.__head)
            self.__head = node

    def pop(self):
        ''' Return the Node that currently represents the top of the stack.
        Update top'''
        # Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #         to hold important information
        # Hint: Return null on a empty stack
        # Hint: Return the element(data) that is popped
        if self.__head == None:
            return None
            #raise Exception("Empty")

        else:
            popped = self.__head
            self.__head = self.__head.getNext()
            popped.__next_node = None
            return popped.getData()

    def isEmpty(self):
        '''Check if the Stack is empty.'''
        return self.__head is None

class TwoStackQueue(object):
    def __init__(self):
        stack1 = Stack()
        stack2 = Stack()
        self.stack1 = stack1
        self.stack2 = stack2

    def enqueue(self, newData):
        return



def isPalindrome(s):
    '''Use your Queue and Stack class to test wheather an input is a palindrome.'''
    s = s.lower()
    s = s.replace(" ",'')
    #print(s)
    myStack = Stack()
    myQueue = Queue()
    for i in range(len(s)):
        myStack.push(s[i])
        #print(f"push {s[i]}")
        myQueue.enqueue(s[i])
        #print(f"queue {s[i]}")
    #print(myQueue)
    #print(myStack)
    for i in range(len(s)):
        popped = myStack.pop()
        deq = myQueue.dequeue()
        #print(f"{popped.getData()} {deq.getData()}\n")
        if popped != deq:
            return False
        else:
            continue


    ## Helper function ##
    # print("stack data")
    # myStack.printStack()

    # print("queue data")
    # myQueue.printQueue()

    # Return appropriate value
    return True

def isPalindromeEC(s):
    '''Implement if you wish to do the extra credit.'''

    # Return appropriate value
    s = s.lower()
    s = s.replace(" ",'')
    #print(s)
    myTwoQueue = TwoStackQueue()
    for i in range(len(s)):
        #print(f"push {s[i]}")
        TwoStackQueue.enqueue(s[i])
        #print(f"queue {s[i]}")
    #print(myQueue)
    #print(myStack)
    for i in range(len(s)):
        deq = TwoStackQueue.dequeue()
        #print(f"{popped.getData()} {deq.getData()}\n")

