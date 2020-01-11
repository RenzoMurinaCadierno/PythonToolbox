Sorted Singly Linked List Abstract Data Structure
==================================

Overview
----------------------------------

A class that tries to emulate the behavior of a _Singly Sorted linked list_, with some additional features.

You can create object instances by simply calling the constructor, in which case a linked list will be empty, with no head or tail references linked to anything.

Or, you can pass any number of objects (they do not need to be valid node instances) when constructing the list, and they will be automatically converted to valid nodes if necessary and assigned an index to each in the order you passed them as args. This way, the head reference will point to node (former arg) index 0, and tail to the last supplied value. The list index will always be the same as its length, and will increase and decrease as nodes are added/removed.

From there on, feel free to check the methods, they are all commented and -I hope- readable. Moreover, there are several examples down below, when the main program initializes. Uncomment them a block at a time to test them out.

Keep in mind that this structure does NOT support adding the same node to different lists, since each list is indexed by using its nodes _idx individual values. Whenever a new node is added to a linked list, the list is reindexed, what affects the index values of other lists that contain that node in them alas breaking the integrity. You can do so if you desire. However, keep in mind that the behavior of any method that searches by index value will rise an exception or generate and infinite loop, since this way a list can contain more than one of the same index.


Instructions
----------------------------------
Just import this file in your script and instantiate the main class. From there on, you can create node and linked list objects. Everything is commented in the code, feel free to check it out.

As stated above, there are examples in the main program down below in the script, they are designed to show you the usage.

Attributes, methods and classes
----------------------------------

**Attributes:**
- *self.\_head* : Head reference to first node.
- *self.\_tail* : Tail reference to last node.
- *self.\_idx* : Index to assign to each node to keep sorted order.

**Methods:**
- *\_\_init\_\_*
- *\_\_len\_\_*
- *\_\_str\_\_*
- *\_\_iter\_\_*
- *\_\_contains\_\_*
- *\_\_getitem\_\_*
- *\_\_setitem\_\_*
- *\_\_eq\_\_*
- _get\_head_ : Gets a reference to the head node.
- _get\_tail_ : Gets a reference to the tail node.
- _get\_list\_index_ : Gets the current list index.
- _get\_nodes_ : Gets a tuple with all nodes in the list. If indexed=True is passed as parameter, it gets a tuple of tuples where each inner tuple is in the format of (node index, node value).
- _set\_nodes_ : Sets all nodes to a value. Has a safe overwirte mode to replace only the nodes whose values are None.
- _indexOf_ : Gets the indexes of the node whose values matches with the parameter.
- _valueOf_ : Gets the value of the node whose index matches with the parameter.
- _clear_ : Removes all nodes from the list. If the nodes are not bound to an external reference, they will be garbage collected.
- _append_ : Inserts a value/node at the end of the list.
- _prepend_ : Inserts a value/node at the beginning of the list.
- _insert_ : Inserts a value/node at the given index position.
- _pop_ : Removes the node at the given index. Defaults to self._tail
- _pprint_ : Prints each node's index and values. A detailed print.
- _dprint_ : Prints the current list index, the list itself (as in pprint), and the head and tail references with their index, value and next fields. If all_nodes=True, all of the member nodes will be printed out in the same fashion.
- _split_ : Splits the list in two starting at the given index and returns a reference to the head of the second list.
- _clone_ : Creates and returns a shallow copy of the linked list.
- *_find\_by\_value* : finds and returns a tuple of tuples with all nodes whose values match the one passed as a parameter. Inner tuples : (matched_node, previous_neighbor).
- *_find\_by\_index* : finds and returns a tuple with the node whose index matches the one passed as a parameter. The tuple will also contain the previous neighbor.          
- *_nodify* : Takes a value and converts it to a SSLL_Node instace before returning it. If the value is already an instance of that class, it will be returned with no changes.
- *_reindex* : Beginning from the node passed as parameter, reindexes each node counting from the integer passed as parameter onwards.

**Classes:**
- *_SSLL\_Iterator* : Inner private class that generates the iterator.
- *SSLL\_Node* : Outer public class that creates valid node objects. It is kept public for convenience, when nodes ought to be created before assigning them to the linked list.

- **Attributes:**
    - *self.\_value* : The node's value. 
    - *self.\_idx* : The node's index assigned by the linked list. Defaults to None.
    - *self.\_next* : The reference to the next node. Defaults to None.

- **Methods:**
    - *_get\_value* : Returns the node's value.
    - *_get\_index* : Returns the node's index.
    - *_get\_next* : Returns a reference to the node linked to the _next field.

What I learned from this project
----------------------------------
- How singly linked list work.
- Some pros and cons of working with node indexing in complement of the head and tail references.
- Sometimes storage matters, sometimes speed do. Linked lists are better to work with if you require huge amounts of nodes, since each one is places on its individual memory address. Also, head and tail reference stand for fast append and prepend methods. Though however, if the list is large, removing or inserting nodes can take time. Here is where indexing comes into play, since ordered items make it up in overall speed allowing the search to end prematurely. Nothing matches array's direct access, though.
- How NOT to add the same node to mutiple linked lists if they are indexed. Methods that reindex nodes break the integrity of other lists that contain the same node, thus anything that requires looking for a node up by its index will crash on them.

Debugging
----------------------------------
**12.31.2019**

- *Added **clear***: A method to remove all nodes from the list. Sets the list index to 0 and head and tail references to None.
- *Added **clone***: A method to that returns a shallow copy of the linked list.
- *Refactored **\_\_init\_\_***: it no longers generates a node when no parameters are passed as a constructor.
- *Refactored **\_\_eq\_\_***: modified the assertion to check for any instance of this class or its children's.
- *Refactored **\_\_str\_\_***: removed *args and *kwargs, replaced them with start and end positional arguments to format each descendant neatly.
- *Refactored **get_nodes***: it now accepts "indexed" as a kwarg. Defaults to False. Removed *args.
- *Refactored **set_nodes***: it now accepts "overwrite" as a kwarg. Defaults to False. Removed *args.
- *Refactored **dprint***: it now accepts "all_nodes" as a kwarg. Defaults to False. Removed *args.
  
### Thank you for reading and for taking your time to check this project out!
