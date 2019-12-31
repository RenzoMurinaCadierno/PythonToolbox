Stack Abstract Data Structure
==================================

Overview
----------------------------------
A class that tries to emulate the behavior of a Stack data structure.

It extends (and limits some capabilities of) its parent class: the Sorted Singly linked list.

Attributes, methods and classes
----------------------------------
**Methods:**
- *\_\_str\_\_* : Overrides super().__str__() to print out the stack
                in a more intuitive way.
- _clone_ : Overrides super().clone() so that an instance of the Stack class is returned, and not one of the parent's.
- _peek_ : Returns a reference to the top of the stack.
- _pop_ : Removes the node from the top of the stack and returns a reference to it.
- _push_ : Adds a node to the top of the stack.
- _split_ : Overrides super().split() so that both halves can be returned as Stack instances.
- _And all other methods, attributes and classes in the parent's class._

Instructions
----------------------------------
Make sure the parent class is situated on .
Just import this file in your script and instantiate the main class. From there on, you can create node and linked list objects. Everything is commented in the code, feel free to check it out.

As stated above, there are examples in the main program down below in the script, they are designed to show you the usage.

What learned from this project
----------------------------------
- How stacks work in depth and how close they behave as Linked Lists.
- How easy is to create new Data Structures inheriting from similar ones and changing the behavior by adding, restricting or modifying methods.
- I'm getting better at debugging, little by little. I notice I can spot and correct bugs quicker than before.

###Thank you for reading and for taking your time to check this project out!
