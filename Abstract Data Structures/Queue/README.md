Queue Abstract Data Structure
==================================

Overview
----------------------------------
A class that tries to emulate the behavior of a Queue data structure.

It extends (and limits some capabilities of) its parent class: the Sorted Singly linked list.

Attributes, methods and classes
----------------------------------
**Methods:**
- *\_\_str\_\_* : Overrides super().__str__() to print out the queue in a more intuitive way.
- _clear_ : Removes all nodes from the queue. This is an unmodified super() method to make you remember you can still use all of those on instances of this class too.
- _clone_ : Overrides super().clone() so that an instance of the queue class is returned, and not one of the parent's.
- _peek_ : Returns a reference to the end of the queue.
- _dequeue_ : Removes the node from the top of the queue and returns a reference to it.
- _enqueue_ : Adds a node to the end of the queue.
- _split_ : Overrides super().split() so that both halves can be returned as Queue instances.
- _And all other methods, attributes and classes in the parent's class._

Instructions
----------------------------------
Make sure the 'modules' folder is in the same directory as queue.py.

Just import this file in your script and instantiate the main class. From there on, you can create Queue objects. Everything is commented in the code and in the module files, feel free to check them out.

As stated above, there are examples in the main program down below in the script. They are designed to show you the usage.

What learned from this project
----------------------------------
- How queues work in depth and how close they behave as Linked Lists.
- How easy is to create new Data Structures inheriting from similar ones and changing the behavior by adding, restricting or modifying methods.
- If something work as intended and there are some minor and unimportant details to correct just for the sake of aesthetics, DO NOT TOUCH anything. It is better to be clear in commentaries instead of trying to accidentally mess with the functionality, even if the code is modular and well written.

### Thank you for reading and for taking your time to check this project out!
