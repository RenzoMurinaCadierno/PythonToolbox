Set Abstract Data Structure
========================================

Overview
----------------------------------------

A Set Abstract Data Class built up around Python list data structure, 
binary search and merge sort algorithms to emulate some basic functionalities 
of Python's Set data structure. 

It currently accepts integers and floats as values. Items are inserted and kept in order at all times, which makes binary searching possible.

I have made this one following Rance D. Necaise's proposed exercise in his 'Data Structures and Algorithms using Python' book. Definitely worth checking out, it has taught me lots.

**Methods:**
- *\_\_init\_\_*
- *\_\_len\_\_*
- *\_\_contains\_\_*
- *\_\_iter\__*
- *\_\_eq\_\_*
- *\_\_str\_\_*
- *add*
- *pop*
- *is_subset*
- *union*
- *intersection*
- *difference*
- *_get_idx_position* : Helper method to get the index position of a value.

**Subclasses:**
- *_SetIterator* : A class to generate the iterator when */_/_iter/_/_* is called.

Test and Use it!
------------------------------------------

Down below in the script you can find instances and methods as examples. Uncomment them to test them out.

Or just import the script from any other one, instantiate a set using Set() constructor and there you go!

### Thank you for reading and for taking your time to check this script out!
