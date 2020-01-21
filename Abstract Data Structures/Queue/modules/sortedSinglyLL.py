class SortedSinglyLL:
    """
    A class that tries to emulate the behavior of a Singly Sorted linked 
    list, with some additional features.

    You can create object instances by simply calling the constructor,
    in which case a linked list will be empty, with no head or tail
    references linked to anything.
    
    Or, you can pass any number of objects (they do not need to be
    valid node instances) when constructing the list, and they will be
    automatically converted to valid nodes if necessary and assigned an 
    index to each in the order you passed them as args. This way, the 
    head reference will point to node (former arg) index 0, and tail to 
    the last supplied value. The list index will always be the same as
    its length, and will increase and decrease as nodes are added/removed.

    From there on, feel free to check the methods, they are all commented 
    and -I hope- readable. Moreover, there are several examples down below, 
    when the main program initializes. Uncomment them a block at a time to 
    test them out.

    Keep in mind that this structure does NOT support adding the same node
    different lists, since each list is indexed by using its nodes _idx 
    individual values. Whenever a new node is added to a linked list, the 
    list is reindexed, what affects the index values of other lists that 
    contain that node in them alas breaking the integrity. You can do so 
    if you desire. However, keep in mind that the behavior of any method that 
    searches by index value will rise an exception or generate and infinite 
    loop, since this way a list can contain more than one of the same index.

    Attributes:
        self._head : Head reference to first node.
        self._tail : Tail reference to last node.
        self._idx : Index to assign to each node to keep sorted order.
    
    Methods:
        __init__
        __len__
        __str__
        __iter__
        __contains__
        __getitem__
        __setitem__
        __eq__
        get_head : Gets a reference to the head node.
        get_tail : Gets a reference to the tail node.
        get_list_index : Gets the current list index.
        get_nodes : Gets a tuple with all nodes in the list. If indexed=True 
                     is passed as parameter, it gets a tuple of tuples where
                     each inner tuple is in the format of (node index, node value).
        set_nodes : Sets all nodes to a value. Has a safe overwirte 
                     mode to replace only the nodes whose values are None.
        indexOf : Gets the indexes of the node whose values matches with 
                the parameter.
        is_empty : Returns True if the head pointer is None.
        valueOf : Gets the value of the node whose index matches with 
                the parameter.
        clear : Removes all nodes from the list. If the nodes are not bound
                to an external reference, they will be garbage collected.
        append : Inserts a value/node at the end of the list.
        prepend : Inserts a value/node at the beginning of the list.
        insert : Inserts a value/node at the given index position.
        pop : Removes the node at the given index. Defaults to self._tail
        dprint : Prints the current list index, the list itself (as in
                  pprint), and the head and tail references with their index,
                  value and next fields. If all_nodes=True, all of the member
                  nodes will be printed out in the same fashion.
        pprint : Prints each node's index and values. A detailed print.
        split : Splits the list in two starting at the given index and 
                returns a reference to the head of the second list.
        clone : Creates and returns a shallow copy of the linked list.
        _find_by_value : finds and returns a tuple of tuples with all nodes  
                        whose values match the one passed as a parameter.
                        Inner tuples : (matched_node, previous_neighbor).
        _find_by_index : finds and returns a tuple with the node whose index
                        matches the one passed as a parameter. The tuple
                        will also contain the previous neighbor.          
        _nodify : Takes a value and converts it to a SSLL_Node instace before
                returning it. If the value is already an instance of that
                class, it will be returned with no changes.
        _reindex : Beginning from the node passed as a parameter, reindexed
                each node counting from the integer onwards.

    Classes:
        _SSLL_Iterator : Inner private class that generates the iterator.

        SSLL_Node : Outer public class that creates valid node objects.
                    It is kept public for convenience, when nodes ought to
                    be created before assigning them to the linked list.

            Attributes:
                self._value : The node's value.
                self._idx : The node's index assigned by the linked list.
                            Defaults to None.
                self._next : The reference to the next node.
                                Defaults to None.

            Methods:
                get_value : Returns the node's value.
                get_index : Returns the node's index.
                get_next : Returns a reference to the node linked to the
                            _next field.

    Author: Renzo Nahuel Murina Cadierno - December 29, 2019.
    Github: https://github.com/RenzoMurinaCadierno
    Contact: nmcadierno@hotmail.com
    """         

    def __init__(self, *args):
        """ 
        Initializes a list composed SSLL_Node objects with the values
        passed as args in that order. Assigns an index to each of them
        and links them by their _next field.
        
        If no args are supplied, the instance will be empty.
        """
        self._idx = 0
        self._head = None
        self._tail = None

        if args:
            first = self._nodify(args[0])
            first._idx = self._idx
            self._idx +=1
            self._head = first
            self._tail = first

            for arg in args[1:]:
                node = self._nodify(arg)
                node._idx = self._idx
                self._idx += 1
                self._tail._next = node
                self._tail = node

    def __len__(self):
        return self._idx

    def __str__(self, start=">> ", end=" >/>", separator='->'):
        current = self._head
        rtn = start

        while current:

            if not current._next:
                rtn += f'{current}'
                break

            rtn += f'{current} {separator} '
            current = current._next

        rtn += end
        return rtn

    def __iter__(self):
        return self._SSLL_Iterator(self._head)

    def __contains__(self, node):
        result = self._find_by_value(node)
        return True if result[0][0] else False

    def __getitem__(self, idx):
        result = self._find_by_index(idx)

        if result[0]:
            return result[0].value
        else:
            raise IndexError('Index out of range.')

    def __setitem__(self, idx, value):
        result = self._find_by_index(idx)

        if result[0] == self._tail and isinstance(value, SSLL_Node):
            self.pop(result[0]._idx)
            self.insert(value, 'end')
        elif result[0] and isinstance(value, SSLL_Node):
            temp = result[0]._idx
            self.pop(result[0]._idx)
            self.insert(value, temp)
        elif result[0]:
            result[0].value = value
        else:
            raise IndexError('Index out of range.')

    def __eq__(self, ssll):
        assert isinstance(ssll, SortedSinglyLL), \
            "Both instances must be type SortedSinglyLL to compare."
 
        current_one = self._head
        current_two = ssll._head

        while current_one and current_two:
            if repr(current_one.value) != repr(current_two.value):
                return False
            current_one = current_one._next
            current_two = current_two._next

        if current_one or current_two:
            return False
        
        return True

    def get_head(self):
        """ 
        Returns a reference to the head node.
        """
        return self._head

    def get_tail(self):
        """ 
        Returns a reference to the tail node.
        """
        return self._tail

    def get_list_index(self):
        """ 
        Returns a reference to the current index node.
        """
        return len(self)

    def get_nodes(self, **kwargs):
        """ 
        Returns a tuple populated with all nodes of the linked list.
        
        If indexed=True, the returned tuple will contain each node in
        its individuall tuple in the format of (index, value).
        
        If indexed=False, the each node inside the returned tuple will
        consist have a reference to its value.
        """
        nodes = []
        current = self._head

        while current:
            if 'indexed' in kwargs.keys():
                if kwargs['indexed'] == True:
                    nodes.append((current._idx, current.value))
            else:
                nodes.append(current.value)
            current = current._next

        return tuple(nodes)

    def set_nodes(self, value, **kwargs):
        """ 
        Sets each nodes' values to the one passed as a parameter.
        
        If overwrite=True, all values will be changed.
        
        If overwrite=False, only values=None will be changed.
        """
        current = self._head

        while current:

            if 'overwrite' in kwargs.keys():

                if kwargs['overwrite'] == True:
                    current.value = value 
                elif kwargs['overwrite'] == False and current.value == None:
                    current.value = value

            elif 'overwrite' not in kwargs.keys() and current.value == None:
                current.value = value

            current = current._next

    def indexOf(self, node_or_value):
        """ 
        Returns a tuple containing the indexes of the nodes whose 
        values match the value or the node's value passed as the 
        parameter. 
        """
        result = self._find_by_value(node_or_value)

        if result[0][0]:
            return tuple([result[i][0]._idx for i in range(len(result))])
        else:
            raise ValueError('Value not in list.')

    def is_empty(self):
        """
        Returns True if the head pointer is None.
        """
        return self._head is None

    def valueOf(self, idx):
        """ 
        Returns the value of the index passed as parameter. 
        """
        result = self._find_by_index(idx)

        if result[0]:
            return result[0].value
        else:
            raise IndexError('Index out of range.')

    def clear(self):
        """
        Removes the head and tail references, and resets the list index. Thus,
        clearing all nodes from the list.
        """
        self._head = None
        self._tail = None
        self._idx = 0

    def append(self, node_or_value):
        """ 
        Appends the node to the end of the list, assigns its respective index and 
        moves self._tail to point to it.

        If a value is passed as a parameter instead, a SSLL_Node object is created
        from it and is submitted to the process described above.
        """
        node = self._nodify(node_or_value)
        node._idx = self._idx
        self._idx += 1

        if not self._head:
            self._head = node
            self._tail = node
        else:
            self._tail._next = node
            self._tail = node

    def prepend(self, node_or_value):
        """ 
        Appends a node in front of the list, assigns index 0 to it, links
        it to the former first node, moves the head to point to this new node
        and reindexes the whole list. 

        If a value is passed as a parameter instead, a SSLL_Node object is created
        from it and is submitted to the process described above.
        """
        node = self._nodify(node_or_value)
        node._idx = 0
        node._next = self._head
        if not self._head:
            self._tail = node
        self._head = node
        self._idx += 1
        self._reindex(node, 0)

    def insert(self, node_or_value, position): 
        """ 
        Inserts a node in the specified index position, assigning the
        former node at that position as this new node _next field. 

        If the insertion is at the front, self._head is reassigned to that
        node. If it is at the back, self._tail is adjusted accordingly.
        'START' and 'END' can be used as position values to specify the 
        start or end of the list respectively.

        After the insertion, from this new node onwards, the list is 
        reindexed, and self._idx is adjusted accordingly.

        If a value is passed as a parameter instead, a SSLL_Node object is created
        from it and is submitted to the process described above.
        """
        if type(position) == str:

            if position.lower() == 'end': 
                position = self._tail._idx + 1
            elif position.lower() == 'start':
                position = 0
            else:
                raise ValueError('Only "start" and "end" are valid string parameters.')

        node_to_move, node_behind = self._find_by_index(position)
       
        if not node_to_move and not node_behind:

            if position == 0 and not self._head:
                node = self._nodify(node_or_value)
                node._idx = self._idx
                self._head = node
                self._tail = node
                self._idx += 1
                return
            else:
                raise IndexError('Index out of range')

        node = self._nodify(node_or_value)

        if not node_to_move and node_behind and position == self._tail._idx +1:
            node_behind._next = node
            self._tail = node
            node._idx = self._idx
            self._idx += 1
            node._next = None
        else:
            assert position <= self._tail._idx, \
                "Index out of range."

            new_node_idx = node_to_move._idx
            node._next = node_to_move

            if node_to_move is self._head:
                self._head = node
            else:
                node_behind._next = node

            self._idx += 1
            self._reindex(node, new_node_idx)

    def pop(self, idx=None):
        """ 
        Removes the node from the list by linking its predecessor _next 
        field to with its successor node. 
        
        It takes the node-to-remove's index as a parameter and returns 
        a reference to that unlinked node.
         
        If the node to be removed is the head, then the _head reference
        is adjusted to point to it. If it is the tail node, then the _tail
        reference is moved to point towards its predecessor.

        self._idx is adjusted accordingly.
        """
        assert self._head, 'List is empty.'

        if idx == None:
            idx = self._tail._idx

        node_to_remove, node_behind = self._find_by_index(idx)

        if not node_to_remove:
            raise IndexError('Index out of range.')

        rtn = node_to_remove

        if not self._head._next:
            self._head = None
            self._tail = None
        elif node_to_remove is self._head:
            self._head = node_to_remove._next
            self._reindex(self._head, 0)
        elif node_to_remove is self._tail:
            self._tail = node_behind
            node_behind._next = None
        else:
            node_behind._next = node_behind._next._next
            self._reindex(node_behind._next, node_to_remove._idx)

        self._idx -= 1
        rtn._idx = None
        rtn._next = None
        return rtn

    def dprint(self, **kwargs):
        """
        Prints the head and tail node references in detail, the list index
        and the list itself.

        If print_all_nodes=True, each node reference will be printed in detail, 
        not only the ones mentioned above.
        """
        print('*** Detailed linked list display ***', '\n')
        print("List current index:", self._idx)

        if not self._head:
            print("Head pointer is null.")
        else:
            print("> Head: idx", self._head.get_index(), "- Value:", self._head.get_value(), \
                "- Next:", self._head.get_next())

        if 'all_nodes' in kwargs.keys():

            if kwargs['all_nodes'] == True:
                head = self._nodify(self._head)

                if head._next:
                    current = self._head._next

                    while current and current is not self._tail:
                        print("- Node: idx", current.get_index(), "- Value:", current.get_value(), \
                            "- Next:", current.get_next())
                        current = current._next

        if not self._tail:
            print("Tail pointer is null.")
        else:
            print("< Tail: idx", self._tail.get_index(), "- Value:", self._tail.get_value(), \
                "- Next:", self._tail.get_next())
        
        print('\n', '*** Lazy linked list display ***')
        print(self)
        print('-' * 80, end='\n')

    def pprint(self):
        """ 
        Prints the list in a horizontal fashion and index order, one object
        at a time.
        """
        current = self._head

        if not current:
            print("Linked list is empty.")
            return "Linked list is empty."

        rtn = ""

        while current:

            if not current._next:
                print(f'Index: {current._idx} - Value: {str(current.value)}')
                rtn += f'Index: {current._idx} - Value: {str(current.value)}'
                break

            print(f'Index: {current._idx} - Value: {str(current.value)}')
            rtn += f'Index: {current._idx} - Value: {str(current.value)}'
            current = current._next

        return rtn

    def split(self, idx):
        """ 
        Splits the list into two halfs, the second one starting from the
        index passed as a parameter.

        If you do not know the index of the node from where to split the
        list, you can use indexOf().

        This method modifies the original list, adjusting self._tail
        reference to point to the predecessor of the node passed as a
        parameter.

        Returns a new SortedSinglyLL object composed of all nodes in the 
        second half of the list, with its own head and tail references.
        """
        assert self._head, 'List is empty.'

        assert idx is not self._head._idx, \
            "Cannot split from head node, it must be from the second node onwards."

        node_to_split, node_behind = self._find_by_index(idx)

        if not node_to_split:
            raise IndexError('Index out of range.')

        self._tail = node_behind
        self._tail._next = None
        self._idx = node_behind._idx + 1

        second_head = node_to_split
        second_list = SortedSinglyLL(second_head)
        second_node_in_new_list = second_head._next

        while second_node_in_new_list:
            second_list.append(second_node_in_new_list)
            second_node_in_new_list = second_node_in_new_list._next

        return second_list

    def clone(self):
        """
        Creates and returns a shallow copy of the linked list.
        """
        assert self._head, 'Cannot clone an empty list.'
        
        clone = SortedSinglyLL()
        current = self._head
        
        while current:
            node = SSLL_Node(current.get_value())
            clone.append(node)
            current = current._next

        return clone


    def _nodify(self, node):
        """ 
        Converts any value that is not an instance of SSLL_Node 
        (Sorted Singly Linked List class), to an object of that class,
        which is returned.
        """
        if not isinstance(node, SSLL_Node):
            node = SSLL_Node(node)

        return node

    def _reindex(self, starting_node, idx):
        """ 
        Reassigns the index values of all linked objects starting
        from starting_node, and counting from idx onwards.
        """
        while starting_node:
            starting_node._idx = idx
            idx += 1
            starting_node = starting_node._next

    def _find_by_value(self, node):
        """ 
        Finds the nodes whose values' repr match the node value attribute.

        Returns a tuple with the node found and its predecessor. Otherwise, 
        it returns a tuple with two None references.

        If a value is passed as a parameter instead, a SSLL_Node object is created
        from it and is submitted to the process described above.
        """
        node = self._nodify(node)
        current = self._head
        previous = current
        values = []

        while current:

            if repr(current.value) == repr(node.value):
                values.append((current, previous))
                previous = current
                current = current._next
            elif current is self._head:
                current = current._next
            else:
                previous = current
                current = current._next
        
        if not values:
            values.append((None, None))

        return values

    def _find_by_index(self, idx):
        """ 
        Finds the node whose _idx matches the one passed as a
        parameter.

        Returns a tuple with the node found and its predecessor.
        Otherwise, it returns a tuple with one None reference and
        the reference to the previous value before the search ended.
        That is, a reference pointing to the last node of the list. 
        """
        current = self._head
        previous = current

        while current:

            if current._idx == idx:
                return current, previous
            elif current is self._head:
                current = current._next
            else:
                previous = current
                current = current._next

        return None, previous

    
    class _SSLL_Iterator:
        """ 
        A lass to generate the iterator object when __iter__ 
        is called. 
        """
        def __init__(self, head):
            self._current = head

        def __iter__(self):
            return self

        def __next__(self):
            if not self._current:
                raise StopIteration
            else:
                value = self._current.value
                self._current = self._current._next
                return value
        

