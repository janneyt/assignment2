import unittest
from dynamic_array import DynamicArray, DynamicArrayException, find_mode
from static_array import StaticArrayException


class MyTestCase ( unittest.TestCase ):
    def test_empty_array(self):
        da = DynamicArray()
        self.assertEqual ( da.get_capacity(),4 )
        old_data = da._data
        self.assertEqual(da._data, old_data)
        da.resize(5)
        self.assertEqual(da.get_capacity(),5)
        with self.assertRaises(DynamicArrayException):
            da.resize(-1)

    def test_resize_full_array(self):
        da = DynamicArray([1,2,3,4,5,6,7,8])
        da.append(1)
        da.append(2)
        self.assertEqual(da._size,10)
        self.assertEqual(da._capacity,16)
        da.resize(12)
        self.assertEqual(da._size,10)
        self.assertEqual(da._capacity,12)
        with self.assertRaises(DynamicArrayException):
            da.resize(9)

    def test_append(self):
        da = DynamicArray()
        da.append(1)
        self.assertEqual(da._size,1)
        self.assertEqual(da._capacity, 4)
        self.assertEqual(da._data[0],1)
        da.append(2)
        self.assertEqual(da._size,2)
        self.assertEqual(da._capacity,4)
        self.assertEqual(da._data[1],2)
        da.append(3)
        da.append(4)
        da.append(5)
        self.assertEqual(da._size,5)
        self.assertEqual(da._capacity, 8)
        self.assertEqual(da._data[3],4)

        self.assertEqual(da._data[4],5)

        self.assertEqual(da._data[5],None)

    def test_insert_at_index(self):
        da = DynamicArray()
        with self.assertRaises(DynamicArrayException):
            da.insert_at_index(1,100)
        with self.assertRaises(DynamicArrayException):
            da.insert_at_index(-1,100)
        da.insert_at_index(0,100)
        self.assertEqual(da._size,1)
        self.assertEqual(da._capacity, 4)
        self.assertEqual(da._data[0],100)
        da.insert_at_index(0,200)
        self.assertEqual(da._data[0],200)
        self.assertEqual(da._data[1],100)
        da.insert_at_index(0,300)
        self.assertEqual(da._data[0],300)
        self.assertEqual(da._data[1],200)
        self.assertEqual(da._data[2],100)
        self.assertEqual(da._size,3)
        self.assertEqual(da._capacity,4)
        da.insert_at_index(0,400)
        da.insert_at_index(0,500)
        self.assertEqual(da._size,5)
        self.assertEqual(da._capacity,8)
        self.assertEqual(da._data[4],100)
        self.assertEqual(da._data[3],200)
        self.assertEqual(da._data[2],300)
        self.assertEqual(da._data[1],400)
        self.assertEqual(da._data[0],500)
        da.insert_at_index(4,600)
        self.assertEqual(da._data[4],600)
        self.assertEqual(da._data[5],100)
        self.assertEqual(da._data[3],200)
        self.assertEqual(da._size, 6)
        self.assertEqual(da._capacity,8)

    def test_restore_values(self):
        da = DynamicArray ( [1, 2, 3, 4, 5, 6] )
        da.restore_values(3,-1)
        self.assertEqual(da._data[3],5)

    def test_remove_at_index(self):
        da = DynamicArray([1,2,3,4,5,6])
        da.remove_at_index(3)
        self.assertEqual(da._data[3],5)
        with self.assertRaises(DynamicArrayException):
            da.remove_at_index(-1)
        with self.assertRaises(DynamicArrayException):
            da.remove_at_index(8)
        self.assertEqual(da._data[0],1)
        self.assertEqual(da._data[1],2)
        self.assertEqual(da._data[2],3)
        self.assertEqual(da._data[4],6)
        self.assertEqual(da._data[5],None)
        self.assertEqual(da._data[6],None)
        self.assertEqual(da._data[7],None)
        self.assertEqual(da._size,5)
        self.assertEqual(da._capacity,8)
        da.remove_at_index(0)
        da.remove_at_index(0)
        da.remove_at_index(0)
        da.remove_at_index(0)
        self.assertEqual(da._size,1)
        self.assertEqual(da._capacity,8)

        da2 = DynamicArray ( [10, 20, 30, 40, 50, 60, 70, 80] )
        da2.remove_at_index ( 0 )
        da2.remove_at_index ( 6 )

        da2.remove_at_index ( 2 )
        with self.assertRaises(DynamicArrayException):
            da2.get_at_index(6)
        self.assertEqual(da2.get_at_index(1),30)
        da3 = DynamicArray()
        for i in range ( 17 ):
            da3.insert_at_index ( i, i )
        self.assertEqual(da3.get_at_index(14),14)
        for i in range ( 16, -1, -1 ):
            da.remove_at_index ( 0 )

        da4 = DynamicArray ()
        [da4.append ( 1 ) for i in range ( 100 )]  # step 1 - add 100 elements
        self.assertEqual(da4.length(),100)
        self.assertEqual(da4.get_capacity(),128)
        [da4.remove_at_index ( 0 ) for i in range ( 68 )]  # step 2 - remove 68 elements

        self.assertEqual(da4.length(),32)
        self.assertEqual(da4.get_capacity(),128)
        da4.remove_at_index ( 0 )  # step 3 - remove 1 element
        self.assertEqual(da4.length(),31)
        self.assertEqual(da4.get_capacity(),128)
        da4.remove_at_index ( 0 )  # step 4 - remove 1 element
        self.assertEqual(da4.length(),30)
        self.assertEqual(da4.get_capacity(),62)
        [da4.remove_at_index ( 0 ) for i in range ( 14 )]  # step 5 - remove 14 elements
        self.assertEqual(da4.length(),16)
        self.assertEqual(da4.get_capacity(),62)
        da4.remove_at_index ( 0 )  # step 6 - remove 1 element
        self.assertEqual(da4.length(),15)
        self.assertEqual(da4.get_capacity(),62)
        da4.remove_at_index ( 0 )  # step 7 - remove 1 element
        self.assertEqual(da4.length(),14)
        self.assertEqual(da4.get_capacity(),30)

        da5 = DynamicArray ( [1, 2, 3, 4, 5] )
        for num in range ( 4 ):
            da5.remove_at_index ( 0 )
            self.assertEqual(da5._data[0],num+2)
        da5.remove_at_index(0)
        self.assertEqual(da5._data[0],None)

    def test_slice(self):
        da = DynamicArray ( [1, 2, 3, 4, 5, 6, 7, 8, 9] )
        da_slice = da.slice ( 1, 3 )
        self.assertEqual(da_slice[0],2)
        self.assertEqual(da_slice[1],3)
        self.assertEqual(da_slice[2],4)
        with self.assertRaises(DynamicArrayException):
            da_slice1 = da.slice(8,11)
        with self.assertRaises(DynamicArrayException):
            da_slice1 = da.slice(-1,3)
        with self.assertRaises(DynamicArrayException):
            da_slice1 = da.slice(9,3)
        with self.assertRaises(DynamicArrayException):
            da_slice1 = da.slice(1,20)
        with self.assertRaises(DynamicArrayException):
            da_slice1 = da.slice(0,9)
        da_slice2 = da.slice(0,8)
        self.assertEqual(da_slice2[7],8)
        self.assertEqual(da_slice2[6],7)
        self.assertEqual(da_slice2[5],6)
        self.assertEqual(da_slice2[4],5)
        self.assertEqual(da_slice2[3],4)
        self.assertEqual(da_slice2[2],3)
        self.assertEqual(da_slice2[1],2)
        self.assertEqual(da_slice2[0],1)
        da_slice.remove_at_index ( 0 )
        self.assertEqual(da_slice.get_at_index(0),3)
        da_slice3 = da.slice(1,8)
        self.assertEqual ( da_slice3[7], 9 )
        self.assertEqual ( da_slice3[6], 8 )
        self.assertEqual ( da_slice3[5], 7 )
        self.assertEqual ( da_slice3[4], 6 )
        self.assertEqual ( da_slice3[3], 5 )
        self.assertEqual ( da_slice3[2], 4 )
        self.assertEqual ( da_slice3[1], 3 )
        self.assertEqual ( da_slice3[0], 2 )

    def test_merge(self):
        da = DynamicArray ( [1, 2, 3, 4, 5] )
        da2 = DynamicArray ( [10, 11, 12, 13] )
        da.merge ( da2 )
        self.assertEqual(da._size,9)
        self.assertEqual(da._capacity,16)
        self.assertEqual(da._data[0],1)
        self.assertEqual ( da._data[1], 2 )
        self.assertEqual ( da._data[2], 3 )
        self.assertEqual ( da._data[3], 4 )
        self.assertEqual ( da._data[4], 5 )
        self.assertEqual ( da._data[5], 10 )
        self.assertEqual ( da._data[6], 11 )
        self.assertEqual ( da._data[7], 12 )
        self.assertEqual ( da._data[8], 13 )

        da1 = DynamicArray ( [1, 2, 3] )
        da4 = DynamicArray ()
        da5 = DynamicArray ()
        da1.merge ( da4 )
        self.assertEqual(da1._data[0],1)
        self.assertEqual(da1._data[1],2)
        self.assertEqual(da1._data[2],3)
        with self.assertRaises(DynamicArrayException):
            da1.get_at_index(3)
        da4.merge ( da5 )
        self.assertTrue(da4.is_empty())
        da5.merge ( da1 )
        self.assertTrue(da5._data,da1._data)

    def test_map(self):
        da = DynamicArray([1, 5, 10, 15, 20, 25])
        new_da = da.map(lambda x: (x ** 2))
        self.assertEqual(new_da._data[0],1)
        self.assertEqual(new_da._data[1],25)
        self.assertEqual(new_da._data[2],10**2)
        self.assertEqual(new_da._data[3],15**2)
        self.assertEqual(new_da._data[4],20**2)
        self.assertEqual(new_da._data[5],25**2)


    def test_filter(self):
        '''def filter_a(e):
            return e > 10

        da = DynamicArray ( [1, 5, 10, 15, 20, 25] )
        print ( da )
        result = da.filter ( filter_a )
        print ( result )
        print ( da.filter ( lambda x: (10 <= x <= 20) ) )

        def is_long_word(word, length):
            return len ( word ) > length

        da = DynamicArray ( "This is a sentence with some long words".split () )
        print ( da )
        for length in [3, 4, 7]:
            print ( da.filter ( lambda word: is_long_word ( word, length ) ) )'''

    def test_reduce(self):
        values = [100, 5, 10, 15, 20, 25]
        da = DynamicArray ( values )
        self.assertEqual(da.reduce ( lambda x, y: (x // 5 + y ** 2) ),714 )
        self.assertEqual(da.reduce ( lambda x, y: (x + y ** 2), -1 ), 11374 )
        da = DynamicArray ( [100] )
        self.assertEqual(da.reduce ( lambda x, y: x + y ** 2 ),100 )
        self.assertEqual(da.reduce ( lambda x, y: x + y ** 2, -1 ),9999 )
        da.remove_at_index ( 0 )
        self.assertEqual(da.reduce ( lambda x, y: x + y ** 2 ), None)
        self.assertEqual(da.reduce ( lambda x, y: x + y ** 2, -1 ),-1 )

    def test_find_mode(self):
        da = DynamicArray([1])
        self.assertEqual(find_mode(da)[1],1)
        self.assertEqual(find_mode(da)[0]._data[0],1)
        da.append(1)
        self.assertEqual(find_mode(da)[1],2)
        self.assertEqual(find_mode(da)[0]._data[0],1)
        da.append(2)
        da.append(2)
        self.assertEqual(find_mode(da)[1],2)
        self.assertEqual(find_mode(da)[0]._data[0],1)
        self.assertEqual(find_mode(da)[0]._data[1],2)
        da.append(3)
        self.assertEqual(find_mode(da)[1],2)
        self.assertEqual(find_mode(da)[0]._data[0],1)
        self.assertEqual(find_mode(da)[0]._data[1],2)
        for x in range(0,10):
            da.append(3)

        self.assertEqual(find_mode(da)[1],11)
        self.assertEqual(find_mode(da)[0]._data[0],3)
        for x in range(0,11):
            da.append(4)
        self.assertEqual(find_mode(da)[1],11)
        self.assertEqual(find_mode(da)[0]._data[0],3)
        self.assertEqual(find_mode(da)[0]._data[1],4)
        for x in range(0,11):
            da.insert_at_index(0,5)
        print(da)
        self.assertEqual ( find_mode ( da )[1], 11 )

        da10 = DynamicArray([4,4,4,2,2,1,1,3,3,3,6,6,6])
        self.assertEqual(find_mode(da10)[0]._data[0],4)
        self.assertEqual(find_mode(da10)[0]._data[1],3)
        self.assertEqual(find_mode(da10)[0]._data[2],6)
        self.assertEqual(find_mode(da10)[1],3)
        self.assertEqual ( find_mode ( da )[0]._data[1], 3 )
        self.assertEqual ( find_mode ( da )[0]._data[2], 4 )
        self.assertEqual(find_mode(da)[0]._data[0],5)


if __name__ == '__main__':
    unittest.main ()
