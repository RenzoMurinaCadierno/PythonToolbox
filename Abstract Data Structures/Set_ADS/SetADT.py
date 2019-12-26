class Set:
    """ 
    A Set Abstract Data Class built up around Python list data structure, 
    binary search and merge sort algorithms to emulate some basic functionalities 
    of Python's Set data structure. 
    It currently accepts integers and floats as values. Items are inserted and kept 
    in order at all times, which makes binary searching possible.
    I have made this one following Rance D. Necaise's proposed exercise in his
    'Data Structures and Algorithms using Python' book. Definitely worth checking
    it out, it has taught me lots.
    
    Methods:
        __init__
        __len__
        __contains__
        __iter__
        __eq__
        __str__
        add
        pop
        is_subset
        union
        intersection
        difference
        _get_idx_position : Helper method to get the index position of a value.

    Subclasses:
        _SetIterator : A class to generate the iterator when __iter__ is called.
        """
   
    def __init__(self, *args):

        self._contents = list()
        if args:
            for arg in args:    # O(n) + O(1) == complete args trasversal + amortized
                self.add(arg)   # cost of list expansion.
        
    def __len__(self): 
        return len(self._contents) 
        
    def __contains__(self, value): 
        idx = self._get_idx_position(value)                       # O(log n) due to
        return idx < len(self) and self._contents[idx] == value   # binary search.

    def add(self, value):
        if value not in self: 
            idx = self._get_idx_position(value)
            self._contents.insert(idx, value) # O(log n) + O(1) == binary search +
                                              # amortized cost due to list expansion
                                              # on large values.
            
    def pop(self, value):
        assert value in self, "Value not in set."
        idx = self._get_idx_position(value)
        return self._contents.pop(idx)  # O(log n) + O(1) == binary search + amortized
                                        # cost due to list reduction on large values.

    def _get_idx_position(self, value) -> int:
        """ 
        Helper method to get the position of a value inside the Set.
        It applies the binary search algorithm to do so.
        
        Parameters:
            value (Int): A value to find inside self Set.

        Return:
            An integer corresponding to the index position where the
            value is or should be located
        """

        first_idx = 0
        last_idx = len(self) -1
        
        while first_idx <= last_idx: 

            middle_idx = (last_idx + first_idx) // 2 

            if self._contents[middle_idx] == value: 
                return middle_idx
                
            elif value < self._contents[middle_idx]: 
                last_idx = middle_idx - 1 

            else: 
                first_idx = middle_idx + 1 
                
        return first_idx   # O(log n) worst case, a binary search algorithm.
        
    def __eq__(self, other_set) -> bool: 
        
        if len(self) is not len(other_set): 
            return False 

        else:
            for i in range(len(self)): 

                if self._contents[i] is not other_set._contents[i]: 
                    return False 

            return True # O(n) worst case, when self has the same values as other_set.

    def is_subset(self, other_set) -> bool:
        """ 
        Checks if self is subset of the Set passed as a parameter.
        
        Parameters:
            other_set (Set): A set to evaluate if self is subset of.

        Return:
            True is self is subset of other_set. False otherwise.
        """

        assert len(self) <= len(other_set), \
            "Target set is larger than compared set."

        a = 0
        b = 0

        while b < len(other_set):

            if other_set._contents[b] == self._contents[a]:
                a += 1
                if len(self._contents) == a:
                    break

            elif other_set._contents[b] > self._contents[a]:
                return False

            b += 1

        if self._contents[a-1] < other_set._contents[b-1]:
            return False
            
        return True  # O(n) worst case, when self has the same values as other_set.
 
        # for value in self : 
        #     if value not in other_set: 
        #         return False
        #     return True        # O(n^2) worst case, when both sets hold n values.
            
    def union(self, other_set):
        """ 
        Returns a new set composed by the union between this set and the one
        passed as a parameter.
        It uses the merge sort algorithm to do so.
        
        Parameters:
            other_set (Set): A set to evaluate the union with self.
        """
        
        merged_set = Set()
        a = 0
        b = 0

        while a < len(self) and b < len(other_set):

            if self._contents[a] < other_set._contents[b]: 
                merged_set._contents.append(self._contents[a]) 
                a += 1

            elif self._contents[a] > other_set._contents[b]: 
                merged_set._contents.append(other_set._contents[b]) 
                b += 1

            else :
                merged_set._contents.append(self._contents[a]) 
                a += 1 
                b += 1
                
        while a < len(self): 
            merged_set._contents.append(self._contents[a]) 
            a += 1 
        
        while b < len(other_set): 
            merged_set._contents.append(other_set._contents[b]) 
            b += 1
            
        return merged_set  # O(2n) worst case assuming both sets hold n values.
        
    def intersection(self, other_set): 
        """ 
        Returns a new set composed by the intersection between this
        set and the one passed as a parameter.
        It uses the merge sort algorithm to do so.
        
        Parameters:
            other_set (Set): A set to evaluate the intersection with self.
        """

        set_intersection = Set()
        a = 0
        b = 0

        while a < len(self) and b < len(other_set):

            if self._contents[a] < other_set._contents[b]: 
                a += 1

            elif self._contents[a] > other_set._contents[b]: 
                b += 1

            else:
                set_intersection._contents.append(other_set._contents[b])  
                a += 1 
                b += 1
            
        return set_intersection  # O(2n) worst case assuming both sets hold n values.
        
    def difference(self, other_set):
        """ 
        Returns a new set composed by the difference between this
        set and the one passed as a parameter.
        It uses the merge sort algorithm to do so.
        
        Parameters:
            other_set (Set): A set to evaluate the difference against self.              self.
        """

        set_diff = Set()
        a = 0
        b = 0

        while a < len(self) and b < len(other_set):

            if self._contents[a] < other_set._contents[b]: 
                set_diff._contents.append(self._contents[a]) 
                a += 1

            elif self._contents[a] > other_set._contents[b]: 
                set_diff._contents.append(other_set._contents[b]) 
                b += 1

            else:
                a += 1 
                b += 1

        while a < len(self): 
            set_diff._contents.append(self._contents[a]) 
            a += 1 
        
        while b < len(other_set): 
            set_diff._contents.append(other_set._contents[b]) 
            b += 1
            
        return set_diff   # O(2n) worst case assuming both sets hold n values.

    def __str__(self):
        a = "{"

        for i in range(len(self)):
            if i == len(self) - 1:
                a += f'{self._contents[i]}\u007d'
                break
            a += f"{self._contents[i]}, "

        return a                        # O(n) time but displays as set

        # return str(self._contents)    # O(1) time but displays as list
        
    def __iter__(self): 
        return self._SetIterator(self._contents)

    class _SetIterator():
        """ An private Class used by Set's __iter__ method to generate the iterable"""

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
                raise StopIteration     # O(n) worst case, complete list trasversal


if __name__ == '__main__':

    # Test the functionality by uncommenting the lines down below

    a = Set(5,8,6,6.5,7,4)
    b = Set(5,7,6,2,8,9,2,5,10,6,1,3,4,10)

    # print("A:", a, "B:", b)           # __str__

    # print(a == b)                     # __eq__

    # print(2 in a, 5 in a)             # __contains__

    # print(len(a))                     # __len__

    # a.add(2); print(a)                # add

    # c = a.pop(5); print(a); print(c)  # pop (assigning value to variable)
    # a.pop65); print(a);               # pop (not assigning value to variable)

    # print(a.is_subset(b))             # is_subset

    # print(a.union(b))                 # union

    # print(a.intersection(b))          # intersection

    # print(a.difference(b))            # difference

    # for i in a:                       # __iter__
    #     print(i)