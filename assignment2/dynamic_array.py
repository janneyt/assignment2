# Name: Ted Janney
# OSU Email: janneyt@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 2
# Due Date: 26/04/2022
# Description: Dynamic (resizing) array implementation


from static_array import StaticArray


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the capacity of the array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    def print_da_variables(self) -> None:
        """
        Print information contained in the dynamic array.
        Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        """
        Changes the capacity of an array by doubling its capacity.

        Returns the resized Dynamic Array and new Static Array
        """

        if type(new_capacity) is int and new_capacity > 0 and new_capacity > self._size:
            self._capacity = new_capacity
            old_data = self._data
            self._data = StaticArray(new_capacity)
            for values in range(0,new_capacity-1):

                # Frequently the old_data is too short so we have to insert Nones
                if values >= old_data.length():
                    self._data[values] = None
                else:
                    self._data[values] = old_data[values]
        elif type(new_capacity) is int and new_capacity == 0 and self._size == 0:
            self._capacity = new_capacity
            self._data = StaticArray(1)
        else:
            raise DynamicArrayException

    def append(self, value: object) -> None:
        """
        Adds a value to the end of the DynamicArray

        Returns None unless there is an error thrown
        """

        # If append was called as part of the __init__ method the size will not be accurate
        if self._size <= 0 and self._data[0] is not None:
            self._size = self._data.length()

        # If append was called as part of the __init__ method the capacity will not be accurate
        while(self._size >= self.get_capacity()):

            # I always resize to twice current capacity per the exploration
            self.resize(2*self.get_capacity())

        self._data[self._size] = value
        self._size += 1


    def insert_at_index(self, index: int, value: object) -> None:
        """
        Inserts a given value at a given index, after shifting values after that index to the right

        Ex. self._data = [1,2]
        self.insert_at_index(1,3)
        self._data = [1,3,2]

        No return, changes the array in place
        """
        # Weed out bad indices
        if index < 0 or index > self._size:
            raise DynamicArrayException

        # Finally update the size (capacity's already been updated)
        self._size += 1

        # Check the capacity before adding an element
        if self._capacity <= self._size:
            self.resize(2*self._capacity)
        if self._size < 1 and index == 0:
            self[index] = value
        else:
            # Use helper function to control inserting of values
            self.restore_values(index, 1, value)



    def restore_values(self, index: int, direction: int, value = None) -> None:
        """
        Helper function that resets the values after a given index
        """
        if type(direction) is int and direction < 0:

            # Switch variables in range (index,N-1) to avoid index bounds problems
            for num in range ( index, self._data.length () - 1 ):
                self._data[num] = self._data[num + 1]

            self._data[self._data.length()-1] = None
        elif type(direction) is int and direction > 0:
            # Use a temp variable to move items in place
            temp = self._data[index]
            change = value

            # Switch variables in range (index,N-1) to avoid index bounds problems
            for num in range ( index, self._data.length () - 1 ):
                self._data[num] = change
                change = temp
                temp = self._data[num + 1]

            # Finish the last value's switch for index reasons
            self._data[num + 1] = change

    def remove_at_index(self, index: int) -> None:
        """
        Removes a value at an index and, if necessary, resizes the array
        """
        if index < 0 or index >= self._data.length():
            raise DynamicArrayException

        # Since resizing is required to happen before value deletion, we need the < operator and not <=
        # so that capacity is set to old size * 2
        if self._size < 0.25*(self._capacity) and self._size > 10:
            self.resize(2*self._size)
        self.restore_values(index, -1)

        # Prevent overrun
        if self._size > 0:
            self._size -= 1




    def slice(self, start_index: int, size: int) -> "DynamicArray":
        """
        Returns a slice of an array between a start index and the computed end index (derived from the size parameter)

        Returns a new Dynamic Array containing the values of that slice
        """
        end = start_index + size



        # Parameters as specified in assignment, with end filling in for a size that is too large
        if start_index in range(0,self._size-1) and size in range(0,self._size) and end <= self._size:

            # Temp index for iterating
            index = start_index
            new_da = DynamicArray()

            # Advance temp index up the original array and append values to the new dynamic array
            while(index < end):
                new_da.append(self._data[index])
                index += 1
            return new_da
        raise DynamicArrayException

    def merge(self, second_da: "DynamicArray") -> None:
        """
        Takes a second array and appends it to the current array (does not sort)
        """
        # Weed out improperly sized dynamic arrays
        if second_da._size >= 0 and self._size >=0:
            for num in range(0, second_da.length()):

                # Skip None values (derived from the behavior in the assignment)
                if second_da[num] is not None:

                    # Append will handle all capacity resizing needed.
                    self.append ( second_da[num] )

    def map(self, map_func) -> "DynamicArray":
        """
        Maps a passed function that is applied to the Dynamic Array
        """
        new_da = DynamicArray()
        for num in range(0,self.length()):
            new_da.append(map_func(self._data[num]))
        return new_da

    def filter(self, filter_func) -> "DynamicArray":
        """
        Runs a filter and returns only those values for which the filter function returns true
        """
        true_da = DynamicArray()
        for num in range(0,self.length()):
            if filter_func(self._data[num]):
                true_da.append(self._data[num])
        return true_da

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        Takes the passed function and applies to all elements of the DynamicArray

        The initializer is an optional first step (like the first two terms of the Fibonacci sequence
        """

        if initializer is not None:
            base = initializer
            initial = 0
        else:
            base = self._data[0]
            initial = 1

        # We have to use the initial step because with an initializer, the range should be from 0, but without
        # it is from 1
        for num in range(initial,self.length()):
            base = reduce_func(base,self._data[num])

        return base



