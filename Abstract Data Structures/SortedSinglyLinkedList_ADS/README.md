Sorted Singly Linked List ADS
==================================

Overview
----------------------------------

A class that tries to emulate the behavior of a _Singly Sorted linked list_, with some additional features.

You can create object instances by simply calling the constructor, in which case a linked list will contain a single node with a value of none, index of zero, and head and tail references pointing to it.

Or, you can pass any number of objects (they do not need to be valid node instances) when constructing the list, and they will be automatically converted to valid nodes if necessary and assigned an index to each in the order you passed them as args. This way, the head reference will point to node (former arg) index 0, and tail to the last supplied value. The list index will always be the same as its length, and will increase and decrease as nodes are added/removed.

From there on, please feel free to check the methods, they are all commented and -I hope- readable. Moreover, there are several examples down below, when the main program initializes. Uncomment them a block at a time to test them out.

Please, keep in mind that _this structure is NOT a multi-linked list_. Since each list is indexed by using its nodes _idx individual values, it DOES NOT SUPPORT adding the same node to different lists. Whenever a new node is added to a linked list, the list is reindexed, what affects the index values of other lists that contain that node in them alas breaking the integrity. You can do so if you desire. However, keep in mind that the behavior of any method that searches by index value will rise an exception or generate and infinite loop, since this way a list can contain more than one of the same index.

**Attributes:**
- *_self.\_head* : Head reference to first node.
- *_self.\_tail* : Tail reference to last node.
- *_self.\_idx* : Index to assign to each node to keep sorted order.

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
- _get\_nodes_ : Gets all nodes in the list.
- _set\_nodes_ : Sets all nodes to a value. Has a safe overwirte mode to replace only the nodes whose values are None.
- _indexOf_ : Gets the indexes of the node whose values matches with the parameter.
- _valueOf_ : Gets the value of the node whose index matches with the parameter.
- _append_ : Inserts a value/node at the end of the list.
- _prepend_ : Inserts a value/node at the beginning of the list.
- _insert_ : Inserts a value/node at the given index position.
- _pop_ : Removes the node at the given index. Defaults to self._tail
- _pprint_ : Prints each node's index and values. A detailed print.
- _split_ : Splits the list in two starting at the given index and returns a reference to the head of the second list.
- *_find\_value\_by\_value* : finds and returns a tuple of tuples with all nodes whose values match the one passed as a parameter. Inner tuples : (matched_node, previous_neighbor).
- *_find\_value\_by\_index* : finds and returns a tuple with the node whose index matches the one passed as a parameter. The tuple will also contain the previous neighbor.          
- *_nodify* : Takes a value and converts it to a SSLL_Node instace before returning it. If the value is already an instance of that class, it will be returned with no changes.
- *_reindex* : Beginning from the node passed as a parameter, reindexed each node counting from the integer onwards.

**Classes:**
- *_SSLL\_Iterator* : Inner private class that generates the iterator.
- *SSLL\_Node* : Outer public class that creates valid node objects. It is kept public for convenience, when nodes ought to be created before assigning them to the linked list.

- **Attributes:**
    - *_self.\_value* : The node's value. 
    - *_self.\_idx* : The node's index assigned by the linked list. Defaults to None.
    - *_self.\_next* : The reference to the next node. Defaults to None.

- **Methods:**
    - *_get\_value* : Returns the node's value.
    - *_get\_index* : Returns the node's index.
    - *_get\_next* : Returns a reference to the node linked to the _next field.
