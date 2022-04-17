import unittest
from bag_da import *

class MyTestCase ( unittest.TestCase ):
    def test_add(self):
        bag = Bag()
        self.assertEqual(bag._da._data[0], None )
        bag.add(1)
        self.assertEqual(bag._da._data[0],1)
        bag.add(2)
        self.assertEqual(bag._da._data[1],2)

    def test_remove(self):
        bag = Bag()
        for x in range(0,3):
            bag.add(1)
        self.assertFalse(bag.remove(2))
        self.assertTrue(bag.remove(1))

        self.assertEqual(bag._da._data[0],1)
        self.assertEqual(bag._da._data[1],1)
        bag.add(2)
        bag.remove(1)
        self.assertEqual ( bag._da._data[0], 1 )
        self.assertEqual(bag._da._data[1],2)

    def test_count(self):
        bag = Bag()
        for x in range(0,10):
            bag.add(1)

        self.assertEqual(bag.count(1),10)
        bag.remove(1)
        self.assertEqual(bag.count(1),9)
        bag.add(2)
        self.assertEqual(bag.count(2),1)
        self.assertEqual(bag.count(3),0)

    def test_clear(self):
        bag = Bag()
        for x in range(0,10):
            bag.add(x)
        bag.clear()
        self.assertEqual(bag._da._data[0],None)
        self.assertEqual(bag.size(),0)

    def test_equals(self):
        bag1 = Bag()
        bag2 = Bag()
        bag3 = Bag ( [10, 20, 30, 40, 50, 60] )
        bag4 = Bag ( [60, 50, 40, 30, 20, 10] )
        bag5 = Bag ( [10, 20, 30, 40, 50] )

        self.assertTrue(bag1.equal(bag2))
        self.assertTrue(bag3.equal(bag4))
        self.assertFalse(bag3.equal(bag5))
        self.assertFalse(bag4.equal(bag5))
        self.assertFalse(bag5.equal(bag4))
        self.assertTrue(bag5.equal(bag5))

    def test_iter(self):
        bag = Bag ( [5, 4, -8, 7, 10] )
        for item in bag:
            print ( item )



if __name__ == '__main__':
    unittest.main ()
