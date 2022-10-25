import lab1
import unittest

class T0_TestingQueue(unittest.TestCase):

    def test_basic_enqueue(self):
        # testing the basic enqueue operation
        print("\n")
        q = lab1.Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)

        self.assertEqual(q.__str__(), '[1, 2, 3, 4]')
        print("\n")

class T1_TestingStack(unittest.TestCase):

    def test_is_empty_false(self):
        # testing if queue is empty
        print("\n")
        s = lab1.Stack()
        s.push("4")
        print("return false if the stack is not empty")
        self.assertEqual(s.isEmpty(), False)
        print("\n")


class T2_TestingPalindrome(unittest.TestCase):

    def test_basic_string(self):
        # testing with basic string
        print("\n")
        string = "hello"
        p = lab1.isPalindrome(string)
        print("The string being tested is -> ", string)
        self.assertEqual(p, False)
        print("\n")

class T3_TestingDequeue(unittest.TestCase):

    def test_dequeue(self):
        q = lab1.Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        deq = q.dequeue()

        self.assertEqual(deq, 1)


class T4_TestingPush(unittest.TestCase):

    def test_basic_push(self):
        # testing the basic enqueue operation
        print("\n")
        q = lab1.Stack()
        q.push(1)
        q.push(2)
        q.push(3)
        q.push(4)

        self.assertEqual(q.__str__(), '[4, 3, 2, 1]')
        print("\n")

class T5_TestingPop(unittest.TestCase):

    def test_pop(self):
        s = lab1.Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        pop = s.pop()


        self.assertEqual(pop, 3)

class T6_TestingisEmpty(unittest.TestCase):

    def testEmpty(self):
        s = lab1.Stack()
        self.assertEqual(s.isEmpty(), True)

    def testEmpty2(self):
        s = lab1.Queue()
        self.assertEqual(s.isEmpty(), True)

    def testEmpty3(self):
        s = lab1.TwoStackQueue()
        self.assertEqual(s.isEmpty(), True)

if __name__ == '__main__':
    unittest.main()
