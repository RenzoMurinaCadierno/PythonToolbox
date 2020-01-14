from modules.array import Array

class MDArray:
    """
    A limitless (of course, if your device can handle the storage) multidimensional
    array, represented by a flat 1-Dimensional Array.

    MDArray takes any number of dimension grades and coefficients and inserts all of
    its initial values inside a single Array. To access the values of each specific
    dimension, the iterator skips each dimension or elements inside the target
    subdimension using factors, which are no more than their coefficient times their
    grade.

    Everything is explained on each method, so feel free to check them out. You are
    able to use this class to instantiate 2-D Arrays (like a normal matrix), up to 
    n-D Arrays. Down below in __main__ I've presented several examples for you to
    test out. Those involve three and five dimensional arrays just for the sake of
    comprehension. Once you get the grasp of it, try creating examples on higher 
    dimensions, like 7-D, 10-D, 30-D, 100-D, or whatever you like. Just keep in mind
    that, like in real life, 4-D and higher dimensions are harder to visualize, so
    have a good understanding of pprint() before attempting higher grades.

    You can target the MDArray as a whole, complete dimensions, specific subdimensions
    (like the first 2nd dimension inside the fourth 3rd dimension inside the second
    5th dimension, for example), or even individual elements. You can change single
    values inside a dimension, or whole dimensions. Compare MDArrays, generate hiper-
    specific iterators, index elements by their flat MDArray access index and by
    their dimensional representation indexes, and more. Go, the world is yours. 

    Methods:
        __init__
        __contains__
        __eq__
        __del__
        __iter__
        __len__
        __setitem__
        __getitem__
        get_max_dim_grade
        get_dim_repr
        get_dim_coefficients
        get_dim_iterator
        clone
        indexOf
        clear_all
        clear_dim
        fill_all
        fill_dim
        indexify
        pprint
        fprint
    
    Helper methods:
        _direct_idx
        _get_factors
        _get_iterable
        _get_start_end_values
        _is_valid_idx
        _rise_exception
        _write_values

    Meta classes:
        _MDArrayIterator

    Author: Renzo Nahuel Murina Cadierno
    Contact: nmcadierno@hotmail.com
    Github: https://github.com/RenzoMurinaCadierno
    """

    def __init__(self, *args):
        
        # Only 2-D+ dimensions are accepted. For 1-D, use the Array class.
        if len(args) < 2:
            raise ValueError('MDArray only supports 2 or more dimensions.')

        # Calculate the length of the MDArray (MDArray's number of values)
        dims = 1

        for arg in args:
            assert type(arg) is int, \
                'Dimensions can only be expressed as integer values.'
            dims *= arg
        
        self._dim_repr = Array(dims)    # The array that holds all values
        self._dim_values = Array(args)  # An array to hold the dimension coefficients
        self._dim_values.reverse()      # Reversed. We process them from bottom up
        self._factors = self._get_factors() # And an array to hold all dimension factors

    def __contains__(self, value):
        for i in self:

            if i == value:
                return True
        
        return False

    def __eq__(self, mdarray):
        if len(mdarray) != len(self):
            return False  

        for i in range(len(self)):
            if self.get_dim_repr()[i] != mdarray.get_dim_repr()[i]:
                return False
        
        return True

    def __del__(self):
        self = None

    def __iter__(self):
        return self._MDArrayIterator(self.get_dim_repr())

    def __len__(self):
        return len(self._dim_repr)

    def __str__(self):
        return self._dim_repr.__str__()

    def __getitem__(self, idx_tuple):
        if self._is_valid_idx(idx_tuple, none_enabled=False):
            return self.get_dim_repr()[self._direct_idx(idx_tuple)]

    def __setitem__(self, *args):
        if self._is_valid_idx(args[0], none_enabled=False):
            self.get_dim_repr()[self._direct_idx(args[0])] = args[1]

    def get_max_dim_grade(self) -> int:
        """
        Returns the maximum dimension grade of the MDArray. That is, the
        number of parameters passed to it when it was constructed.
        """
        return len(self._dim_values)

    def get_dim_repr(self):
        """
        Returns the flat representation of the MDArray, that is a 1-dimensional
        array conposed of all of MDArray values.
        """
        return self._dim_repr

    def get_dim_coefficients(self):
        """
        Returns an Array with the coefficient values of each dimension grade
        in the MDArray. In other words, the parameters passed to it when it
        was constructed.
        """
        return self._dim_values

    def get_dim_iterator(self, *args):
        """
        Takes a valid dimensional index, generates and returns an iterator
        object containing all members of that dimension.

        args:
            A number of int or None elements representing the indexes of the 
            specific dimension that is to be iterated.

            Integers in args cannot be less than 0 or higher than its corresponding 
            dimension coefficient. None is accepted as a valid index. Dimensions 
            with None values coming before an index set as an int will not be 
            considered, but the ones coming after will be included as a whole.

            E.g.: Given an MDArray 'x' size (3,2,1,4,5):
            x.get_dim_iterator(0,None,None,None,None) will create and return 
                an instance of MDArrayIterator with the members of the first 5th 
                dimension (which includes all of its subdimensions).
            x.get_dim_iterator((None,1,None,2,None) will create and return
                an instance of MDArrayIterator with the members of the third 2nd 
                dimension of the second 4th dimension.
        """
        if not args or args == tuple([None for _ in args]):
            return self.__iter__()
        
        iterable = self._get_iterable(args)      
        return self._MDArrayIterator(iterable)

    def clone(self):
        """
        Creates and returns a new MDArray instance with the same length as
        self, its same values, dimensions and factors.
        """
        clone = MDArray(*[i for i in self.get_dim_coefficients()])
        clone._dim_repr = self._dim_repr.clone()
        clone._dim_values = self._dim_values.clone()
        clone._factors = self._factors.clone()
        return clone

    def indexOf(self, value, **kwargs) -> list:
        """
        Finds the 1D MDArray index(es) and the dimensional index(es) of the
        value passed as parameter, and returns them as a tuple.

        Parameters:
            value (any): The value to search for in the MDArray.
        
        kwargs:
            lazy (bool): If True, then as soon as an element matches the
                search, it will stop looking for more. On False, the method
                will look for all matching values.
        
        Returns:
            (list): A list containing all tuples with the flat 1D MDArray
                index and the dimensional index of all matching elements.
                Or a list with a single tuple if 'lazy' is True.
        """
        elements = {}
        factors = self._factors.clone()
        factors.reverse()
        lazy = False

        # set lazy to True if it was specified in kwargs
        if kwargs:
            if kwargs['lazy'] is True:
                lazy = True

        # for each value in the MDArray, if it matches the one passed as
        # a parameter, add a new key and a value to elements dictionary,
        # both equal to the flat index where it was found.
        # If lazy=True, then as soon as there is one match, stop searching.
        for dir_idx, val in enumerate(self.get_dim_repr()):
            if val == value:
                elements[dir_idx] = dir_idx
                if lazy:
                    break
        
        if not elements:
            return None
        
        idx_list = []

        # for each key in the dictionary that holds all matching indexes
        for dir_idx in elements.keys():
            dim_idx = ""

            # perform an integer division between the key's value (flat index) 
            # and the MDArray factor (starting from the max dimension grade's 
            # factor). Concatenate the result as a string to dim_idx and perform 
            # a modulo operation with those same operands, which will set the
            # flat_index's remainder to be analized by the next factor and so on.
            # Each operation will append an int representing the dimensional
            # index representation of the flat index, and we do so as a string
            # so as to be able to access it by [] indexing notation later on.
            for curr_factor in factors:
                dim_idx += str(elements[dir_idx] // curr_factor)
                elements[dir_idx] = elements[dir_idx] % curr_factor

            # Once you have the flat and dimensional indexes of the current
            # element's key, append both as a tuple to idx_list
            idx_list.append((dir_idx, dim_idx))

        # and return it
        return idx_list

    def clear_all(self):
        """
        Overwrites all MDArray's values with None.
        """
        self.fill_all(None, overwrite=True)

    def clear_dim(self, *args):
        """
        Takes a tuple with int or None elements representing the indexes
        of the specific dimension to clear and replaces all of its objects 
        with None.

        Integers in the idx_tuple cannot be less than 0 or higher than its
        corresponding dimension coefficient. None is accepted as a valid 
        index. Dimensions with None values coming before an index set as an 
        int will not be considered, but the ones coming after will be included
        as a whole.

        E.g.: Given an MDArray 'x' size (3,2,1,4,5):
        x.clear_dim(0,None,None,None,None) will set all members of the
            first 5th dimension (and all of its subdimensions) to None.
        x.clear_dim(None,1,None,2,None) will set all members of the
            third 2nd dimension of the second 4th dimension to None.

        Parameters:
            idx_tuple (tuple): A tuple with the dimensional index of the
                dimension to replace the values. Check the description and
                examples above for a better understanding.
        """
        if len(args) is self.get_max_dim_grade():
            return self.fill_dim(None, tuple(args))

        self._rise_exception('_get_start_end_values_0')

    def fill_all(self, value=None, **kwargs):
        """
        Replaces each value in the MDArray with the value passed as a 
        parameter.

        Parameters:
            value (any): The value to replace the elements with.
                Defaults to None.
        
        kwargs: 
            overwrite (boolean): True if all values are to be replaced, 
            False if only None values would be overriden. Defaults to True.
        """
        self._write_values(range(len(self)), value, **kwargs)

    def fill_dim(self, value, idx_tuple, **kwargs):
        """
        Takes a tuple with int or None elements representing the indexes
        of the specific dimension to fill up and replaces all of its objects 
        with the specified value.

        Integers in the idx_tuple cannot be less than 0 or higher than its
        corresponding dimension coefficient. None is accepted as a valid 
        index. Dimensions with None values coming before an index set as an 
        int will not be considered, but the ones coming after will be included
        as a whole.

        E.g.: Given an MDArray 'x' size (3,2,1,4,5):
        x.fill_dim("1", (0,None,None,None,None)) will fill all members of 
            the first 5th dimension (and all of its subdimensions) with
            a value of "1".
        x.fill_dim("2", (None,1,None,2,None)) will fill all members of the
            third 2nd dimension of the second 4th dimension with a value
            of "2".

        Parameters:
            value (any): The value to fill the dimension with.
            idx_tuple (tuple): A tuple with the dimensional index of the
                dimension to replace the values. Check the description and
                examples above for a better understanding.
        
        kwargs:
            overwrite (bool): if False, only None values will be overriden.
                On True, all values will.
        """
        if idx_tuple and idx_tuple == tuple([None for _ in idx_tuple]):
            return self.fill_all(value, **kwargs)

        start, end = self._get_start_end_values(idx_tuple)

        self._write_values(range(start, end), value, **kwargs)

    def indexify(self, replace_values=False):
        """
        Creates and returns new MDArray instance with the same flat length as
        self, assigning a tuple to each of its values containing their flat
        MDArray access index and dimensional index. If replace_values is False, 
        then the tuple will also include the value (it will not be overriden).

        Since this method is costly storage-and-speed wise (O(n^2) + O(n), and 
        requires MDArray cloning), the indexed result is returned, so that
        it can be used again if needed and if values were not modified since
        this last call. 
        
        Parameters:
            replace_values (bool): If False, each tuple will contain the value's
                flat MDArray index, its dimensional index and the value itself.
                If false, the MDArray will be filled up with tuples that contain
                the flat MDArray index and the dimensional index. Existing values
                will be overriden. This functionality serves as to 'mock' an MDArray
                for testing purposes.

        Returns:
            (MDArray): An MDArray with the same length as self, with each element
                in the form of a tuple, format: 
                    (flat_MDArray_access_index, dimensional_index, value)
        """
        dimensions = self.get_dim_coefficients().clone()
        dimensions.reverse()
        indexed_mda = MDArray(*[i for i in dimensions])

        for i, value in enumerate(indexed_mda.get_dim_repr()):

            # find the indexes, one by one. Lazy mode.
            indexes = indexed_mda.indexOf(value, lazy=True)

            # replace the MDArray respective value with a tuple containing the flat
            # access index and the dimensional index of that value. Replacing the
            # values this way is needed so that they do not intefere with indexOf 
            # calls on following iterations.
            indexed_mda.get_dim_repr()[i] = (indexes[0][0], indexes[0][1])
        
        # Do we want this tuple to replace the values only? If so, return the
        # cloned MDArray as it is.
        if replace_values: 
            return indexed_mda

        # We want to keep the original values as reference.
        for i, value in enumerate(self.get_dim_repr()):

            # For each value, replace the indexed tuple in the cloned MDArray with
            # a tuple containing the flat index, dimensional index and corresponding 
            # value.
            index = indexed_mda.get_dim_repr()[i][0], indexed_mda.get_dim_repr()[i][1], value
            indexed_mda.get_dim_repr()[i] = index

        # And return it.
        return indexed_mda

    def pprint(self, *args, **kwargs) -> list:
        """
        Prints out the MDArray in a more readable format than its __str__
        equivalent. The output will vary depending on the kwargs.

        args: A number of int or None values equal to self._get_max_dim_grade().
            Each int cannot be less than zero or higher than its respective
            dimension coefficient. This arguments specify the dimension you want
            to print out. A value of None after an int will consider all members 
            of that subdimension. A value of None before the first int value
            will disregard that respective higher dimension.
            Empty args or full None values will print out all higher dimensions,
            thus, the whole MDArray.
            E.g.: Given a 5-dimensional array size (3,2,1,4,5):
                d.pprint() or d.pprint(None,None,None,None,None) will print the
                    whole MDArray (all 3 fifth dimensions)
                d.pprint(0,None,None,None,None) will print out all members of the
                    first fifth dimension (with all of its lower grade subdimensions).
                d.pprint(None,1,None,2,None) will print out all members of the
                    third 2nd dimension inside the second fourth dimension.

        kwargs:
            break_by_dimension (int): An int value representing the number of the
                dimension you want to break your results at on each print iteration.
                It has to be a dimension assigned as None in args, cannot be zero or
                lower, or higher than the last dimension with an int value (or higher
                than the higest dimension grade, if no int is assigned).
                E.g.: Given a 5-dimensional array size (3,2,1,4,5):
                    d.pprint(None,None,None,None,None, break_by_dimension=3) will
                        print out all members of the MDArray divided by their respective
                        third dimensions each.
                    d.pprint(None,1,None,None,None, break_by_dimension=2) will print
                    out all members of the second 4th dimension divided by their
                    corresponding 2nd dimensions.
                NOTE: Errors in [-break_by_dimension] are intentional!
            show_details (bool): If True, the MDArray dimension coefficients, factors,
                length and length of each of its subdimensions will be printed out, 
                as well as the specified dimension's (args') index and length.
            value_separator (str): What is used to separate each member being printed
                out. Defaults to ' - '. For better readability, '\n' is suggested.

        Returns:
            (list): A list containing all of the values of the dimension passed as
                args, or the whole MDArray values if no args are passed. This values
                are indexed in a tuple, format: (flat_index, dimensional_index, value).
        
        Keep in mind this operation is very costly. Not only it executes
        print() repeatedly, but it also requires a call to indexify(),
        which has a storage cost of 2x the __len__ of the MDA and an order
        of magnitude of (O(n^2) + O(n), where n is self.__len__()).
        Moreover, a linear iteration is also required to separate the 
        values by dimensions or to print them out as a whole.

        Though however, this method prints out the specified dimension in
        great detail, with its members in a tuple consisting of their flat
        MDArray access index, its dimensional index and value. It also divides
        the members on their respective dimension if you pass break_by_dimension
        as kwargs. Additionally, the specified dimension passed as args is
        returned as a list if there is a need to use it without calling other
        methods that do the same, or this same method again.
        """
        indexed_mda = self.indexify()
        dimensions = self.get_dim_coefficients().clone()
        factors = self._factors.clone()
        dimensions.reverse()
        factors.reverse()
        value_separator = ' - '
        break_by_dimension = None
        show_details = False

        # creates the respective iterable object to print and return the
        # values according to the passed args.
        if not args:
            args = tuple([None for _ in factors])
            iterable = indexed_mda.get_dim_repr()
        elif args == tuple([None for _ in factors]):
            iterable = indexed_mda.get_dim_repr()
        else:
            iterable = indexed_mda._get_iterable(args)

        # assigns values to the variables that depend on kwargs.
        if kwargs:
            if 'value_separator' in kwargs:
                value_separator = kwargs['value_separator'] if type(kwargs['value_separator']) is str else ' - '
            if 'break_by_dimension' in kwargs:
                break_by_dimension = kwargs['break_by_dimension'] if type(kwargs['break_by_dimension']) is int else None
                if (break_by_dimension <= 0 or break_by_dimension > len(args)) or args[-break_by_dimension]:
                    self._rise_exception('dprint_0')
            if 'show_details' in kwargs:
                show_details = True if kwargs['show_details'] else False

        print('-' * 80)

        # prints the dimension coefficients, factos, length and length of each
        # subdimension
        if show_details:
            print('MDArray dimension coefficients:', dimensions)
            print('\nMDArray factors:', factors)
            print('\nMDArray grade:', self.get_max_dim_grade())
            print('\nMDArray length:', len(self))
            print('\nLength of each subdimension grade:')
            print('\t> ', end='')

            for i, dim in enumerate(dimensions):
                if i is len(dimensions) - 1:
                    print(f'Dim {len(dimensions)-i}: {dim * factors[i]}')
                    break
                print(f'Dim {len(dimensions)-i}: {dim * factors[i]}', end=' - ')

            # prints the indexes of the specified dimension
            print('\nSpecified dimension index:')
            print('\t>', args, '\n\t> ', end='')
            
            for i, arg in enumerate(args):
                if i is len(args) - 1:
                    print(f'Dim {len(args)-i}: {arg}')
                    break
                print(f'Dim {len(args)-i}: {arg}', end=' - ')

            # prints the specified dimension's length
            print('\nSpecified dimension length:', len(iterable))
        
        print('\nSpecified dimension members:')

        # prints headers before iterating
        if break_by_dimension:
            print('\t> Header format: Subdimension index: (from highest assigned dimension to breakpoint subdimension).')
            print('\t> Member format: (flat_MDArray_index, dimensional_index, value).')
            print(f'\t> Breakpoints: separating members by each {break_by_dimension} subdimensions.', end='')
        else:
            print('\t> Member format: (flat_MDArray_index, dimensional_index, value).')
            print('\t> Breakpoints: none assigned to break_by_dimension kwarg. Displaying all members at once.', end='\n\n')
        
        dim_breakpoint = 0

        for i in range(len(iterable)):
            # Intentional errors here, if break_by_dimension holds a None value,
            # the exception will be caugth and no subdimension division will occurr.
            # This is the case when no break_by_dimension kwarg exists.
            try:
                # dim breakpoint will be compared to the respective dimensional index
                # when iterating. If break_by_dimension is 2 and the tuple is a 5 dimension
                # one (e.g. (3,1,2,4,3)), dim_breakpoint will go from 0 to 3 (max index 3
                # in 4th dimension). Each time the break_by_dimension index of the dimensional 
                # value of the current iteration matches dim_breakpoint, the subdimension
                # division will occur, and dim_breakpoint will be resetted to 0.
                if str(dim_breakpoint) == iterable[i][1][-break_by_dimension]:
                    print(
                        '\n\nSubdimension index:', 
                        iterable[i][1][:-break_by_dimension+1] if break_by_dimension != 1 else iterable[i][1]
                    )

                    dim_breakpoint += 1

                    if dim_breakpoint is dimensions[-break_by_dimension]:
                        dim_breakpoint = 0
            
            except TypeError:
                pass

            # At any case (with or without subdimensional division), prints the
            # current iterating value out.
            if i is len(iterable) -1:
                print(iterable[i])
                break

            print(iterable[i], end=value_separator)

        print('\n', '-' * 80)
        
        # return the whole iterable, if needed for anything later on.
        return iterable

    def fprint(self, *args) -> list:
        """
        A much faster but not as informative version of pprint().
        Prints out the values in the dimension specified by the index 
        in args -or all values in the MDArray if no args are passed-, 
        indexing them by the order they appear.

        Note that this index is NOT the flat MDArray access index for
        the value, much less its dimensional index. It is just an
        additional sorting method to aid the ordering if values are
        repeated.

        Integers in args cannot be less than 0 or higher than its 
        corresponding dimension coefficient. None is accepted as a valid 
        index. Dimensions with None values coming before an index set as an 
        int will not be considered, but the ones coming after will be 
        included as a whole.

        E.g.: Given an MDArray 'x' size (3,2,1,4,5):
        x.fprint(0,None,None,None,None) will print out all members of 
            the first 5th dimension (and all of its subdimensions).
        x.fprint(None,1,None,2,None) will print out all members of the
            third 2nd dimension of the second 4th dimension.

        Return:
            (list): The iterable list containing all values of the
                specified index.

        pprint()'s order of magnitud is n^2 + 2n. fprint() deals n + 2k, 
        where k is the highest dimension grade, or total amount of factors. 
        For both cases, n is the length of the flat MDArray, or total amount 
        of values inside the MDArray.
        """
        if not args:
            args = tuple([None for _ in self._factors])
            iterable = self.get_dim_repr()
        elif args == tuple([None for _ in self._factors]):
            iterable = self.get_dim_repr()
        else:
            iterable = self._get_iterable(args)

        for (i, value) in enumerate(iterable):
            print(i, "Value:", value)

        return iterable

    def _direct_idx(self, idx_tuple) -> int:
        """
        Multiplies each value of idx_tuple by its respective factor and
        adds the result up to get the direct flat index of the MDArray.

        Parameters:
            idx_tuple (tuple): Contains the index of each dimension to
                get to the element we want to access, in order from the 
                highest dimension to the lowest one. 
                E.g.: Given a three-dimensional MDArray size (4,3,2).
                To access the first element of the 1st dimension, of the 
                third 2nd dimension, of the second 3rd dimension, idx_tuple
                would be (1, 2, 0). 1 is the index of the second 3rd dimension,
                2 is the third 2nd dimension, and 0, the first 1st dimension.
        
        Returns:
            (int): The MDArray flat index to access that element directly.
        """
        array_idx = 0

        for i, idx in enumerate(idx_tuple[::-1]):
            array_idx += idx * self._factors[i]
        
        return array_idx

    def _get_iterable(self, args):
        """
        Given the dimensional index passed as args, it creates and returns a list
        object containing all members of the specified dimension given that index.

        To do so, it uses _is_valid_index to check if args is a correct dimensional
        index for self, _get_start_end_values to get the initial and final integers
        used to create the range of the list iterable of the given dimensional index,
        and a list comprehension to create such iterable.

        Feel free to check the commentaries on those two methods for more details.

        args:
            A number of int or None elements representing the indexes of the 
            specific dimension that is to be iterated. fprint() and pprint() explain
            in detail the requirements of args, which applies here too. Plase, do
            check those two methods for further instructions on how to construct args.
        """
        self._is_valid_idx(args, none_enabled=True)
        start, end = self._get_start_end_values(args)
        iterable = [self.get_dim_repr()[i] for i in range(start, end)]
        return iterable

    def _get_factors(self):
        """
        Calculates and returns an array containing the factors of each 
        dimension grade in the MDArray. The factors are the numbers to
        multiply and add when trying to reach to a specific dimension
        inside the flat Array that holds all values.

        The first factor is always 1, since to skip over elements in the
        targeted 1st grade dimension, you do so one by one.

        The second factor is the length of the 1st grade dimension, as 
        that is how you skip over those 1D as a whole from a higher 
        dimension: by its total length.

        Then for the following k dimensions, their factors are calculated
        multiplying the amount of their k-1 dimension factor by their k-1
        dimension coefficient.

        For example, an MDArray with size (5,4,3,2) will have:
            1 as the factor of the grade 1 coefficient 2 dimension,
            2 as the factor of the grade 2 coefficient 3 dimension,
            6 as the factor of the grade 3 coefficient 4 dimension,
            24 as the factor of the grade 4 coefficient 5 dimension.

        Leading to a return Array of |2, 3, 6, 24|, from lowest to highest
        dimension grade, which is later reversed in some methods that use 
        and deal with it as it is in some other methods. 
        """
        arr_of_factors = Array(self.get_max_dim_grade())
        current = 1
        arr_of_factors[0] = current
        arr_of_factors[1] = self.get_dim_coefficients()[0]

 
        for i in range(2, self.get_max_dim_grade()):
            current = arr_of_factors[i-1] * self.get_dim_coefficients()[i-1]
            arr_of_factors[i] = current

        return arr_of_factors

    def _get_start_end_values(self, idx_tuple) -> tuple:
        """
        Takes a tuple with the dimensional index pointing to a specific dimension and 
        returns a start and an end integer value to pass as parameters to range() so 
        as to iterate over that dimension inside the flat MDArray.

        Parameters:
            idx_tuple (tuple): A tuple with the dimensional index of the dimension to 
                evaluate to get its flat MDArray index boundaries.
                Integers and None values are accepted as a valid individual dimension 
                indexes but not all of those indexes can be None at the same time. If 
                a None value comes before the first int value, that dimension grade
                represented by None will be omitted. If it comes after a valid int
                individual value, then that None dimension is considered as a whole.
                Integers cannot be lower than 0 or higher than their respective
                dimension coefficient.

        Return:
            (tuple): A tuple containing the start and end position values to use in a
                range function to iterate over that specific dimension insde the flat
                1D MDArray.

        E.g.: Given an MDArray 'x' size (3,3,2,4,5):
            x._get_start_end_values((1,None,None,None,None)) will return (120, 240),
                since each one of the 3 coefficients of the fifth dimension have a 
                factor of 120. We are looking for index 1, the 2nd fifth dimension
                (all None values are disregarded since they come after the first int
                value: 1). Index 0 goes from 0 to 120, index 1 is 120-240, index 3,
                240-360. Applying range(120, 240) will lead us to the 2nd fifth dim.
            x._get_start_end_values((2,None,1,None,None)), will look for the start
                and end values of the second 3rd subdimension inside the 3rd fifth
                dimension. Dimension 5 has a factor of 120, and dimension 3, 20.
                120*2 + 20*1 gives us the starting point, which is 260. Ending point
                of that subdimension is that number plus its lowest subdimension 
                value, 20. Which leads to the tuple (260, 280). range(260, 280) is
                the flat MDArray index of that particular dimension. 
        """
        assert len(idx_tuple) is len(self._factors), \
            self._rise_exception('_get_start_end_values_0')

        start = 0
        one_factor_end = 0
        specific_end = 0
        idx_tuple = idx_tuple[::-1]         # we need the highest values up front

        for i, idx in enumerate(idx_tuple):
            if idx is None:                 # disregard None values
               continue

            # if the current int index is a valid one for the subdimension
            elif type(idx) is int and idx < self.get_dim_coefficients()[i]:

                # if that index is 0, we need to start counting from dimension 0,
                # on any subdimensional index. So, start is set to 0.
                if idx == 0 and not start:
                    start = 0

                # Otherwise, the beginning point is that subdimensional index
                # times its respective dimension factor to skip in the MDArray,
                # which adds up in a same fashion for each found index that is
                # a valid integer.
                else:
                    start = start + idx * self._factors[i]
                
                # Save the first found integer's respective dimensional factor.
                # End point will be that factor + start if only one integer is
                # passed to idx_tuple, and all other values are None.
                if not specific_end:
                    specific_end = self._factors[i]

                # Calculate the End point to be the current sum of all found
                # indexes times their respective dimension's factor, plus the
                # factor of the current (lowest) found int index.
                one_factor_end = start + self._factors[i]

            # int index is a valid one? Rise exception if it is not.
            elif type(idx) is int and idx >= self.get_dim_coefficients()[i]:
                self._rise_exception('_get_start_end_values_2')

        # End point is start + specific_end (only int index set as start + its
        # factor) if all indexes in idx_tuples but one were None values.
        # Otherwise, end is the addition of all int indexes multiplied by their
        # factors + the last found index's corresponding factor.
        end = start + specific_end if specific_end else one_factor_end
        
        # There has to be at least one end point. The one available at all cases
        # is one_factor_end (always set no matter what). If it is not there (All
        # None values), then rise exception.
        if not one_factor_end:
            self._rise_exception('_get_start_end_values_1')

        # Indexes found, return a tuple with them
        return start, end

    def _is_valid_idx(self, idx_tuple, **kwargs) -> bool:
        """
        Checks if the dimensional index passed as idx_tuple is a valid one
        according to the MDArray's dimension grade and its individual
        coefficients.

        args:
            idx_tuple (tuple): A tuple with the dimensional index of the
                dimension to validate. Integers in idx_tuple cannot be less 
                than 0 or higher than its corresponding dimension coefficient. 
                If kwargs['none_enabled'] is True, then None is accepted as a 
                valid individual index. Dimensions with None values coming 
                before an individual index set as an int will not be considered, 
                but the ones coming after will be included as a whole.

                E.g.: Given an MDArray 'x' size (3,2,1,4,5):
                    x._is_valid_idx(None,1,None,2,None, none_enabled=True) will 
                        return True since index 1 in the fourth dimension is less 
                        than its coefficient 2, and index 2 in the second dimension 
                        is less than less than its coefficient 4. Both are higher
                        than 0, and None values are allowed because of kwarg.
                    x._is_valid_idx(None,2,None,2,None, none_enabled=False) will
                        return False since index 2 in the fourth dimension is equal
                        than its coefficient, and None is not allowed due to kwarg.
        
        kwargs:
            none_enabled (bool): If True, None is accepted as an individual value
                of each dimension index, in which case dimensions with None values 
                coming before an individual index set as an int will not be 
                considered, but the ones coming after will be included as a whole.

        Return:
            (bool): True if the index is a valid dimensional index. False otherwise.
        """
        if self.get_max_dim_grade() is not len(idx_tuple):
            self._rise_exception('_is_valid_idx_1')

        for i, idx in enumerate(idx_tuple[::-1]):
            if kwargs['none_enabled']:
                if idx is not None and type(idx) is not int:
                    self._rise_exception('_is_valid_idx_3')
                if idx is None:
                    continue
                elif idx < 0 or idx >= self.get_dim_coefficients()[i]:
                    self._rise_exception('_is_valid_idx_4')

            elif type(idx) is not int:
                self._rise_exception('_is_valid_idx_2')
            
            if idx < 0 or idx >= self.get_dim_coefficients()[i]:
                self._rise_exception('_is_valid_idx_4')

        return True

    def _rise_exception(self, idx):
        """
        Rises the respective exception according to the passed idx.
        """
        if idx == '_is_valid_idx_1':
            raise IndexError('You must provide a number of integer values as the dimensions assigned '+\
                'to the MDArray. They can be inside a container like a tuple or list.')
        elif idx == '_is_valid_idx_2':
            raise TypeError('Must pass integers as index values in the tuple.')
        elif idx == '_is_valid_idx_3':
            raise IndexError('Must pass integers or None as index values in the tuple.')
        elif idx == '_is_valid_idx_4':
            raise IndexError('Cannot pass an index value that is negative or ' +\
                    'greater than its respective dimension.')
        elif idx == '_get_start_end_values_0':
            raise IndexError('You must provide a a number of integers or None values as parameters '+\
                'equal to the quantity of dimensions in the MDArray.')
        elif idx == '_get_start_end_values_1':
            raise ValueError('You must provide a number of int or None values as the dimensions assigned '+\
                'to the MDArray (ints cannot be equal or higher than their respective dimension '+\
                'size) dimension number positioned at the desired dimension index (cannot be equal or '+\
                'higer than that dimension size). All other values should be None.')
        elif idx == '_get_start_end_values_2':
            raise ValueError('The int index cannot be equal or higher than its respective dimension size.')
        elif idx == 'dprint_0':
            raise IndexError("You must provide a valid dimension index to break the print output. The "+\
                "dimension index you are targeting must be None when assigning it to dprint()'s tuple, "+\
                "it must be a dimension lower than the last non-None dimension you specified to the "+\
                "tuple, of an integer value lower than its dimension index's respective dimension "+\
                "coefficient and higher than 0.")


    def _write_values(self, iterable, value=None, **kwargs):
        """
        Takes an iterable representing a sequence range inside the MDArray 
        and a value -both passed as parameters-, and replaces each object of 
        the MDArray in the range of that sequence with the specified value.

        Parameters:
            iterable (range): A range object representing a sequence inside
                the MDArray.
            value (any): The value to replace the objects with in the MDArray.
                Defaults to None.
        
        kwargs:
            overwrite (bool): True if all values are to be replaced, False if 
                only None values would be overriden. Defaults to True.
        """
        if 'overwrite'.lower() in kwargs:
            
            if kwargs['overwrite'.lower()] is False:

                for i in iterable:

                    if self.get_dim_repr()[i] is None:
                        self.get_dim_repr()[i] = value

                return
        
        for i in iterable:
            self.get_dim_repr()[i] = value

    class _MDArrayIterator:
        """
        A private iterator class for MDArray, called by __iter__.
        """
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
                raise StopIteration


if __name__ == "__main__":


    #######################################################
    ####  Uncomment each segments of code down below,  ####
    ####  one segment at a time, to test the methods.  ####
    #######################################################

    
    mdarr3_1 = MDArray(2, 3, 2)
    mdarr3_2 = MDArray(2, 3, 2)
    mdarr5_1 = MDArray(3, 3, 2, 4, 5)
    mdarr5_2 = MDArray(3, 3, 2, 4, 5)
    mdarr5_3 = MDArray(3, 3, 2, 4, 5)

    mdarr3_2 = mdarr3_1.indexify(True)      # assigning flat and dimensional 
    mdarr5_3 = mdarr5_2.indexify(True)      # index to each value 


    # print('None in mdarr5_1?', None in mdarr5_1)                          #  __contains__
    # print('[] in mdarr5_1?', [] in mdarr5_1)                              #
    # mdarr5_1[1,1,1,1,1] = []                                              #
    # print('[] in mdarr5_1 now?', [] in mdarr5_1)                          # /__contains__


    # print('mdarr5_1 == mdarr3_1?', mdarr5_1 == mdarr3_1)                  # __eq__
    # print('mdarr5_1 == mdarr5_2?', mdarr5_1 == mdarr5_2)                  #
    # mdarr5_1[0,0,0,0,0] = "eq will be false now"                          #
    # print('mdarr5_1 == mdarr5_2?', mdarr5_1 == mdarr5_2)                  # /__eq__


    # mdarr3_2.fprint()                                                     # __del__
    # del mdarr3_2                                                          #
    # mdarr3_2.fprint()                                                     # /__del__


    # for i, value in enumerate(mdarr3_2):                                  # __iter__
    #     print(i, ': ', value)                                             # /__iter__


    # print('mdarr3_1 len:', len(mdarr3_1))                                 # __len__
    # print('mdarr5_1 len:', len(mdarr5_1))                                 # /__len__


    # print(mdarr3_2)                                                       # __str__


    # print('mdarr5_1[1,2,1,3,2]:', mdarr5_1[1,2,1,3,2])                    # __setitem__
    # mdarr5_1[1,2,1,3,2] = "Hello!"                                        #  
    # print('mdarr5_1[1,2,1,3,2]:', mdarr5_1[1,2,1,3,2])                    # /__setitem__


    # mdarr5_1[1,2,1,3,2] = "Bye bye!"                                      # __getitem__
    # print('mdarr5_1[1,2,1,3,2]:', mdarr5_1[1,2,1,3,2])                    # /__getitem__


    # print(mdarr3_1.get_max_dim_grade(), 'is max dim grade in mdarr3_1')   # get_max_dim_grade
    # print(mdarr5_1.get_max_dim_grade(), 'is max dim grade in mdarr5_1')   # /get_max_dim_grade


    # print('The flat representation of mdarr3_2 is:')                      # get_dim_repr
    # print(mdarr3_2.get_dim_repr())                                        #
    # print('-' * 80)                                                       #
    # print('The flat representation of mdarr5_3 is:')                      #
    # print(mdarr5_3.get_dim_repr())                                        # /get_dim_repr


    # print('Dimension coefficients of mdarr3_3 are:', end=' ')             # get_dim_coefficients
    # print(mdarr3_2.get_dim_coefficients())                                #
    # print('-' * 80)                                                       #
    # print('Dimension coefficients of mdarr5_2 are:', end=' ')             #
    # print(mdarr5_2.get_dim_coefficients())                                # /get_dim_coefficients


    # print('Getting iterator for the 1st fifth dimension of mdarray5_3...')# get_dim_iterator
    # iterator = mdarr5_3.get_dim_iterator(0,None,None,None,None)           #
    # print('iterating over it and printing its values...')                 #
    # for i in iterator:                                                    #
    #     print(i, end="  ")                                                #
    # print('\n', '-' * 80)                                                 #
    # print('Getting iterator for the 3rd second dimension in the 2nd '+\   
    #       'fourth dimension in the 1st fifth dimension of mdarray5_3...') #
    # iterator = mdarr5_3.get_dim_iterator(0,1,None,2,None)                 #
    # print('iterating over it and printing its values...')                 #
    # for i in iterator:                                                    #
    #     print(i, end="  ")                                                # /get_dim_iterator


    # print('Cloning mdarr5_3 into mdarr5_4...')                            # clone
    # mdarr5_4 = mdarr5_3.clone()                                           #
    # print('mdarr5_3 == mdarr5_4? -', mdarr5_3 == mdarr5_4)                #   
    # print('Replacing a value in the clone...')                            #
    # mdarr5_4[1,1,1,1,1] = "Replaced!"                                     #
    # print('mdarr5_3 == mdarr5_4 now? -', mdarr5_3 == mdarr5_4)            # /clone


    # print('Setting True as mdarr5_1[0,0,0,0,0] value...')                 # indexOf
    # mdarr5_1[0,0,0,0,0] = True                                            #   
    # print('Setting {"a": 1} as mdarr5_1[1,1,1,1,1] value...')             #
    # mdarr5_1[1,1,1,1,1] = {"a": 1}                                        #
    # print('Setting True as mdarr5_1[2,2,1,3,4] value...')                 #
    # mdarr5_1[2,2,1,3,4] = True                                            #
    # print('-' * 80)                                                       #
    # print('Flat and dimensional indexes of True values in mdarr5_1 are:', #
    #         end=' ')                                                      #
    # print(mdarr5_1.indexOf(True))                                         #
    # print('Flat and dimensional  of {"a": 1} values in mdarr5_1 are:',    #
    #         end=' ')                                                      #
    # print(mdarr5_1.indexOf({"a": 1}))                                     # /indexOf


    # print('Showing all values in mdarr3_2...', end='\n'                   # clear_all
    # mdarr3_2.fprint()                                                     #
    # print('-' * 80)                                                       #
    # print('Setting all values to None in mdarr3_2...')                    # 
    # mdarr3_2.clear_all()                                                  #
    # print('-' * 80)                                                       #
    # print('Showing all values in mdarr3_2...', end='\n')                  #                                  
    # mdarr3_2.fprint()                                                     # /clear_all


    # print('Showing all values of the second 2nd dimension in the third')  # clear_dim
    # print('4th dimension in the first 5th dimension in mdarr5_3...')      #
    # print()                                                               #
    # mdarr5_3.fprint(0,2,None,1,None)                                      #
    # print('-' * 80)                                                       #
    # print('Setting all of those values to None')                          #
    # mdarr5_3.clear_dim(0,2,None,1,None)                                   #
    # print('-' * 80)                                                       #
    # print('Showing all values of the second 2nd dimension in the third')  #
    # print('4th dimension in the first 5th dimension in mdarr5_3...')      #
    # print()                                                               #
    # mdarr5_3.fprint(0,2,None,1,None)                                      # 
    # print('-' * 80)                                                       # /clear_dim


    # print('*' * 80)                                                       # fill_all
    # print('    Overwrite mode ON    '.center(80, '*'))                    # > overwrite=True
    # print('*' * 80)                                                       #
    # print('Showing all values in mdarr3_2...', end='\n\n')                # 
    # mdarr3_2.fprint()                                                     #
    # print('-' * 80)                                                       #
    # print('Setting all values to [1] in mdarr3_2...')                     # 
    # mdarr3_2.fill_all([1])                                                #
    # print('-' * 80)                                                       #
    # print('Showing all values in mdarr3_2...', end='\n\n')                #                                  
    # mdarr3_2.fprint()                                                     # 
    # print('-' * 80)                                                       # /fill_all


    # print('*' * 80)                                                       # fill_all
    # print('    Overwrite mode OFF    '.center(80, '*'))                   # > overwrite=False
    # print('*' * 80)                                                       #
    # print('Changing the first and last elements of mdarr3_2 to None...')  #
    # mdarr3_2[0,0,0] = None                                                #
    # mdarr3_2[1,2,1] = None                                                #
    # print('-' * 80)                                                       #
    # print('Showing all values in mdarr3_2...', end='\n\n')                # 
    # mdarr3_2.fprint()                                                     #
    # print('-' * 80)                                                       #
    # print('Setting all None values to [1] in mdarr3_2...')                # 
    # mdarr3_2.fill_all([1], overwrite=False)                               #
    # print('-' * 80)                                                       #
    # print('Showing all values in mdarr3_2...', end='\n\n')                #                                  
    # mdarr3_2.fprint()                                                     # 
    # print('-' * 80)                                                       # /fill_all


    # print('*' * 80)                                                       # fill_dim
    # print('    Overwrite mode OFF    '.center(80, '*'))                   # > overwrite=True
    # print('*' * 80)                                                       # 
    # print('Showing all values of the second 2nd dimension in the third')  #
    # print('4th dimension in the first 5th dimension in mdarr5_3...')      #
    # print()                                                               # 
    # mdarr5_3.fprint(0,2,None,1,None)                                      #
    # print('-' * 80)                                                       #
    # print('Filling that dimension with {"a": 1} values')                  # 
    # mdarr5_3.fill_dim({"a": 1}, (0,2,None,1,None))                        #
    # print('-' * 80)                                                       #
    # print('Showing all values of the second 2nd dimension in the third')  #
    # print('4th dimension in the first 5th dimension in mdarr5_3...')      #
    # print()                                                               #                                  
    # mdarr5_3.fprint(0,2,None,1,None)                                      # 
    # print('-' * 80)                                                       # /fill_dim


    # print('*' * 80)                                                       # fill_dim
    # print('    Overwrite mode OFF    '.center(80, '*'))                   # > overwrite=False
    # print('*' * 80)                                                       # 
    # print('Showing all values of the second 2nd dimension in the third')  #
    # print('4th dimension in the first 5th dimension in mdarr5_3...')      #
    # print()                                                               # 
    # mdarr5_3.fprint(0,2,None,1,None)                                      #
    # print('-' * 80)                                                       #
    # print('Assigning None to the 1st and last values of that dimension')  #
    # mdarr5_3[0,2,0,1,0] = None                                            #
    # mdarr5_3[0,2,0,1,4] = None                                            #
    # print('-' * 80)                                                       #
    # print('Displaying that dimension again...', end='\n\n')               #
    # mdarr5_3.fprint(0,2,None,1,None)                                      #
    # print('-' * 80)                                                       #
    # print('Overriding only None values with {"a": 1}')                    # 
    # mdarr5_3.fill_dim({"a": 1}, (0,2,None,1,None), overwrite=False)       #
    # print('-' * 80)                                                       #
    # print('Showing the dimension again. Only None values changed.')       #
    # print()                                                               #                                  
    # mdarr5_3.fprint(0,2,None,1,None)                                      # 
    # print('-' * 80)                                                       # /fill_dim


    # print('-' * 80)                                                       # indexify
    # print('   Showing all values in mdarr3_1.   '.center(80, '*'))        # > replace_values=True
    # print('   They are all None   '.center(80, '*'))                      # 
    # print('-' * 80)                                                       #
    # mdarr3_1.fprint()                                                     #
    # print('-' * 80)                                                       #
    # print('Replacing values for their flat and dimensional indexes...')   #
    # newmdarr3_1 = mdarr3_1.indexify(replace_values=True)                  #
    # print('-' * 80)                                                       #
    # print('   Showing all values in newmdarr3_1.   '.center(80, '*'))     #
    # print(' They are now (flat_index, dimensional_index '.center(80, '*'))# 
    # print('-' * 80)                                                       #
    # newmdarr3_1.fprint()                                                  #
    # print('-' * 80)                                                       # /indexify


    # print('-' * 80)                                                       # indexify
    # print('   Showing all values in mdarr3_1.   '.center(80, '*'))        # > replace_values=False
    # print('   They are all None   '.center(80, '*'))                      # 
    # print('-' * 80)                                                       #
    # mdarr3_1.fprint()                                                     #
    # print('-' * 80)                                                       #
    # print('Adding their their flat and dimensional indexes...')           #
    # newmdarr3_1 = mdarr3_1.indexify(replace_values=False)                 #
    # print('-' * 80)                                                       #
    # print('   Showing all values in newmdarr3_1.   '.center(80, '*'))     #
    # print(' They are now (flat_index, dim_index, value '.center(80,'*'))  # 
    # print('-' * 80)                                                       #
    # newmdarr3_1.fprint()                                                  #
    # print('-' * 80)                                                       # /indexify



    # print('*' * 80)                                                       # pprint
    # print('      Showing the first 5th dimension      '.center(80, '*'))  # > whole MDArray
    # print(' broken by all its 3rd grade subdimensions '.center(80, '*'))  # > break_by_dimensions
    # print('      and displaying in detailed view      '.center(80, '*'))  # > detailed_view
    # print('*' * 80)                                                       #
    # mdarr5_1.pprint(
    #     break_by_dimension=3, show_details=True, value_separator=' || ')  # /pprint 


    # print('*' * 80)                                                       # pprint
    # print('      Showing the first 3rd dimension      '.center(80, '*'))  # > Dimension:
    # print('        of the second 4th dimension        '.center(80, '*'))  # (None,1,0,None,None)
    # print(' broken by all its 2nd grade subdimensions '.center(80, '*'))  # > break_by_dimension
    # print('               no detail view              '.center(80, '*'))  # 
    # print('*' * 80)                                                       #
    # mdarr5_1.pprint(
    #     None,1,0,None,None, break_by_dimension=2, value_separator='\n')   # /pprint 


    # print('*' * 80)                                                       # fprint
    # print('   Fast printing the first 3rd dimension '.center(80, '*'))    # > Dimension:
    # print(' of the second 4th dimension in mdarr5_3 '.center(80, '*'))    # (None,1,0,None,None)
    # print('*' * 80)                                                       # /fprint
    # mdarr5_3.fprint(None,1,0,None,None)


    # print('*' * 80)                                                       # pprint
    # print('    Fast printing the whole mdarr3_2    '.center(80, '*'))     # > mdarr_3
    # print('*' * 80)                                                       # 
    # mdarr3_2.fprint()                                                     # /pprint
