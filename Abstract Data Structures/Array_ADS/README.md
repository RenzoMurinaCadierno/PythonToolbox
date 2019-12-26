Array Abstract Data Structure
========================================

Overview
----------------------------------------

A C Array class emulated in Python using ctypes module.

It is basically a fixed-size Python list that can be constructed either
passing an integer as the size, or the values it will store in a list.

I have made this one following Rance D. Necaise's proposed exercise in his
'Data Structures and Algorithms using Python' book. Definitely worth checking it out, it has taught me lots.

**Methods:**
- *\_\_init\_\_*
- *\_\_len\_\_*
- *\_\_getitem\_\_*
- *\_\_setitem\_\_*
- *\_\_iter\_\_*
- *\_\_contains\_\_*
- *\_\_eq\_\_*
- *\_\_str\_\_*
- *fill* : Changes each array value to the value passed as a parameter.
- *clear* : Changes each array value None.

**Subclasses:**
- *_ArrayIterator* : A class to generate the iterator when _\_\_iter\_\__ is called.

Test and Use it!
------------------------------------------

Down below in the script you can find instances and methods as examples. Uncomment them to test them out.

Or just import the script from any other one, instantiate a set using Array() constructor and there you go!

### Thank you for reading and for taking your time to check this script out!