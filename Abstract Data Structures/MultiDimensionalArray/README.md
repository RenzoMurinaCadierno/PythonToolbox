Multidimensional Array Abstract Data Structure
==================================

Overview
----------------------------------
MDArray is a class capable of storing any combination of 'n' dimensions inside a simple 1D Array. 

It takes any number of dimension grades and coefficients and inserts all of its initial values inside a single Array. To access the values of each specific dimension, the built-in iterators skip each dimension or elements inside the target subdimension using factors, which are no more than each dimensions' coefficients times their grades.

Everything is explained on each method, so feel free to check them out (they are in the script itself and down below in this markdown). You are able to use this class to instantiate 2D Arrays (like a regular matrix), up to 'n'D Arrays. At the bottom of the script, in *\_\_main\_\_*, I've presented several examples for you to test out. Those involve three and five dimensional arrays just for the sake of comprehension. Once you get the grasp of it, try creating examples on higher dimensions, like 7D, 10D, 30D, 100D, or whatever you like. Just keep in mind that, like in real life, 4D+ dimensions are harder to visualize, so have a good understanding of pprint() before attempting higher grades.

You can target all MDArray values, a whole dimension, specific subdimensions (like the first 2nd dimension inside the fourth 3rd dimension inside the second 5th dimension, for example), or even individual elements. You can change single values inside a dimension, all values in it. You can also compare MDArrays, generate hiper-specific iterators, index elements by their flat MDArray access and by their dimensional representation index, and more. Go, the world is yours. 

Instructions
----------------------------------
Just import this file in your script and instantiate the main class passing any number of dimensions with their coefficients as parameters. That way, an MDArray with your specs will be generated and ready to use. Everything is commented in the code, feel free to check it out.

You pass the dimensions' grades and their coefficients simply by passing integers to the constructor from the highest dimension grade to the first dimension.

- MDArray(5,3) will construct a 2D flat Array with five 2-dimensions each holding three 1-dimensions. Or, a 5-row 3-column 2x2 matrix.
- MDArray(4,3,2) will create a 3D flat Array with four 3-dimensions, each one holding three 2-dimensions, and each of those 2-dimensions holding two 1-dimensions. Like a 4-table 3-row 2-columns 3x3 matrix.
- And so on, you get the picture.

Make sure array.py is inside 'modules' directory, and that directory next to this script.

As stated above, there are examples in the *\_\_main\_\_* program down below in the script, they are designed to show you the usage. Execute them in the same script.

Attributes, methods and classes
----------------------------------
***NOTE*** : The explanations here are VERY brief, just to give you an overview of what everything does. The detailed description is in the script itself, in each method's commentary.

**Attributes:**
- *self.\_dim\_repr* : The array that holds all values.
- *self.\_dim\_values* : An array that holds the        dimension coefficients.
- *self.\_factors* : An array to hold all dimension factors.

**Main Methods:**
- *\_\_init\_\_*
- *\_\_contains\_\_*
- *\_\_eq\_\_*
- *\_\_del\_\_*
- *\_\_iter\_\_*
- *\_\_len\_\_*
- *\_\_str\_\_*
- *\_\_getitem\_\_*
- *\_\_setitem\_\_*
- _get\_max\_dim\_grade_ : Returns the maximum dimension grade of the MDArray.
- _get\_dim\_repr_ : Returns the flat representation of the MDArray.
- _get\_dim\_coefficients_ : Returns an Array with the coefficient values of each dimension grade in the MDArray.
- _get\_dim\_iterator_ : Takes a valid dimensional index, generates and returns an iterator object containing all members of that dimension.
- _clone_ : Creates and returns a new MDArray instance with the same length as self, its same values, dimensions and factors.
- _indexOf_ : Finds the 1D MDArray index(es) and the dimensional index(es) of the value passed as parameter, and returns them as a tuple.
- _clear\_all_ : Overwrites all MDArray's values with None.
- _clear\_dim_ : Sets all objects in a specific dimension to None.
- _fill\_all_ : Replaces each value in the MDArray with a value passed as a parameter.
- _fill\_dim_ : Replaces each value in a specific dimension a the value passed as a parameter.
- _indexify_ : Creates and returns new MDArray instance with the same flat length as self, assigning a tuple to each of its values containing their flat MDArray access index and dimensional index.
- _pprint_ : Prints out the MDArray in a more readable format than its *\_\_str\_\_* equivalent. The output will vary depending on the kwargs.
- _fprint_ : A much faster but not as informative version of pprint().

**Helper Methods:**
- *_direct\_idx* : Multiplies each value of idx_tuple by its respective factor and adds the result up to get the direct flat index of the MDArray.
- *_get\_iterable* : Given the dimensional index passed as args, it creates and returns a list object containing all members of the specified dimension.
- *_get\_factors* : Calculates and returns an array containing the factors of each dimension grade in the MDArray. The factors are the numbers to multiply and add when trying to reach to a specific dimension inside the flat Array that holds all values.
- *_get\_start\_end\_values* : Takes a tuple with the dimensional index pointing to a specific dimension and returns a start and an end integer value to pass as parameters to range() so as to iterate over that dimension inside the flat MDArray.
- *_is\_valid\_idx\_* : Checks if the dimensional index passed as idx_tuple is a valid one according to the MDArray's dimension grade and its individual coefficients.
- *_rise\_exception* : Rises the respective exception according to the passed idx.
- *_write\_values* : Takes an iterable representing a sequence range inside the MDArray and a value -both passed as parameters-, and replaces each object of the MDArray in the range of that sequence with a specified value.

