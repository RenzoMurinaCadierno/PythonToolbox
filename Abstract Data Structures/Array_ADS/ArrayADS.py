import ctypes

class Array:
    """ 
    A C Array class emulated in Python using ctypes module.

    It is basically a fixed-size Python list that can be constructed either
    passing an integer as the size, or the values it will store in a list.

    I have made this one following Rance D. Necaise's proposed exercise in his
    'Data Structures and Algorithms using Python' book. Definitely worth checking it out, it has taught me lots.
    
    Methods:
        __init__
        __len__
        __getitem__
        __setitem__
        __iter__
        __contains__
        __eq__
        __str__
        fill : Changes each array value to the value passed as a parameter.
        clear : Changes each array value None.
        
    Subclasses:
        _ArrayIterator : A class to generate the iterator when __iter__ is called.
    """

    def __init__(self, size_or_values=[]):
        """ 
        Initializes the list. Either integer representing the size of the
        array or a list containing the initial values must be passed as an
        argument. Otherwise, the proper error will be risen.

        Efficiency is O(n) at worse time, where n is len(size_or_values).

        Attributes:
            self._length (int) : The size of the Array.
            self._values (any) : The array itself holding its values.
        """

        # Initialization conditions
        if not size_or_values:
            raise TypeError("Must provide the size as an int > 0 or pass the Array's values in a non-empty list.")
        elif type(size_or_values) is float:
            raise TypeError("Must provide the size as an int.")
        elif type(size_or_values) == int:
            self._length = size_or_values
        elif type(size_or_values) == list:
            self._length = len(size_or_values)
        else:
            raise TypeError('Values must be passed inside a list.')
        
        # C-to-Python object linking
        C_to_Py_Array =  self._length * ctypes.py_object
        self._values = C_to_Py_Array()

        # If the size was passed as an int, fill the array with None
        if type(size_or_values) == int:
            self.fill(None)

        # Otherwise, fill the array with the values in size_or_values list
        else:
            for i in range(self._length):
                self._values[i] = size_or_values[i]

    def __len__(self):
        return self._length
        
    def __getitem__(self, idx):
        assert idx >= 0 and idx < len(self._values), "Index out of range."
        return self._values[idx]        # O(1) worse time, direct access.

    def __setitem__(self, idx, value):
        assert idx >= 0 and idx < len(self._values), "Index out of range."
        self._values[idx] = value       # O(1) worse time, direct insertion.

    def __iter__(self):
        return self._ArrayIterator(self._values)

    def __contains__(self, value):
        for i in range(len(self)):
            if i == value:
                return True
        return False                    # O(n) worse time, full trasversal.

    def __eq__(self, other_arr):
        """ 
        Returns True only if both arrays have the same values in the
        same order.
        """
        assert len(self) == len(other_arr), "Both arrays' length must be equal."

        for i in range(len(self)):
            if self._values[i] is not other_arr._values[i]:
                return False
        return True                     # O(n) worse time, full trasversal.

    def __str__(self):
        string = '|'

        for i in range(len(self)):
            if i == len(self) -1:
                string += f'{ str(self._values[i])}|'
                break
            string += f'{ self._values[i]}, '

        return string                   # O(n) worse time, full trasversal.

    def fill(self, value):
        """ 
        Changes each array value to the value passed as a parameter. 
        """
        for i in range(len(self)):
            self._values[i] = value     # O(n) worse time, full trasversal.

    def clear(self):
        """ 
        Changes each array value to None. 
        """
        self.fill(None)                 # O(n) worse time, full trasversal.

    class _ArrayIterator:

        def __init__(self, arr): 
            self._arr = arr 
            self._idx = 0 
            
        def __iter__(self): 
            return self
        
        def __next__(self): 
            if self._idx < len(self._arr): 
                current_value = self._arr[self._idx] 
                self._idx += 1 
                return current_value 
            else: 
                raise StopIteration     # O(n) worse time, full iteration


a = Array(6)
b = Array([1, None, [1,2], {'a': 1, 1 : 'a'}, True, "Testing"])

# print(a)                        # __str__
# print(b)                

# print(len(b))                   # __len__

# print(b[3])                     # __getitem__

# b[3]='Modified!'; print(b)      # __setitem__

# for i in b: print(i)            # __iter__

# print(1 in b)                   # __contains__

# print(a == b)                   # __eq__

# b.fill('Full'); print(b)        # fill

# b.clear(); print(b)             # clear

# b.append('Error!')              # ERROR! Array size is fixed once constructed

# b.pop()                         # ERROR! Array size is fixed once constructed