class SSLL_Node:
    """ 
    An outer class to create SSLL_Node objects.

    It is kept outside of the main class itself just to be able to
    create nodes to pass as parameters when constructing a 
    SortedSinglyLL objects.

    However, other objects can be passed as parameters, so this is a
    matter of personal preference.
    """
    def __init__(self, value=None):
        self.value = value
        self._idx = None
        self._next = None

    def __str__(self):
        return str(self.value)

    def get_value(self):
        """ 
        Returns the node value. 
        """
        return self.value

    def get_index(self):
        """ 
        Returns the node assigned index in the linked list or
        None if it does not belong to any. 
        """
        return self._idx
    
    def get_next(self):
        """ 
        Returns the next node of the list. None if no node
        is assigned to self._next field. 
        """
        return self._next


if __name__ == '__main__':


    #######################################################
    ####  Uncomment each segments of code down below,  ####
    ####  one segment at a time, to test the methods.  ####
    #######################################################


    dummy = SSLL_Node(True)
    dummy2 = SSLL_Node("dummy 2")
    dummy3 = SSLL_Node(["dummy 3", True])   

    ssll = SortedSinglyLL('Hello', 1, dummy, {'a': 1}, 0.5, [1,False], {1,"b"}, [])
    ssll2 = SortedSinglyLL('Hello', 1, "Hello", {'a': 1}, dummy2, [1,False], {1,"b"}, "dummy 2")
    ssll3 = SortedSinglyLL('Hello', 1, "asd", {'a': 1}, 0.5, [1,False], {1,"b"}, [])
    ssll4 = SortedSinglyLL('Hello', 1, "asd", {'a': 1}, 0.5, [1,False], {1,"b"}, [])

    # ssll5.dprint()

    # print(len(ssll))                                # __len__

    print(ssll)                                     # __str__

    # for i in ssll:                                  # __iter__
    #     print(i)                                    # /__iter__    

    # print({"a": 1} in ssll)                         # __contains__   
    # print(dummy in ssll)                            #
    # print(["not", "in", "list"] in ssll)            # /__contains__     

    # print(ssll[0])                                  # __getitem__      

    # print(ssll)                                     # __setitem__ 
    # ssll[1] = "Replaced!"                           #
    # print(ssll)                                     # 
    # print("-" * 80)                                 #
    # print(ssll)                                     #
    # ssll[7] = dummy2                                #
    # print(ssll)                                     # /__setitem__

    # print(ssll == ssll2)                            # __eq__
    # print(ssll3 == ssll4)                           # /__eq__

    # print(ssll.get_head())                          # get_head
  
    # print(ssll.get_tail())                          # get_tail

    # print(ssll.get_list_index())                    # get_list_index

    # print(ssll.get_nodes())                         # get_nodes
    # print("-" * 80)                                 #
    # print(ssll.get_nodes(indexed=True))             # /get_nodes

    # ssll[1] = None                                  # set_nodes
    # ssll[ssll.indexOf(ssll.get_tail())[0]] = None   #
    # print(ssll)                                     #
    # ssll.set_nodes("Overwrite off", overwrite=False)#
    # print(ssll)                                     #
    # print('-' * 80)                                 #  
    # ssll[1] = None                                  #
    # ssll[ssll.indexOf(ssll.get_tail())[0]] = None   #
    # print(ssll)                                     #
    # ssll.set_nodes("Overwrite on", overwrite=True)  #
    # print(ssll)                                     # /set_nodes

    # ssll.dprint()                                   # dprint
    # ssll.dprint(all_nodes=True)                     # /dprint

    # ssll.pprint()                                   # pprint

    # print(ssll2.indexOf(1))                         # indexOf
    # print(ssll2.indexOf("Hello"))                   #
    # print(ssll2.indexOf(dummy2))                    #
    # print(ssll2.indexOf("Not in list"))             # /indexOf

    # print(ssll.is_empty())                          # is_empty
    # ssll.clear()                                    #
    # print(ssll.is_empty())                          # /is_empty

    # print(ssll.valueOf(3))                          # valueOf

    # print(ssll)                                     # clear
    # ssll.clear()                                    #
    # print(ssll)                                     # /clear

    # print(ssll)                                     # append
    # ssll.append("Last!")                            #
    # print(ssll)                                     # /append

    # print(ssll)                                     # prepend
    # ssll.prepend("First!")                          #
    # print(ssll)                                     # /prepend

    # print(ssll)                                     # insert
    # ssll.insert("Squeezing!", 2)                    #
    # print(ssll)                                     #
    # print("-" * 80)                                 #
    # print(ssll)                                     #
    # ssll.insert(dummy3, 'END')                      #
    # print(ssll)                                     #
    # print("-" * 80)                                 #
    # print(ssll)                                     #
    # ssll.insert("First", 'START')                   #
    # print(ssll)                                     # /insert

    # print(ssll)                                     # pop
    # node_4 = ssll.pop(3)                            #
    # print(node_4)                                   #
    # print(ssll)                                     #
    # print("-" * 80)                                 #
    # print(ssll)                                     #
    # tail_node = ssll.pop()                          #
    # print(tail_node)                                #
    # print(ssll)                                     #
    # print("-" * 80)                                 #
    # print(ssll)                                     #
    # dummy_ref = ssll.pop(dummy.get_index())         #
    # print(dummy_ref)                                #
    # print(ssll)                                     #
    # print("-" * 80)                                 #
    # print(ssll)                                     #
    # ssll.insert(dummy_ref, 'end')                   #
    # print(ssll)                                     # /pop

    # print(ssll)                                     # split
    # split_ssll = ssll.split(dummy.get_index())      #
    # print(ssll)                                     #
    # print(split_ssll)                               #
    # print("-" * 80)                                 #
    # further_split = split_ssll.split(3)             #
    # print(ssll)                                     #
    # print(split_ssll)                               #
    # print(further_split)                            # /split

    # print(ssll)                                     # clone
    # ssll_clone = ssll.clone()                       # 
    # print(ssll)                                     #
    # print(ssll_clone)                               # /clone

    # print(dummy.get_value())                        # get_value
    # print(dummy2.get_value())                       #
    # print(dummy3.get_value())                       # /get_value

    # print(dummy.get_index())                        # get_index
    # print(dummy2.get_index())                       # 
    # print(dummy3.get_index())                       # /get_index

    # print(dummy.get_next())                         # get_next
    # print(dummy2.get_next())                        # 
    # print(dummy3.get_next())                        # /get_next