**Meta Classes:**
- *_SSLL\_Iterator* : Inner private class that generates the iterators.

TODOs
----------------------------------
The module is ready to use, but some details could be added to enhance it. I do not intend to do so in the near future since I want to move to other projects, but it might be a good practice for anyone who desires to tackle the challenge, or for me myself ahead in time.
- Suppose the MDArray's elements are integers and/or floats. Even though you could target individual elements or dimensions and perform arithmetics over some other values or dimensions applying the right set of instructions -like you do in matrix addition, substraction, scaling and so on-, it would be nice to add methods that accept other MDArrays and perform the given operations to return a new MDArray or to modify the base one according to the result. Some ideas include:
    - *add_all(other_MDArray)* : sums up the values of self and other_MDArray and returns a new MDArray with the added values.
    - *add_dim(dim_index, other_dimension)* : sums up the values of the specified dimension in self and a dimension in other_dimension.
    - *sub_all(other_MDArray)* : same as add_all but for substraction.
    - *sub_dim(dim_idx, other_dimension)* : same as sub_all but for substraction.
    - *scale(scalar)* : multiplies each MDArray element by the given scalar. Changes the values in self or returns a new MDArray with the calculated values.
    - *mul_all(other_MDArray)* : performs an n-dimensional multiplication between the elements in self and other_MDArray. Modifies the elements in the targetted MDArray or returns a new MDArray with the calculated values.
    - *mul_dim(dim_index, other_dimension)* : performs a miltiplication between the elements of the given dim_idx and other_dimension. Modifies the elements in the targetted dimension or returns a new dimension with the calculated values.
- Suppose the MDArray's elements are strings. Given the same conditions as above, some methods could be added to work with strings, like:
    - *concat_all(string)* : concatenates all elements of the MDArray with the given string.
    - *concat_dim(dim_idx, string)* : concatenates the string with each element of the dimension targetted by dim_idx.
    - *find_str_all(regex)* : looks in all elements of the MDArray for regex matches and returns the results. Could return indexed positions.
    - *find_str_dim(dim_idx, regex)* : same as find_str_all(regex) but for the targetted dimension by dim_idx.
    - *replace_str(regex, replacement)* : look up in the same fashion as find_str_all() but replaces the matches with replacement.
    - *replace_str_dim(dim_idx, regex, replacement)* : same as replace_str() but for a targetted dimension.

What learned from this project
----------------------------------
- A flat 1D can represent multiple arrays at once just by skipping over values in specific ways. This eliminates the need to nest arrays in arrays, or list in lists to create matrix-like objects.
- Nothing comes for free, though. The amount of consecutive storage required for large dimension grade arrays is pretty high, and thus it might be difficult to allocate in memory. This is the case where multidimensional Linked Lists may come handy, but they also have a high cost: any operation that requires accessing an item is costly, specially when dealing with high grades. Even with an external references which move freely to access nodes closer to them, the iterations would take time, and those references, storage space. Thus, if you are to access individual dimension elements more frequently than any other type of operation, then MDArray is ideal. However, if you do not access individual elements or dimensions that often,but you do other types of operations that require expansion or deletion -like adding extra dimensions or elements-, then a Linked List structure might be handier.
- *\_\_setitem\_\_* recieves its access index as a tuple. It might be obvious, but as a beginner, I did not know. This helped me simplify how arguments are passed in order to direct access the MDArray, without needing to use an explicit tuple for them. This is, I could write the access method call like _MDArray[0,1,2]_, and not like _MDArray[(0,1,2)]_.
- If you want to iterate over a tuple in reverse order and then use the iterating index in the loop, it is better to declare the reversed tuple out of the for loop declaration, since the latter will conflict with the current index and the value accessed in reverse.
- Working with reverse lists to emulate dimensions and factors in conjunction with normally ordered lists to do the same turns out to be confusing at one point, specially when passing parameters to a method that loops on the same list directly and reversed in different steps. Must avoid when possible, criteria unification is key.
- I must read my own methods and parameters and keep them in mind, always. When developing _\_get\_start\_end\_values\_()_, I was having a hard time trying to make the method pass through all values in the MDArray and not only those in a single dimension as I initially intended to. I came up with a solution that involved using recursion, just to scrape it out when I remembered that *self.\_dim\_repr* is an Array (iterable) that contains all MDArray values in order. The only thing I needed to do there is to use *self.\_dim\_repr* to generate the iterator. A couple hours wasted overthinking, but worth the learning process.
- Finally, if you are to work with multidimensional arrays represented by a 1D flat one, _INDEX THE VALUES BY DEFAULT!_ This will cost additional storage space, but everything that requires searching for a value whose location is not known beforehand would require less-to-no iterations. And trust me, lots of methods do, so I think it pays off in the end.
  
### Thank you for reading and for taking your time to check this project out!