def find_mode(arr: DynamicArray) -> (DynamicArray, int):
    """
    Finds the most frequently occurring value(s) in a dynamic array and returns tuple containing:
        a Dynamic Array with all values
        the frequency of those values

    Returns a tuple
    """
    new_da = DynamicArray()

    # Set frequency and the counter to 1 since arrays passed to method are always at least length 1
    frequency = 1
    counter = 1
    current = arr[0]

    # Easier and more optimized than recounting arr.length() all the time
    end_point = arr.length()

    # Special case where the array is only a single element long
    if end_point == 1:
        new_da.append ( arr[0] )
        return (new_da, frequency)

    for num in range(1,end_point):

        # This is the main replacement logic when the counter exceeds the frequency
        if arr[num] != current and counter > frequency:

            while(not new_da.is_empty()):
                new_da.remove_at_index(0)

            # It's the *old* value being added, not the new one
            new_da.append(arr[num-1])
            current = arr[num]

            # We have a new frequency due to a replacement (not an addition) so this is the new high watermark
            frequency = counter

            # Reset to 1 for next value
            counter = 1

        elif arr[num] != current and counter == frequency:

            # This is the addition logic, i.e. when we have found another iteration of the current prevailing frequency
            current = arr[num]
            new_da.append(arr[num-1])
            counter = 1

        elif arr[num] != current:

            # This is a sort of default case when the new counter is not a candidate for inclusion but we have to
            # reset some things.
            current = arr[num]
            counter = 1

        elif arr[num] == current and counter > frequency:

            # Update frequency and counter. This would be used for the first "peak" or subsequent peaks when a
            # value has a new high frequency not at the junction with other values
            counter += 1
            frequency = counter


        elif arr[num] == current:

            # Default case for values are the same
            counter += 1

    # We can't use endpoint to index due to index out of bounds errors so we need to have special case processing
    # That respects the end_point value case where the final value should be included
    if counter > frequency:
        while (not new_da.is_empty ()):
            new_da.remove_at_index ( 0 )
        new_da.append(arr[end_point-1])
        frequency = counter
    elif counter == frequency:
        new_da.append(arr[end_point-1])


    return (new_da,frequency)


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()

    # print dynamic array's size, capacity and the contents
    # of the underlying static array (data)
    da.print_da_variables()
    da.resize(8)
    da.print_da_variables()
    da.resize(2)
    da.print_da_variables()
    da.resize(0)
    da.print_da_variables()

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)


    print("\n# append - example 1")
    da = DynamicArray()
    da.print_da_variables()
    da.append(1)
    da.print_da_variables()
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.length())
    print(da.get_capacity())

    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.length(), da.get_capacity())
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.length(), da.get_capacity())
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.length(), da.get_capacity())

    for i in range(14):
        print("Before remove_at_index(): ", da.length(), da.get_capacity(), end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.length(), da.get_capacity())

    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)

    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")

    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)

    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2


    def square(value):
        return value ** 2


    def cube(value):
        return value ** 3


    def plus_one(value):
        return value + 1


    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))

    print("\n# filter example 1")


    def filter_a(e):
        return e > 10


    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))

    print("\n# filter example 2")


    def is_long_word(word, length):
        return len(word) > length


    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))

    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: (x // 5 + y ** 2)))
    print(da.reduce(lambda x, y: (x + y ** 2), -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    print("\n# find_mode - example 1")
    test_cases = (
        [1, 1, 2, 3, 3, 4],
        [1, 2, 3, 4, 5],
        ["Apple", "Banana", "Banana", "Carrot", "Carrot",
         "Date", "Date", "Date", "Eggplant", "Eggplant", "Eggplant",
         "Fig", "Fig", "Grape"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")

    case = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    da = DynamicArray()
    for x in range(len(case)):
        da.append(case[x])
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}")
