import unittest
import pqueue
import mheap


class T0_pqueue_insert(unittest.TestCase):


    def test_1_pq_insert(self):
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        pq.insert(4)
        pq.insert(5)
        pq_list = [element for element in pq]
        self.assertEqual(pq_list, [5,4,2,1,3])
        print("\n")

class T1_pqueue_peek(unittest.TestCase):

    def test_1_pq_peek(self):
        print("Just return the fist element of the queue.")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        self.assertEqual(pq.peek(), 3)
        print("\n")


class T2_pqueue_extract_max(unittest.TestCase):

    def test_1_pq_extract_max(self):
        print("extract and return the maximum element of the queue")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        self.assertEqual(pq.extract_max(), 3)
        print("\n")


class T5_heap_sort(unittest.TestCase):

    def test_heap_sort_1(self):
        print("\n")
        to_sort_list = [10,24,3,57,4,67,37,87,7]
        sorted_list = mheap.heap_sort(to_sort_list)

        self.assertEqual(sorted_list, [3, 4, 7, 10, 24, 37, 57, 67, 87])
        print("\n")

class T6_build_heap(unittest.TestCase):

    def test_build_heap(self):
        print("\n")
        mh = mheap.max_heap(data=[10,24,3,57,4,67,37,87,7])
        mh.build_heap()
        self.assertEqual(mh.get_heap(), [87,57,67,24,4,3,37,10,7])
        print("\n")

class T7_insert_full(unittest.TestCase):

    def test_insert_full(self):
        print("\n")
        mh = mheap.max_heap(data=[10, 24, 3, 57, 4, 67, 37, 87, 7])
        self.assertRaises(IndexError, mh.insert, 5)



class T8_extract_empty(unittest.TestCase):

    def test_extract_empty(self):
        print("\n")
        mh = mheap.max_heap(data=[])
        self.assertRaises(KeyError, mh.extract_max)

class T9_operate_pqueue(unittest.TestCase):

    def test_operate_pqueue(self):
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert("hello")
        pq.insert("world")
        pq.insert("python")
        pq.insert("CIS313")
        pq.insert("Joe")
        self.assertEqual(pq.peek(), "world")

class T10_insert(unittest.TestCase):

    def test_insert_word_full(self):
        print("\n")
        mh = mheap.max_heap(size=4, data=[1,3])
        self.assertRaises(IndexError, mh.insert, "yo")

class T11_insert(unittest.TestCase):

    def test_insert_after_delete_full(self):
        print("\n")
        mh = mheap.max_heap(size=4, data=[1,3])
        mh.extract_max()
        mh.insert(5)
        self.assertRaises(IndexError, mh.insert, 6)

class T12_extract_after(unittest.TestCase):

    def test_extract_after(self):
        print("\n")
        mh = mheap.max_heap(data=[1,2,3,4,5])
        for i in range(5):
            mh.extract_max()
        self.assertRaises(KeyError, mh.extract_max)


class T13_build_heap(unittest.TestCase):

    def test_build_heap_twice(self):
        print("\n")
        mh = mheap.max_heap(data=[10,24,3,57,4,67,37,87,7])
        mh.build_heap()
        self.assertEqual(mh.get_heap(), [87,57,67,24,4,3,37,10,7])
        print("\n")
        mh.extract_max()
        mh.build_heap()
        self.assertEqual(mh.get_heap(), [67, 57, 7, 24, 4, 3, 37, 10, 87])


class T14_heap_sort_twice(unittest.TestCase):

    def test_heap_sort_twice(self):
        print("\n")
        to_sort_list = [10,24,3,57,4,67,37,87,7]
        sorted_list = mheap.heap_sort(to_sort_list)

        self.assertEqual(sorted_list, [3, 4, 7, 10, 24, 37, 57, 67, 87])
        print("\n")

        to_sort_list.pop()

        sorted_list_2 = mheap.heap_sort(to_sort_list)
        self.assertEqual(sorted_list_2, [3, 4, 7, 10, 24, 37, 57, 67])

class T15_heap_sort_wierd(unittest.TestCase):

    def test_heap_weird(self):
        print("\n")
        to_sort_list_weird = ["HI", "YO", "Test"]
        sorted_list = mheap.heap_sort(to_sort_list_weird)

        self.assertEqual(sorted_list, ['HI', 'Test', 'YO'])


'''
tests:
    test_build_heap
    test_insert_full
    test_extract_empty
    test_operate_pqueue    ->    do things with pqueue()
    6 other tests
'''

    
    
if __name__ == '__main__':
    unittest.main()