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
    - /_/_self._/_head_ : Head reference to first node.
    - /_/_self._/_tail_ : Tail reference to last node.
    - /_/_self._/_idx_ : Index to assign to each node to keep sorted order.

**Methods:**
    - /_/_len_/_/
    - /_/_str_/_/
    - /_/_iter_/_/
    - /_/_contains_/_/
    - /_/_getitem_/_/
    - /_/_setitem_/_/
    - /_/_eq_/_/
    - _get_/_head_ : Gets a reference to the head node.
    - _get_/_tail_ : Gets a reference to the tail node.
    - _get_/_list_/_index_ : Gets the current list index.
    - _get_/_nodes_ : Gets all nodes in the list.
    - _set_/_nodes_ : Sets all nodes to a value. Has a safe overwirte mode to replace only the nodes whose values are None.
    - _indexOf_ : Gets the indexes of the node whose values matches with the parameter.
    - _valueOf_ : Gets the value of the node whose index matches with the parameter.
    - _append_ : Inserts a value/node at the end of the list.
    - _prepend_ : Inserts a value/node at the beginning of the list.
    - _insert_ : Inserts a value/node at the given index position.
    - _pop_ : Removes the node at the given index. Defaults to self._tail
    - _pprint_ : Prints each node's index and values. A detailed print.
    - _split_ : Splits the list in two starting at the given index and returns a reference to the head of the second list.
    - _/_find_/_by_/_value_ : finds and returns a tuple of tuples with all nodes whose values match the one passed as a parameter. Inner tuples : (matched_node, previous_neighbor).
    - _/_find_/_by_/_index_ : finds and returns a tuple with the node whose index matches the one passed as a parameter. The tuple will also contain the previous neighbor.          
    - _/_nodify_ : Takes a value and converts it to a SSLL_Node instace before returning it. If the value is already an instance of that class, it will be returned with no changes.
    - _/_reindex_ : Beginning from the node passed as a parameter, reindexed each node counting from the integer onwards.

**Classes:**
    - _/_SSLL_/_Iterator_ : Inner private class that generates the iterator.
    - _SSLL_/_Node_ : Outer public class that creates valid node objects. It is kept public for convenience, when nodes ought to be created before assigning them to the linked list.

        **Attributes:**
            - /_/_self._/_value_ : The node's value. 
            - /_/_self._/_idx_ : The node's index assigned by the linked list. Defaults to None.
            - /_/_self._/_next_ : The reference to the next node. Defaults to None.

       **Methods:**
            - _get_/_values_ : Returns the node's value.
            - _get_/_index_ : Returns the node's index.
            - _get_/_next_ : Returns a reference to the node linked to the _next field.