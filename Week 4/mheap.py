
class max_heap(object):
    """Binary max-heap

    Supports most standard heap operations (insert, peek, extract_max).
    Can be used for building a priority queue or heapsort. Since Python
    doesn't have built-in arrays, the underlying implementation uses a
    Python list instead. When initialized, max_heap creates a new list of
    fixed size or uses an existing list.

    atts: size, data
    size: the size is the length of any given heap and will provide bounds on how big
    it can get when inserting
    data: the data that will be input into the max heap, either in list or none format

    methods:

    get_heap - returns heap
    insert - inserts new data into heap and reformats if necessary
    peek - returns root node without removing it
    extract_max - returns and removes root node and reformats heap
    __heapify - sifts items downwards until heap is correct
    build_heap - builds a heap out of data given (usually in a list)
    __get_parent - gets the parent location of a node
    __get_left - gets left child of a node
    __get_right - gets right child of a node
    __swap - swaps two nodes


    """

    def __init__(self, size = 20, data = None):
        """Initialize a binary max-heap.

        size: Total capacity of the heap.
        data: List containing the desired heap contents. 
              The list is used in-place, not copied, so its contents 
              will be modified by heap operations.
              If data is specified, then the size field is ignored."""

        # Add to this constructor as needed
        if data is not None:
            self.max_size = len(data)
            self.length = len(data)
            self.heap = data
        else:
            self.max_size = size
            self.length = 0
            self.heap = [None] * size
        
    def get_heap(self):
        '''
        gets the heap data
        :return: the heap in a list format
        '''
        return self.heap


    def insert(self, data):
        """Insert an element into the heap.
        If needed, it will swap nodes around to fit the heap format
        data: the new data that is to be input into the heap class
        Raises IndexError if the heap is full."""
        # Tips : insert 'data' at the end of the list initially
        #      : swap with its parent until the parent is larger or you 
        #      : reach the root
        
        # whatever the new index is, index/2 shows where it goes under

        if self.length >= self.max_size:
            raise IndexError
            #("Too big for ye britches")
        self.heap[self.length] = data
        self.length += 1

        curr = self.length - 1

        while (curr > 0 and self.heap[curr] > self.heap[self.__get_parent(curr)]):
            self.__swap(self.__get_parent(curr), curr)
            curr = self.__get_parent(curr)

        


    def peek(self):
        """Return the maximum value in the heap.
        return: the max node value in the heap
        """
        if self.length == 0:
            return None
        return self.heap[0]

    def extract_max(self):
        """Remove and return the maximum value in the heap.
        then swaps nodes around to reformat the necessary amounts of times to get
        into heap format
        :return: the maximum value in a heap
        Raises KeyError if the heap is empty."""
        # Tips: Maximum element is first element of the list
        #     : swap first element with the last element of the list.
        #     : Remove that last element from the list and return it.
        #     : call __heapify to fix the heap
        if self.length == 0:
            raise KeyError
        max = self.heap[0]
        self.heap[0] = self.heap[self.length - 1]
        self.heap[self.length - 1] = None
        self.length -= 1
        self.__heapify(0)

        return max


    def __heapify(self, curr_index, list_length = None):
        '''
        "heapifies data to properly return the proper list formating from big to small, starting at curr_index
        :param curr_index: the place in the heap that heapify will occur
        :param list_length: the length of a given list
        :return: no return , swaps the heap in place
        '''
        # helper function for moving elements down in the heap
        # Page 157 of CLRS book
        if list_length is None:
            list_length = self.length
        right_child = self.__get_right(curr_index)
        left_child = self.__get_left(curr_index)

        max = curr_index
        if (left_child < list_length and self.heap[left_child] > self.heap[curr_index]):
            max = left_child
            if (right_child < list_length and self.heap[right_child] > self.heap[max]):
                max = right_child
        if (max != curr_index):
            self.__swap(curr_index, max)
            self.__heapify(max, list_length)

    def build_heap(self):
        '''
        build a heap out of given data to fit heap format
        uses the given data to then move nodes around in the array provided
        :return: none
        '''
        # builds max heap from the list l.
        # Tip: call __heapify() to build to the list
        #    : Page 157 of CLRS book
        for i in range(int((self.length / 2) - 1), -1, -1):
            self.__heapify(i)


    ''' Optional helper methods may be used if required '''
    ''' You may create your own helper methods as required.'''
    ''' But do not modify the function definitions of any of the above methods'''

    def __get_parent(self, loc):
        '''
        gets the parent of a given node in a max heap
        :param loc: the current location of a given node in the heap
        :return: the location of the parent of the node input in the heap
        '''
        # left child has odd location index
        # right child has even location index
        parent = int((loc - 1) / 2)
        return parent

    def __get_left(self, loc):
        '''
        get the left child of a given "node" in a max heap
        :param loc: location in the heap that the node is in
        :return: the location of the left child
        '''
        return 2*loc + 1

    def __get_right(self, loc):
        '''
        gets the right child of a given "node" in a max heap
        :param loc: the location in the heap that the node is in
        :return: the location of the right child
        '''
        return 2*loc + 2
        

    def __swap(self, a, b):
        '''
        swap function in the max heap class to swap two elements in the heap
        :param a: first element to swap, item in list
        :param b: second element to swap, item in list
        :return: none
        '''
        # swap elements located at indexes a and b of the heap
        temp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = temp
    



    

def heap_sort(l):
    """Sort a list in place using heapsort.
    l: list given to heap_sort on
    return : a list that is now heap sorted
    """
    # Note: the heap sort function is outside the class
    #     : The sorted list should be in ascending order
    # Tips: Initialize a heap using the provided list
    #     : Use build_heap() to turn the list into a valid heap
    #     : Repeatedly extract the maximum and place it at the end of the list
    #     : Refer page 161 in the CLRS textbook for the exact procedure
    
    #needs insert, and deletion (nlogn)
    #need a counter for back insertion of elements

    # Initialize a heap using the provided list
    heap = max_heap(size=len(l), data=l)

    heap.build_heap()

    for i in range(len(l) - 1, -1, -1):
        max = heap.extract_max()
        l[i] = max
    return l