class MSCDLL:
    """
    A Multi-Sorted-Circular-Doubly-Linked-List Abstract Data Structure.

    > Multi : any of its nodes can be linked to any other MSCDLL instances at the 
        same time, allowing chains of lists to be connected in many ways.
    > Sorted : nodes keep their added order (links to each other), and the order 
        is maintained when adding/replacing/removing nodes.
    > Circular : the last node in the list is linked to the first one, and vice-versa.
    > Doubly Linked List : each node holds a reference to the next and the back 
        nodes in the list.

    Additionally, many lists can listen to events on other lists via an observer 
    and react accordingly, using a Pub-Sub (or Observer) design pattern. 
    
    This is both convenient if you would like to call for operations in all lists 
    at once, and necessary for the integrity of the whole chain if you were to call 
    for actions in one list that affect other ones. Like removing a node in one 
    list while it is linked to a different list, for example. Removing it will cause 
    no problems in the list it was called from for its removal, but would break the 
    integrity in other lists that share that node if they are not commanded to relink 
    their nodes accordingly.

    Each method and attribute is commented in detail. Please, do refer to them to 
    check what they do and how they do it.

    Attributes :
        _head              _id              _length              _observer
    
    Main methods :
        __init__           __len__          __setitem__          __del__
        __repr__           __getitem__      __eq__               __str__                                   
        __iter__           get_head         get_name             get_nodes
        get_observer       get_observer_subscribers              set_name
        set_nodes_values   append           prepend              insert
        pop                remove           clear                replace
        split              clone            indexOf              valueOf
        reverse            subscribe        unsubscribe          is_empty
        iter_reverse       dprint

    Methods linked to the observer to call for all lists :
        linked_append          linked_prepend           linked_insert
        linked_pop             linked_remove            linked_clear
        linked_replace         linked_split             linked_clone
        linked_reverse         linked_indexOf           linked_valueOf
        linked_split           linked_set_nodes_values  linked_get_head
        linked_get_nodes       linked_is_empty      

    Helper methods:
        _assert_subscription    _nodify    _get_node_by_idx    _get_node_by_name
                
    Author: Renzo Nahuel Murina Cadierno
    Contact: nmcadierno@hotmail.com
    Github: github.com/RenzoMurinaCadierno
    """

    def __init__(self, *args, **kwargs):
        """
        Initalizes the MSCDLL: sets the head reference to None, its length to 0, 
        its name (id) to its memory address casted as int, and its observer instance
        to None.

        args (MSCDLLNode|any): the nodes or values (which will be converted to nodes),
            to link to this list. They will be added in the order they are passed. 
            In case of no given args, the list will be empty. Nodes or values can be
            appended/prepended/inserted/replaced/popped/removed later using the 
            methods provided.

        kwargs:
            name (str|int): the name (id) to use instead of the one set by default.
            observer (MSCDLLObserver): the observer instance this list will be
                subscribed to. Can be None and assigned later on with subscribe().
        """

        # set head reference to None, length to 0, default name to its id in
        # memory, its observer field to None, and a link reference to bind 
        # the nodes passed as args, if any.
        self._head = None
        self._length = 0
        self._id = id(self)
        link = self._head
        self._observer = None

        # set self name and subscribe to observer, if provided
        if 'name' in kwargs:
            self._id = kwargs['name']

        if 'observer' in kwargs:
            kwargs['observer'].subscribe(self)
            # self._observer = kwargs['observer']

        # cast each arg to a valid node if it is not one yet, and place 
        # them in the smcdll, properly linked
        for arg in args:

            arg = self._nodify(arg)

            if not self._head:
                self._head = arg
                arg.set_back(self, self._head)
                arg.set_next(self, self._head)
                link = arg
                self._length +=1
            else:
                link.set_next(self, arg)
                arg.set_back(self, link)
                link = arg
                link.set_next(self, self._head)
                self._length += 1
        
        # on lists with length > 1, the back refernce for the head node
        # would be unlinked, so, link it here
        if self._length > 1:
            self._head.set_back(self, link)

    def __iter__(self):
        return _MSCDLLIterator(self)

    def __del__(self):
        """ 
        Deletes all nodes and its references to each other from the list, and
        releases the variable pointing to the list, triggering the garbage collector
        and eliminating the list completely.

        Keep in mind that this method will not work if other reference is pointing
        to the list, or to any of its nodes that link to it by its _links field.
        There must be only one variable pointing to the list and nothing else bound
        to it or to its nodes for del to work.

        If you want to reset the list (delete its nodes, set its length to 0 and head
        reference to None), use clear() instead.
        """
        # make sure no references are pointing to the list.
        for _ in range(len(self)):
            self.pop(index=0)

    def __eq__(self, mscdll):
        """
        Compares each node's values in self and in the MSCDLL instance passed as a 
        parameter, like a regular Python list's __eq__ method. 
        However, the comparison is not a type-based one, which means truthy and falsy 
        values will be considered the same. If True and 1 are encountered, the check 
        will result in True.
        """
        # lengths are different, they are not equal
        if len(self) != len(mscdll) or not isinstance(mscdll, MSCDLL):
            return False
        elif len(self) == 0 and len(mscdll) == 0:
            return True
        
        # set up the references to trasverse the lists forward and backwards
        self_forwardtrack = self._head
        self_backtrack = self._head.get_back(self)
        mscdll_forwardtrack = mscdll._head
        mscdll_backtrack = mscdll._head.get_back(mscdll)
        
        for _ in range(len(self) // 2 + 1):
            
            # if any compared node trasversing on the same index from the back or the
            # front have different values, they are not equal
            if self_forwardtrack.value != mscdll_forwardtrack.value:
                return False
            
            if self_backtrack.value != mscdll_backtrack.value:
                return False

            # move to each node's next or back references accordingly
            self_forwardtrack = self_forwardtrack.get_next(self)
            self_backtrack = self_backtrack.get_back(self)
            mscdll_forwardtrack = mscdll_forwardtrack.get_next(mscdll)
            mscdll_backtrack = mscdll_backtrack.get_back(mscdll)

        # all values are the same, return True
        return True

    def __getitem__(self, idx):
        return self._get_node_by_idx(idx)

    def __len__(self):
        return self._length

    def __setitem__(self, idx, node_or_value):
        # __setitem__ calls for insert(), and insert targets a non-existent node 
        # after the last one on the list if len(self) is passed as idx. Since
        # we do not want this behavior while replacing an item using this method,
        # a restriction on idx to exclude len(self) must be applied.
        if idx == len(self):
            raise IndexError('Index out of range.')

        return self.insert(node_or_value, idx, overwrite=True)

    def __repr__(self):
        return str(self._id)

    def __str__(self):
        if not self._head:
            return '<(LL)> <(/LL)>'
        head = self._head
        string = '<(LL)> '
        while True:
            string += f'{str(head.value)} <- '
            head = head.get_next(self)
            if head is self._head:
                break
        string += '\b\b\b</(LL)>'
        return string

    def clear(self):
        """
        Sets each node's 'back' and 'next' references as well as the list's head reference 
        to None, and sets the list's length to 0. This action will reset (or clear) the list.
        Differently to __del__(), the list will be cleared out regardless of any references
        pointing at it.
        """
        self.__del__()

    def get_name(self):
        """
        Returns the linked list's name (id).
        """
        return self._id

    def get_head(self):
        """
        Returns a reference to the head node of the list.
        """
        return self._head

    def set_name(self, name):
        """
        Changes the linked list name (id), which also includes all of its nodes _link 
        keys that store this list's name.
        """
        # for each node in self:
        for node in self:

            # create a key for the new list name
            node._links[name] = {}

            # set its value to the next and back fields of the original name
            for key, value in node._links[self._id].items():
                node._links[name][key] = value

            # destroy the previous name's links
            node._links.pop(self._id)

        # change the name of the list
        self._id = name

    def dprint(self, **kwargs):
        """
        Prints the MSCDLL instance in a 'debugging' fashion.

        Will display the instance's name (id), observer, length, lazy representation (__str__),
        and a summary of its nodes (index in list, value and links).

        kwargs:
            show_details (bool): If True, instead of a summary of its nodes, it will call for
                pprint() on each of them, printing them out in detail. 
        """
        idx = 0
        current = self._head
        show_details = False

        if kwargs:
            if 'show_details' in kwargs:
                show_details = True if kwargs['show_details'] else False

        print('*' * 80)
        print('MSCDLL GLOBAL INFORMATION'.center(80), '\n')
        print('MSCDLL name (id):', self._id)
        
        if isinstance(self._observer, MSCDLLObserver):
            print('MSCDLL observer:', self._observer._id)
        elif not self._observer:
            print('MSCDLL observer: None')
        else:
            print('MSCDLL observer: Invalid observer. Must be an instance of SMCDLLObserver.')

        print('MSCDLL length:', self._length)

        if not current:
            print('MSCDLL is empty.')
            print('*' * 80)
        
        else: 
            print('*' * 80)
            print('NODES\' DETAILS'.center(80), '\n')
            
            while True:

                if show_details:
                    print
                    print(f'Node at list index {idx}:')
                    current.pprint()
                else:
                    print('List index:', idx, '- Value:', current.value, \
                        '- Back:', current.get_back(self), \
                        '- Next:', current.get_next(self), \
                        end=' <- (HEAD)\n' if current is self._head else '\n')
                    
                current = current.get_next(self)
                idx += 1

                if current is self._head:
                    print('*' * 80)
                    break
                else:
                    print('-' * 80)
        
        print('LAZY MSCDLL DISPLAY'.center(80), '\n')
        print(self)
        print('*' * 80)

    def indexOf(self, node_or_value) -> tuple:
        """
        Takes value (or node, in which case it will take its value) and searches in the list for 
        all nodes whose values match with it. It returns a tuple containing the indexes in the 
        linked list where the matching nodes were found.

        Note that this method is designed to consider truthy and falsy values as the same 
        (which means True and 1 will be no different from each other). 
        If you want to differentiate between them, use get_nodes() instead.

        Parameters:
            node_or_value (MSCDLLNode|any): the value (or node to take the value from) to filter 
                the nodes in the linked list.

        Returns: 
            (tuple): a tuple containing the indexes where the matching nodes were found.
        """
        # nothing to index if there are no nodes
        if not self._head:
            return ()

        # is it a node with self's next and back references?
        # Try to call for the references. If they respond, then it is a node. Leave it as it is.
        # If any of the two exceptions rise, then we passed a value. Convert it to a node
        try:
            node_or_value._links[self._id]['next']
            node_or_value._links[self._id]['back']
            node = node_or_value
        except (KeyError, AttributeError):
            node = self._nodify(node_or_value)

        # prepare all variables to traverse the list and save the encountered indexes
        backtrack = self._head.get_back(self)
        forwardtrack = self._head
        count = 0
        indexes = []

        while count < self._length / 2:

            # traverse forwards and backwards at the same time -O(log n)-.
            # append any list node's index whose value matches the one in 'node'
            if backtrack.value == node.value:
                indexes.append(self._length - 1 - count)

            if forwardtrack.value == node.value \
              and forwardtrack is not backtrack:
                indexes.append(count)

            # set the next nodes to be traversed and increase the index count
            backtrack = backtrack.get_back(self)
            forwardtrack = forwardtrack.get_next(self)
            count += 1
        
        # return a tuple with all found indexes
        return tuple(sorted(indexes))

    def is_empty(self) -> bool:
        """
        Returns True is the list is empty. False othewise.
        """
        return self._head is None

    def valueOf(self, idx: int):
        """
        Takes an index value, searches on the list to find the node in that given 
        index and returns it.

        Parameters:
            idx (int): the index to search on the list. Accepts negative integers, 
                like regular Python lists.

        Returns:
            (MSCDLLNode): a reference to the node at the given index in the list.
        """
        return self._get_node_by_idx(idx)
    
    def iter_reverse(self):
        """
        Returns an _MSCDLLReverseIterator instance, which can be used as an iterator that 
        traverses the list in reverse order.
        """
        return _MSCDLLReverseIterator(self)

    def append(self, node_or_value, **kwargs) -> tuple:
        """
        Takes a node or a value (which it automatically converts to a valid node), and appends it 
        to the linked list. It uses insert() to do so, passing 'end' as a positional argument
        and kwargs['overwrite'] as False.

        Returns:
            (tuple): A tuple containing the appended node's position and a reference to it.
        """
        kwargs['overwrite'] = False
        return self.insert(node_or_value, 'end', **kwargs)

    def prepend(self, node_or_value, **kwargs) -> tuple:
        """
        Takes a node or a value (which it automatically converts to a valid node), and prepends 
        it to the linked list. It uses insert() to do so, passing 0 as a positional argument
        and kwargs['overwrite'] as False. Head node is set to this new node.
        
        Returns:
            (tuple): A tuple containing the prepended node's position and a reference to it.
        """
        kwargs['overwrite'] = False
        return self.insert(node_or_value, 0, **kwargs)

    def replace(self, node_or_value, **kwargs):
        """
        Using the condition passed as kwarg, it searches on the MSCDLL for instances of nodes 
        that match with it and replaces them with the node or value (which will be casted to 
        a valid MSCDLLNode) passed as parameter.
        
        Keep in mind not to replace a node on the list with a reference of itself, or with
        another node that is already on the list. This might cause conflicts while traversing.

        kwargs:
            by_position (int): the index to look for the node to replace by its index position 
                in the list.
            by_name (int|str): the name (id) to look for the node to replace, by its name.
            by_value (any): the value to look for the node to replace, by its value.
        
        Returns:
            (list): a list of tuples containing the index where the node to replace was found,
                the replaced node and the replacement node.
        """
        # 'by_node', 'by_name', 'by_position' or 'by_value' are accepted as kwarg, and only
        # one of them per method call.
        if [
            'by_node' in kwargs, 'by_name' in kwargs, 'by_position' in kwargs, 'by_value' in kwargs
        ].count(True) > 1:
            raise KeyError(
                '\'linked_replace\' method accepts one of these three kwargs at a time: '+
                '\'by_position\', \'by_node\', \'by_name\', \'by_value\'')

        # replace calls for insert(), and always replaced the node it targets
        kwargs['overwrite'] = True

        # insert accepts 'position' as a kwarg to target the index, so pass this 'by_position'
        # kwarg and call for insert() which will return a tuple with the replaced node and its idx
        if 'by_position' in kwargs:
            kwargs['position'] = kwargs['by_position']
            return self.insert(node_or_value, **kwargs)

        else:

            # create a list to store all of the replaced nodes
            replaced_nodes = []

            # use get_nodes and pass the respective kwargs to get the node tuples with the indexes
            # and nodes to replace
            if 'by_name' in kwargs:
                index_node_tuples = self.get_nodes(names=[kwargs['by_name']])
            elif 'by_node' in kwargs:
                index_node_tuples = self.get_nodes(names=[kwargs['by_node']._id])
            elif 'by_value' in kwargs:
                index_node_tuples = self.get_nodes(values=[kwargs['by_value']])

            # for each of those tuples, call for insert() passing the index of the node as 'position'
            # kwarg, and append the returning tuple to the replaced nodes list
            for item in index_node_tuples:
                kwargs['position'] = item[0]
                replaced_nodes.append(self.insert(node_or_value, **kwargs))

            # return the list containing the replaced nodes and its former indexes.
            return replaced_nodes

    def get_nodes(self, **kwargs) -> list:
        """
        Takes a kwarg as a filter, searches the list and returns the nodes that match that 
        filter in a list of tuples in the format: (node index in list, node).

        kwargs:
            indexes (list|tuple): a list or tuple containing the indexes to filter the 
                linked list. More than one index can be passed in the list|tuple.
            names (list|tuple): a list or tuple containing the node names to filter the 
                linked list. More than one node name can be passed in the list|tuple.
            values (list|tuple): a list or tuple containing the values to filter the 
                linked list. More than one value can be passed in the list|tuple. 
                Contrary to valueOf(), 'values' kwarg will differentiate between truthy 
                and falsy values. True will not be the same as 1.

        Returns:
            (list): a list containing the nodes that match that filter in a list of tuples 
                in the format: (node index in list, node).
        """
        nodes = []
        
        if kwargs:

            # Only one kwarg per method call
            if len(kwargs) > 1:
                raise KeyError('You can only pass one kwarg at a time.')
            
            # kwarg's value must be passed as a tuple or list
            for value in kwargs.values():

                if type(value) is not tuple and type(value) is not list:
                    raise TypeError('Must pass kwarg value(s) in a list or tuple.')
            
            # case kwargs['values']: search the list for any nodes whose values equal the ones
            # in kwargs['values'], append a tuple with its list index and node reference to
            # 'nodes' list and return that list when done.
            if 'values' in kwargs:

                for i, node in enumerate(self):

                    for value in kwargs['values']:

                        if repr(node.value) == repr(value):
                            nodes.append((i, node))

                return nodes

            # case kwargs['name']: same as kwargs['values'], but searches for node names (id)
            # instead. If more than one node share the same name, they are all returned.
            elif 'names' in kwargs:

                for i, node in enumerate(self):

                    for name in kwargs['names']:

                        if node._id == name:
                            nodes.append((i, node))

                return nodes

            # case kwargs['indexes']: same as kwargs['values'], but searches by list index.
            elif 'indexes' in kwargs:

                for i, node in enumerate(self):

                    for idx in kwargs['indexes']:

                        if idx < 0:
                            idx = self._length + idx

                        if idx == i:
                            nodes.append((i, node))

                return nodes

            # exception for any wrong kwarg
            raise ValueError(
                'You might have passed the wrong kwarg. '+
                'Options are: \'names\', \'values\' or \'indexes\'.'
            )

        # no kwargs passed when calling for the method, append all nodes in a tuple
        # format (list index, node reference) to 'nodes' list and return it
        else:

            for i, node in enumerate(self):
                nodes.append((i, node))
            
            return nodes

    def set_nodes_values(self, value, **kwargs):
        """
        Gets all nodes in the MSCDLL instance filtered by the respective kwarg and
        replaces their values for the one passed as parameter.

        kwargs:
            indexes (list|tuple): the same one as get_nodes().
            names (list|tuple): the same one as get_nodes().
            values (list|tuple): the same one as get_nodes().

        Returns:
            (list): a list containing all of the MSCDLL nodes with the changed
            values in the format of: (node index in list, node).
        """
        nodes_to_set_values = self.get_nodes(**kwargs)
        
        for node_tuple in nodes_to_set_values:
            node_tuple[1].value = value

        return nodes_to_set_values

    def pop(self, **kwargs):
        """
        Filters the list according to the passed kwarg and removes the node in the MSCDLL 
        instance that matches that kwarg. It returns a reference to that removed node, or
        None if the node was not found.

        The node's _links reference to the list will be cleared, and its neighbour nodes
        inside the linked list will be linked to each other, effectively unlinking the
        target node.

        This method differs from remove() in a way that it matches only one node, and not
        several instances. However, the search will stop as soon as the target is found,
        which means it is potentially more speed-efficient.

        kwargs:
            name (str|int): the name (id) of the node to look for and remove from the MSCDLL.
            index (int): the index where the node to remove is located.
        
        Returns:
            (MSCDLLNode): a reference to the removed node.
        """
        # pop by name only works if nodes have different names (id)
        target = None

        # validate kwarg and get the target node depending on it
        if kwargs:

            if len(kwargs) > 1:
                raise Exception(
                    'You must provide a node name or a list index as a kwarg, not both at the same time.'
                )

            elif 'name' in kwargs:
                target = self._get_node_by_name(kwargs['name'])

            elif 'index' in kwargs:
                target = self._get_node_by_idx(kwargs['index'])

            else:
                raise KeyError('Provide a valid kwarg. Options are: \'name\' and \'index\'.')

        # node not found on the trasversal
        if not target:
            return None

        # if the list consists of only one node, remove the node
        if len(self) == 1:
            removed_node = self._head
            self._head._links.pop(self._id)
            self._head = None
        
        # there is more than one node in the list, link its previous node to the one after it,
        # the one after it to the one behind, and unlink its own back and next references.
        # If the removed node is self._head, move that pointer to the node after it.
        # Also, remove the list's name from the removed node's _link dictionary.
        else:
            removed_node = target

            if target is self._head:
                self._head = target.get_next(self)

            target.get_back(self).set_next(self, target.get_next(self))
            target.get_next(self).set_back(self, target.get_back(self))
            target._links.pop(self._id)
        
        # adjust the list's length and return a reference to the removed node.
        self._length -= 1
        return removed_node

    def remove(self, **kwargs) -> list:
        """
        Given the passed kwarg, it checks on the list for any matching nodes and removes 
        them, setting their 'back' and 'next' list references to None, and linking their
        previous node to their next node. It returns a list of tuples with those removed
        nodes in the format: (index where node was found, removed node).
        
        This method differs from pop() as it matches several instances of nodes instead
        of one, and returns their list index. The drawback is that it requires a full list
        traversal.

        kwargs:
            indexes (list|tuple): a list or tuple containing the nodes' indexes (int) to 
                filter the linked list. A node whose list index matches any one of those 
                will be removed. 
            names (list|tuple): a list or tuple containing the nodes' names (id) (str|int) 
                to filter the linked list. A node whose name matches any one of those will 
                be removed.
            values (list|tuple): a list or tuple containing the nodes' values (any) to 
                filter the linked list. A node whose value matches any one of those will 
                be removed.  
        
        Returns:
            (list): a list of tuples with the removed nodes in the format: (index where 
                node was found, removed node).
        """
        # 'name', 'values' or 'indexes' are accepted as kwargs. Only one per method call
        assert ['names' in kwargs, 'values' in kwargs, 'indexes' in kwargs].count(True) == 1, \
            'You can only pass one kwarg at a time: \'indexes\', \'names\' or \'values\'.'

        removed_nodes = []  # list to store the removed nodes to return later
        indexes = []        # list to store the already used node indexes
        offset = 0          # keeps track of the offset when returning indexes while removing nodes
        last_index = 0      # keeps the last index used to decide if offset is applied or not

        # use get_nodes() in all three cases to retrieve the node list we are to remove
        if 'names' in kwargs:
            node_tuples = self.get_nodes(names=kwargs['names'])
        elif 'values' in kwargs:
            node_tuples = self.get_nodes(values=kwargs['values'])
        elif 'indexes' in kwargs:
            node_tuples = self.get_nodes(indexes=kwargs['indexes'])
        
        # for each returned tuple:
        for j, node_tuple in enumerate(node_tuples):

            # if the node index was called before, do not remove it again
            if node_tuple[0] in indexes:
                continue

            # if the node index is <= to the last tuple index and it is not the first
            # time we call for the loop, then remove the node taking into consideration
            # the offset (if we removed nodes before in the loop), and to calculate the
            # index to be returned in the tuple
            if node_tuple[0] <= last_index and j != 0:
                removed_nodes.append((node_tuple[0] - offset, self.pop(index=node_tuple[0] - offset)))
            
            # do the same, but we do not have the need to adjust the returning index
            else:
                removed_nodes.append((node_tuple[0], self.pop(index=node_tuple[0] - offset)))
            
            # we removed a node, so add 1 to the offset for the following iteration. Also,
            # set the current node index as last_index, and append it to indexes list (of
            # already used indexes which need to be skipped if called in following iterations)
            offset += 1
            last_index = node_tuple[0]
            indexes.append(node_tuple[0])

        # all nodes were removed, return a list with them
        return removed_nodes

    def clone(self, **kwargs):
        """
        Creates a shallow copy of the linked list and returns a reference to it.

        kwargs:
            clone_list_name (string|int): the name (id) to assign to the cloned list.
            bind_to_self (bool): On True, each cloned node and original list's node will keep 
                a link field reference to their respective counterpart's 'back' and 'next' nodes. 
                On false, the clone will be a pure shallow copy, which means that its nodes will 
                ony keep a field reference to their own 'back' and 'next' nodes. The original 
                list's nodes will also be unbound from the cloned ones.
        """
        clone_list = MSCDLL()     # create the MSCDLL clone
        clone_list._id = f'{self._id}_clone_{id(clone_list)}'
        bind_to_self = False      
        current = self._head
        flag = False

        if kwargs:

            # set its id. If you are binding to self below, keep in ming the clone list 
            # must not share the name of another list with any node(s) that are linked to 
            # it. This includes lists in self._observer._subscribers
            if 'clone_list_name' in kwargs:
                clone_list._id = kwargs['clone_list_name']

            # set node binding with original list's links to True
            if 'bind_to_self' in kwargs:
                if kwargs['bind_to_self']:
                    bind_to_self = True 

        # trasverse the original list forwards
        while current:

            # first case is head node, set flag to True and continue
            if current is self._head and not flag:
                flag = True
            
            # if we hit head node again, the list was trasversed. We are finished
            elif current is self._head:
                break
            
            # create a node with the clone's _nodify method
            clone_node = clone_list._nodify(current.value)

            # set the node's name to a default one. We add the clone_list's id
            # to avoid node name collision if clone() is called again from the
            # same original MSCDLL
            clone_node._id = f'{current._id}_of_{clone_list._id}'
            
            # The node is configured, append it to clone_list
            clone_list.append(clone_node)

            # if we are to bind that node with the same links as the node in
            # the original list, then add all of its links to it. Also, add the
            # cloned node links to the original node links. 
            if bind_to_self:
                
                for key, value in current._links.items():
                    clone_node._links[key] = value

                current._links[clone_list._id] = clone_node._links[clone_list._id]

            # continue with the next node in the original list
            current = current.get_next(self)

        # list is cloned, return a reference to it
        return clone_list

    def extend(self, mscdll, unlink_nodes=True, check_for_repeated_nodes=True):
        """
        Extends the MSCDLL instance with another valid one. Like Python's list's extend().
        
        The head node of the MSCDLL instance passed as a parameter (mscdll) will be linked 
        to the last node of the original list and all of mscdll nodes's _links dictionaries
        will be modified to contain a reference to the original list with their own 'back'
        and 'next' fields.

        Keep in mind that lists will be fused, which means that all nodes will share the
        same list. If a node is in both lists at the same time before they are fused together,
        the lists will be combined regardless, but any operation that require a traversal will
        either rise an exception or fall in an infinite loop. If you are not sure whether a 
        node is shared by both lists, use check_for_repeated_nodes parameter.

        Parameters:
            mscdll (MSCDLL): the MSCDLL instance the original list will be extended with.
            unlink_nodes (bool): on True, each one of mscdll nodes will lose their mscdll
                key in their _links dictionaries, effectively unlinking them from it, which
                empties that list. On False, the nodes will keep the reference in their
                _links, which means mscdll will remain as a non-empty linked list.
            check_for_repeated_nodes (bool): On True, each node in both lists will be compared
                to each other in an attempt to find an instance of a node that is in both lists
                at the same time (repeated). If one is encountered, an exception will rise and
                extend() will abort. This method is speed-inefficient, and that is why there is
                the option not to use it if you are certain that both lists contain unique nodes.
        """
        # both lists must be type mscdll
        if not isinstance(mscdll, MSCDLL):
            raise TypeError('An instance of MSCDLL can only extend an instance of its same class.')

        # case 0: any of the two lists have no nodes. Cannot extend empty lists
        assert self._head and mscdll._head, 'You cannot extend empty lists.'

        # if you are sure one node is not in both lists at the same time, set this arg to False.
        # Keep in mind that if you do so and there is a node repetition, the lists will be fused
        # anyway and a KeyError will rise each time you perform any operation that requires access 
        # to a node in the list passed as arg when calling for this method.
        # I added the option to tell the program to evade the check since it is costly: O(2n + m), or
        # O(nm) if amortized. 'n' is the total nodes of the shortest list, and 'm' of the longest one
        if check_for_repeated_nodes:

            # Given their length, differentiate between the shortest and the longest lists
            shortest_list = self if self._length <= mscdll._length else mscdll
            longest_list = mscdll if mscdll._length >= self._length else self
            
            # the list to hold all nodes to compare now is guaranteed to hold the nodes of the shortest list.
            # This might not seem much, but remember that list comprehensions take O(n) time, not considering
            # the amortized cost. A full traversal is still required. Cost is O(2n), or O(n+1) if amortized
            self_nodes = [node[1] for node in shortest_list.get_nodes()]

            # traverse through the nodes of the longest list and compare each node with all nodes in the
            # smaller list. If an instance of the same node is found in both lists, rise an error.
            # Otherwise, we can assume both lists are valid ones to perform an expansion. Cost is O(m)
            for node in longest_list:

                if node in self_nodes:
                    raise ValueError(
                        'A node cannot be in more than one list at the same time while performing an extension.'
                    )
        
        # make references more readable
        self_first = self._head
        self_last = self._head.get_back(self)
        mscdll_first = mscdll._head
        mscdll_last = mscdll_first.get_back(mscdll)

        # if there is no reference to self in the list-to-be-extended's 
        # (mscdll's) first and last nodes, create them
        if not 'mscdll' in mscdll_first._links:
            mscdll_first.set_MSCDLL_links(self)

        if not 'mscdll' in mscdll_last._links:
            mscdll_last.set_MSCDLL_links(self)

        # if any of the lists have only one node (cases 1, 2 and 3)
        if len(self) == 1 or len(mscdll) == 1:

            # case 1: the original list has one node and the one passed as arg, more than one
            if len(self) == 1 and len(mscdll) > 1:

                # link the next reference to the node in the original list to the first node 
                # of the extension list, and create the corresponding links in the first node
                # of the extension list
                self_first.set_next(self, mscdll_first)
                mscdll_first.set_back(self, self_first)
                mscdll_first.set_next(self, mscdll_first.get_next(mscdll))
                
                # do the same for the back reference of the single node in the original list
                # and for the last node of the extension list.
                self_first.set_back(self, mscdll_last)
                mscdll_last.set_next(self, self_first)
                mscdll_last.set_back(self, mscdll_last.get_back(mscdll))

                for node in mscdll:
                    
                    # first and last nodes in extension lists are already configured
                    if node is mscdll_first or node is mscdll_last:
                        continue
                    
                    # create the links to the original list on each node in the extension list
                    node._links[self._id] = {}
                    node.set_next(self, node.get_next(mscdll))
                    node.set_back(self, node.get_back(mscdll))
                    
                    # and we are to unlink from the extension list, remove the reference to it
                    if unlink_nodes:
                        node._links.pop(mscdll._id)

                # if we are to unlink, do the same as before for the first and last nodes
                # of the extension list, which did not enter in the loop
                if unlink_nodes:
                    mscdll_first._links.pop(mscdll._id)
                    mscdll_last._links.pop(mscdll._id)

            # case 2: the original list has more than one node and the one passed as arg, one
            elif len(self) > 1 and len(mscdll) == 1:

                # set the back reference of the first node in the original list to point to
                # the single node in the extension list, and that node to point to the first
                # one in the original list
                self_first.set_back(self, mscdll_first)
                mscdll_first.set_next(self, self_first)

                # do the same for the next reference of last node of the original list.
                self_last.set_next(self, mscdll_first)
                mscdll_first.set_back(self, self_last)

                # if we are to unlink the nodes from the extension list, there is only one
                # node, so, just delete its self list links.
                if unlink_nodes:
                    mscdll_first._links.pop(mscdll._id)
            
            # case 3: length of both lists is 1
            else:
                self_first.set_next(self, mscdll_first)
                self_first.set_back(self, mscdll_first)
                mscdll_first.set_next(self, self_first)
                mscdll_first.set_back(self, self_first)

                if unlink_nodes:
                    mscdll_first._links.pop(mscdll._id)
            
            # in all cases, adjust the length of the original list 
            self._length += mscdll._length

            # and if we unlinked, set the extension list's head to None and length 
            # to 0, which resets it since it already has no nodes.
            if unlink_nodes:
                mscdll._head = None
                mscdll._length = 0
            
            # done with cases 1, 2 and 3
            return
                   
        # case 4: both lists have more than one node each

        # set both next and back references of the first node in self and last node
        # in mscdll's to point to their new correct fields
        self_first.set_back(self, mscdll_last)
        mscdll_last.set_next(self, self_first)
        mscdll_last.set_back(self, mscdll_last.get_back(mscdll))
        self_last.set_next(self, mscdll_first)

        # do the same for the first node in mscdll and adjust the first node in self's
        # back reference accordingly. We do so last as not to break any links.
        mscdll_first.set_back(self, self_last)
        mscdll_first.set_next(self, mscdll_first.get_next(mscdll))
        self_first.set_back(self, mscdll_last)

        # adjust length to be the combination of both lists
        self._length += mscdll._length

        current = mscdll._head.get_next(mscdll)

        # the first and last nodes of mscdll already have their correct self
        # references in their _links dictionary. All of the middle ones do not.
        # Add them in this while loop.
        # Also, if we are to unlink all nodes from mscdll, we remove the references
        # to that list from all of its nodes.
        while current is not mscdll_last:
            current._links[self._id] = {}
            current.set_next(self, current.get_next(mscdll))
            current.set_back(self, current.get_back(mscdll))
            next_node = current.get_next(mscdll)

            if unlink_nodes:
                current._links.pop(mscdll._id)

            current = next_node

        # if we chose to unlink nodes, head still contains the reference to mscdll.
        # Remove that reference as well as the head pointer, and reset the length.
        # This way, mscdll will be reset to be empty and all of its nodes will be
        # bound to self as an extended list.
        if unlink_nodes:
            current._links.pop(mscdll._id)
            mscdll._head._links.pop(mscdll._id)
            mscdll._head = None
            mscdll._length = 0

    def split(self, idx: int, splitted_list_name=None):
        """
        Splits the MSCDLL instance into two parts, where the second one starts from the 
        node in the original list at the index passed as a parameter.

        The original list is modified. It will contain all of the nodes from index 0 to 
        idx, not inclusive. The splitted list will hold all of the nodes from idx onwards.
        Both lists will be independent from each other.

        Parameters:
            idx (int): the node index from where the splitted list will begin.
            splitted_list_name (str|int): the splitted list name (id). If not given, it
                will default to its memory address id.

        Returns:
            (MSCDLL): a reference to the splitted list. 
        """
        if idx == 0 or idx == -self._length:
            raise IndexError('You can only split from node index 1 onwards.')

        # get the target node where we want to split the list at, the node that comes
        # before it and create an instance of MSCDLL to assign the split list to
        target_node = self._get_node_by_idx(idx)
        target_node_back = target_node.get_back(self)
        splitted_list = MSCDLL()

        # If a name for the splitted list was provided, set it
        if splitted_list_name:
            splitted_list._id = splitted_list_name

        while True:

            # once we reach self._head, the splitted list was trasversed. Break out
            if target_node is self._head:
                break

            # add the splitted list's link key to _links dictionary in the node and
            # append it to the list
            target_node = splitted_list._nodify(target_node)
            splitted_list.append(target_node)

            # assign the head reference of the splitted_list on the first loop
            if not splitted_list._head:
                splitted_list._head = target_node
            
            # save a reference of the target node before erasing the original list's
            # dictionary. We need it later to follow the next and back fields
            # correctly while trasversing. Once that list is popped, then reassign
            # the temporal target node to target node again to continue the loop.
            temp_target_node = target_node.get_next(self)
            target_node._links.pop(self._id)
            target_node = temp_target_node

        # Once finished with the splitted list, recompose the original one. Set the 
        # previous node to the one where the list was split to have its next field 
        # pointing to the original list's head. Set the head's back link to that 
        # previous node, and adjust self._length accordingly
        target_node_back.set_next(self, self._head)
        self._head.set_back(self, target_node_back)

        if idx > 0:
            self._length -= self._length - idx 
        else: 
            self._length = self._length + idx

        # finally, return a reference to the splitted list
        return splitted_list

    def insert(self, node_or_value, position, **kwargs):
        """
        Inserts the node or value (which will be converted to a MSCDLLNode) passed as
        parameter in the specified index position. If 'overwrite' is passed as a kwarg,
        the node found at the given position will be replaced with the node or value
        converted to a node instead.

        Parameters:
            node_or_value (MSCDLLNode|any): the node to insert at the given position,
                or to replace with if you are to 'overwrite' instead. If a value is
                passed instead of a MSCDLLNode, then it will be automatically converted
                to one.
            position (int): the index position where the node is to be inserted in, or
                where the target node to replace is positioned. Negative indexing is 
                accepted, but keep in mind that -1 will insert the node before the last
                one in the list. To position a node at the end of the list, use len(self)
                or 'end'.
        
        kwargs:
            name (str|int): the name (id) of the node to be inserted, or to serve as a
                replacement if 'overwrite' is set to True.
            overwrite (bool): on True, the current node at the index targeted by position
                parameter will be replaced with node_or_value. On False, node_or_value
                will be inserted at that index instead, shifting all following nodes to
                the right by one.
        
        Returns:
            (tuple): a tuple containing the index position where the node was inserted and
                a reference to the inserted node. If kwargs['overwrite'] is True, then the
                tuple will contain the index where the node was inserted, a reference to 
                the replaced node, and a reference to the replacement node now in the list.
        """
        if type(position) is str:
            if position.lower() == 'end':
                position = self._length

        assert type(position) is int, \
            'position must be an integer value, or "end".'

        # overwrite OFF will insert the node in the given position index, shifting 
        # all othernodes to the right.
        # overwrite ON will replace the node in the given position index.
        overwrite = False

        # if node_or_value is anything but a MSCDLLNode instance, convert it to one.
        node = self._nodify(node_or_value)

        if 'name' in kwargs:
            node._id = kwargs['name']
        if 'overwrite' in kwargs:
            if kwargs['overwrite']:
                overwrite = True

        # if the list is empty or we are appending to it
        if not self._head or position == self._length or (position == -1 and overwrite):

            # if the list is empty, set this node as its first one.
            # head, next and back references will point to it.
            if not self._head:
                self._head = node
                self._length +=1
                node.set_back(self, self._head)
                node.set_next(self, self._head)

            # if it is not empty, we are either appending or overwriting at
            # position -1
            else:

                # if we are overwriting at position -1
                if (position == -1 and overwrite) or (position == self._length and overwrite):

                    # if there is only 1 node in the list, just replace it with
                    # this new node. Length of the list is unmodified.
                    if self._length < 2:
                        node_to_replace = self._head
                        self._head = node
                        self._head.set_next(self, node)
                        self._head.set_back(self, node)

                    # the list contains more than one node. Adjust the new node's
                    # next link to head, and its back to node at index -2. Then,
                    # unlink the node at index -1 from the list. Same list length.
                    else:
                        node_to_replace = self._head.get_back(self)
                        node.set_back(self, self._head.get_back(self).get_back(self))
                        node.set_next(self, self._head)
                        self._head.get_back(self).get_back(self).set_next(self, node)
                        self._head.set_back(self, node)

                    node_to_replace._links.pop(self._id)

                    # return a reference to the overriden node in case we need it
                    # return node_to_replace
                    return (position, node, node_to_replace)

                # we are appending. Link the last node to its back, the first 
                # node of the list to its next. Make the former last node's 
                # next and the first node's back point to this node and increment
                # self._length by one.
                else:
                    last_node = self._head.get_back(self)
                    self._head.set_back(self, node)
                    last_node.set_next(self, node)
                    node.set_back(self, last_node)
                    node.set_next(self, self._head)
                    self._length += 1

            # return a reference to the inserted node in case we need to use it 
            # for anything.
            return (position, node)

        # if there is one node in the list and we are overwriting
        elif len(self) == 1 and overwrite:

            # set the new node as the only node in the list and unlink the former one.
            # Return a reference to the overriden node if needed for anything
            node_to_replace = self._head
            self._head = node
            self._head.set_next(self, node)
            self._head.set_back(self, node)
            node_to_replace._links.pop(self._id)
            return (0, self._head, node_to_replace)
        
        # the list is not empty and we are not appending.
        else:

            # find the node to move forward by one
            node_after = self._get_node_by_idx(position)

            # link the inserted node back and next references to their now neighbour nodes, 
            # and the previous node's next and following node's back to it. Adjust length.
            node.set_next(self, node_after)
            node.set_back(self, node_after.get_back(self))
            node_after.get_back(self).set_next(self, node)
            node_after.set_back(self, node)
            self._length += 1

            # If the node was inserted at head position, self._head will now point to it.
            if node_after is self._head:
                self._head = node    

            # on overwrite=True, unlink the node after the inserted one.
            # It is the same effect as replacing, or 'overwriting' a node.
            # Also, readjust length since we are removing one node here.
            # And return a reference to the overriden node if needed for anything later.
            if overwrite:
                node_after.get_next(self).set_back(self, node)
                node.set_next(self, node_after.get_next(self))   
                node_after._links.pop(self._id)
                self._length -= 1
                # return node_after
                return (position, node, node_after)

            # return a reference to that node in case we need to use it for anything.
            # return node
            return (position, node)

    def reverse(self):
        """
        Switches each node's 'back' and 'next' references and repositions the head 
        reference to the last node in the list, effectively reversing it in place. 
        This method is the equivalent to Python's list[::-1].
        """
        # switch the 'next' and 'back' references for each node
        for node in self:
            node._links[self._id]['next'], node._links[self._id]['back'] = \
            node._links[self._id]['back'], node._links[self._id]['next']
        
        # and set the head reference to the former last node, now first one
        self._head = self._head.get_next(self)

    def _get_node_by_idx(self, idx: int):
        """
        Takes an integer index (idx) and returns a reference to the node in that index 
        position in the list. Accepts negative indexing, like a regular Python list.
        """
        if idx < -self._length or idx > self._length - 1:
            raise IndexError('Index out of range.')
        
        assert self._length > 0, \
            'List is empty.'

        current = self._head

        # if we passed a negative index
        if idx < 0:

            # abs value of negative index is less than len(self) // 2
            if self._length // 2 < -idx:

                # iterate forward from head
                for _ in range(len(self) + idx):
                    current = current.get_next(self)
        
            # abs value of negative index is more than len(self) // 2
            else:

                # iterate backwards from head
                for _ in range(-idx):
                    current = current.get_back(self)

        # a positive index was passed, follow the same fashion as above,
        # condition and iterators are changed to adjust positive indexing    
        elif self._length // 2 > idx:
            for _ in range(idx):
                current = current.get_next(self)

        else:
            for _ in range(len(self) - idx):
                # input(current)
                current = current.get_back(self)
    
        return current

    def _get_node_by_name(self, name):
        """
        Given the node's name (id) passed as parameter, it searches on the list for a node
        with that name and returns it. Otherwise, it returns None.

        This method works on lists whose nodes have no repeated names.
        """
        assert self._length > 0, \
            'List is empty.'

        fordwardtrack = self._head
        backtrack = self._head.get_back(self)

        # traverse through the list until the target node is encountered.
        # If it is, return it. Otherwise, return None.
        for _ in range(self._length // 2 + 1):
            
            if fordwardtrack._id == name:
                return fordwardtrack
            
            elif backtrack._id == name:
                return backtrack

            fordwardtrack = fordwardtrack.get_next(self)
            backtrack = backtrack.get_back(self)

        return None

    def _nodify(self, node_or_value):
        """
        Takes an instance of MSCDLLNode or any value and: 
        (1) if it is a node, it adds this list to the node's _links' keys, or 
        (2) if it is any value, it converts it to a MSCDLLNode and also adds this 
        list to the node's _links' keys.

        Parameters:
            node_or_value (MSCDLLNode|any): a node to add this list to its _links' 
                keys, or a value to convert to a node and do the same.

        Returns:
            (MSCDLLNode): a valid MSCDLLNode instance with this list set in its 
                _links' keys.
        """
        if isinstance(node_or_value, MSCDLLNode):
            node_or_value._links[self._id] = {}
            return node_or_value

        node_or_value = MSCDLLNode(node_or_value)
        node_or_value._links[self._id] = {}
        return node_or_value

    def get_observer(self):
        """
        Returns a reference to the list's observer (MSCDLLObserver assigned instance), 
        or None if it does not have any, or if the observer is invalid or does not
        contain this instance as a subscriber.
        """
        try:
            self._assert_subscription()
        except AssertionError:
            return None

        return self._observer

    def get_observer_subscribers(self) -> list:
        """
        Returns a list of all linked lists being observed by this list's assigned 
        MSCDLLObserver instance, or None if this list is not subscribed to an observer,
        or if the observer is invalid or does not contain this instance as a subscriber.
        """
        try:
            self._assert_subscription()
        except AssertionError:
            return None

        return self._observer._subscribers

    def subscribe(self, observer):
        """
        Calls for subscribe() in the MSCDLLObserver instance passed as a parameter, 
        which adds this list to its subscribers. 
        It also sets that observer instance as this list's observer.

        Parameters:
            observer (MSCDLLObserver): an observer which this list will subscribe to.
        
        Returns:
            (MSCDLLObserver): a reference to the observer this list is now subscribed to.
        """
        if isinstance(observer, MSCDLLObserver) and not self._observer:
            observer.subscribe(self)
            return observer

        raise TypeError(
            'An instance of MSCDLL can only subscribe to an instance of MSCDLLObserver, ' +
            'and must unsubscribe to its assigned observer (if any) before subscribing ' + 
            'to a new one.'
        )

    def unsubscribe(self):
        """
        Calls for unsubscribe() in the MSCDLLObserver instance passed as a parameter, 
        which removes this list to its subscribers. 
        It also sets this list's _observer field to none.

        Returns:
            (MSCDLLObserver): a reference to the observer this list has unsubscribed from.
        """
        try:
            self._assert_subscription()
        except AssertionError:
            raise TypeError(
            'An instance of MSCDLL can only unsubscribe to an instance of MSCDLLObserver it is subscribed to.'
        )

        observer = self._observer
        self._observer.unsubscribe(self)
        return observer

    def _assert_subscription(self):
        """
        Checks if the list is subscribed to a valid MSCDLLObserver instance, and 
        that MSCDLLObserver has the list as one of its subscribers. Returns True 
        if so. Otherwise, it raises a AssertionError.
        """
        assert isinstance(self._observer, MSCDLLObserver), \
            'This instance must be subscribed to a MSCDLLObserver to use any \'linked\' methods.'
        
        assert self in self._observer._subscribers, \
            f'This instance is not subscribed to the assigned observer named {self._observer._id}.'
        
        return True

    def linked_append(self, node_or_value, **kwargs) -> dict:
        """
        Calls for the assigned observer's _append method to append node_or_value 
        to all of its subscribers. It uses insert() to do so, passing 'end' as a 
        positional argument and kwargs['overwrite'] as False.

        Parameters:
            node_or_value (MSCDLLNode|any): the same one as this class' append().

        Returns:
            (dict): a dictionary whose keys are the names (ids) of all lists, and
                the return of each list's append() as their values.
        """
        self._assert_subscription()
        return self._observer._append(node_or_value, **kwargs)

    def linked_prepend(self, node_or_value, **kwargs) -> dict:
        """
        Calls for the assigned observer's _prepend method to prepend node_or_value 
        to all of its subscribers. It uses insert() to do so, passing 0 as a 
        positional argument and kwargs['overwrite'] as False. Head node is set to 
        this new node for each list.

        Parameters:
            node_or_value (MSCDLLNode|any): the same one as this class' prepend().

        Returns:
            (dict): a dictionary whose keys are the names (ids) of all lists, and
                the return of each list's prepend() as their values.
        """
        self._assert_subscription()
        return self._observer._prepend(node_or_value, **kwargs)

    def linked_insert(self, node_or_value, position, **kwargs) -> dict:
        """
        Calls for the assigned observer's _insert method to insert node_or_value 
        into all of its subscribers at the given position index, or to overwrite the
        node at that index if 'overwrite' is True.

        Parameters:
            node_or_value (MSCDLLNode|any): the same one as this class' insert().
            position (int): the same one as this class' insert().
        
        kwargs:
            name (str|int): the same one as this class' insert().
            overwrite (bool): the same one as this class' insert().

        Returns:
            (dict): a dictionary whose keys are the names (ids) of all lists, and
                the return of each list's insert() as their values.
        """
        self._assert_subscription()
        return self._observer._insert(node_or_value, position, **kwargs)

    def linked_pop(self, **kwargs) -> dict:
        """
        Calls for the assigned observer's _pop method to pop a node from all of its 
        subscribers at the given position index.
        
        kwargs:
            name (str|int): the same one as this class' pop().
            index (int): the same one as this class' pop().
        
        Returns:
            (dict): a dictionary whose keys are the names (ids) of all lists, and
                the return of each list's pop() as their values.
        """
        self._assert_subscription()
        return self._observer._pop(**kwargs)

    def linked_remove(self, **kwargs) -> dict:
        """
        Calls for the assigned observer's _remove method to remove node_or_value 
        from all of its subscribers at the given the passed kwarg.
        
        kwargs:
            indexes (list|tuple): the same one as this class' remove().
            names (list|tuple): the same one as this class' remove().
            values (list|tuple): the same one as this class' remove().
        
        Returns:
            (dict): a dictionary whose keys are the names (ids) of all lists, and
                the return of each list's remove() as their values.
        """
        self._assert_subscription()
        return self._observer._remove(**kwargs)

    def linked_replace(self, node_or_value, **kwargs) -> dict:
        """
        Calls for the assigned observer's _replace method to replace all nodes found
        filtering by the passed kwarg in all of its subscribers with the node or value
        passed as parameter.

        kwargs:
            by_position (int): the same one as this class' replace().
            by_name (int|str): the same one as this class' replace().
            by_value (any): the same one as this class' replace().

        Returns:
            (dict): a dictionary whose keys are the names (ids) of all lists, and
                the return of each list's replace() as their values.
        """
        self._assert_subscription()
        kwargs['overwrite'] = True
        kwargs['mscdll'] = self
        return self._observer._replace(node_or_value, **kwargs)
        
    def linked_reverse(self):
        """
        Calls for the assigned observer's _reverse method to reverse all of its 
        subscribers in place.
        """
        self._assert_subscription()
        self._observer._reverse()

    def linked_get_nodes(self, **kwargs) -> dict:
        """
        Calls for the assigned observer's _get_nodes method to get all nodes 
        in all of its subscribers using the passed kwarg as a filter.

        kwargs:
            indexes (list|tuple): the same one as this class' get_nodes().
            names (list|tuple): the same one as this class' get_nodes().
            values (list|tuple): the same one as this class' get_nodes().

        Returns:
            (dict): a dictionary whose keys are the names (ids) of all lists, and
                the return of each list's get_nodes() as their values.
        """
        self._assert_subscription()
        return self._observer._get_nodes(**kwargs)

    def linked_set_nodes_values(self, value, **kwargs):
        """
        Calls for the assigned observer's _set_nodes_values method change each
        of their subscribers' nodes' values that match the filter stated in the 
        kwargvalues to the value passed as parameter.

        Parameters:
            value (any): the same one as this class' set_nodes_values().

        kwargs:
            indexes (list|tuple): the same one as this class' get_nodes().
            names (list|tuple): the same one as this class' get_nodes().
            values (list|tuple): the same one as this class' get_nodes().

        Returns:
            (dict): a dictionary whose keys are the names (ids) of all lists, and
                the return of each list's set_nodes_values() as their values.
        """
        self._assert_subscription()
        return self._observer._set_nodes_values(value, **kwargs)

    def linked_clone(self, **kwargs):
        """
        Calls for the assigned observer's _clone method to clone all of its 
        subscribers.

        kwargs:
            bind_to_self (bool): the same one as this class' clone().

        Returns:
            (dict): a dictionary whose keys are the names (ids) of all lists, and
                the return of each list's clone() as their values.
        """
        self._assert_subscription()
        return self._observer._clone(**kwargs)

    def linked_clear(self):
        """
        Calls for the assigned observer's _clear method to unlink all nodes from all of its 
        subscribers. Each list's length is set to 0 and head reference to None.
        """
        self._assert_subscription()
        self._observer._clear()

    def linked_extend(self, unlink_nodes=True, check_for_repeated_nodes=True, **kwargs):
        """
        Calls for the assigned observer's _extend method to extend all of its 
        subscribers as indicated by the passed kwarg.

        Parameters:
            mscdll (MSCDLL): the same one as this class' extend().
            unlink_nodes (bool): the same one as this class' extend().
            check_for_repeated_nodes (bool): the same one as this class' extend().
            
        kwargs:
            mode (string): 
                'append_self': the MSCDLL insance will be appended to all of its observer's 
                    subscribers but itself.
                'prepend_self': the MSCDLL insance will be prepended to all of its observer's 
                    subscribers but itself.
                'fuse_all': each of the observer's subscribers will be appended to the MSCDLL
                    instance (except for itself).
        """
        self._assert_subscription()
        self._observer._extend(self, unlink_nodes, check_for_repeated_nodes, **kwargs)

    def linked_split(self, idx):
        """
        Calls for the assigned observer's _split method to split all of its 
        subscribers by the given index.

        Parameters:
            idx (int): the same one as this class' split().

        Returns:
            (dict): a dictionary whose keys are the names (ids) of all lists, and
                the return of each list's split() as their values.
        """
        self._assert_subscription()
        return self._observer._split(idx)

    def linked_is_empty(self):
        """
        Calls for the assigned observer's _is_empty method on all of its 
        subscribers to check if whether they are empty or not.

        Returns:
            (dict): a dictionary whose keys are the names (ids) of all lists, and
                the return of each list's is_empty() as their values.
        """
        self._assert_subscription()
        return self._observer._is_empty()

    def linked_get_head(self):
        """
        Calls for the assigned observer's _get_head method on all of its 
        subscribers to get an instance of their head nodes.

        Returns:
            (dict): a dictionary whose keys are the names (ids) of all lists, and
                the return of each list's get_head() as their values.
        """
        self._assert_subscription()
        return self._observer._get_head()

    def linked_indexOf(self, node_or_value):
        """
        Calls for the assigned observer's _indexOf method on each of its subscribers 
        to get the index position of the nodes whose values match the value or node
        passed as a parameter (if a node was passed, its value will be considered).

        Note that this method is designed to consider all truthy and falsy values as 
        the same. True will be equal to 1. To discriminate between types, use 
        linked_get_nodes() instead, passing values as a kwarg.

        Parameters:
            node_or_value (MSCDLLNode|any): the same one as this class' indexOf().

        Returns:
            (dict): a dictionary whose keys are the names (ids) of all lists, and
                the return of each list's indexOf() as their values.
        """
        self._assert_subscription()
        return self._observer._indexOf(node_or_value)

    def linked_valueOf(self, idx):
        """
        Calls for the assigned observer's _valueOf method on each of its subscribers 
        to get the node's values on the index position passed as a parameter.

        Parameters:
            idx (int): the same one as this class' valueOf().

        Returns:
            (dict): a dictionary whose keys are the names (ids) of all lists, and
                the return of each list's valueOf() as their values.
        """
        self._assert_subscription()
        return self._observer._valueOf(idx)


class _MSCDLLIterator:
    """
    A class resposible of generating iterator objects that traverse
    the MSCDLL forwards. From the head node to the last one.
    """

    def __init__(self, mscdll):
        self._current = mscdll._head
        self._mscdll = mscdll
        self._flag = False

    def __iter__(self):
        return self

    def __next__(self):
        while not self._flag:

            if not self._mscdll._head: 
                raise StopIteration

            node = self._current
            self._current = self._current.get_next(self._mscdll)

            if self._current == self._mscdll._head:
                self._flag = True

            return node

        raise StopIteration


class _MSCDLLReverseIterator:
    """
    A class resposible of generating iterator objects that traverse
    the MSCDLL backwards. From the last node to the head one.
    """

    def __init__(self, mscdll):
        self._current = mscdll._head.get_back(mscdll)
        self._back_ref = mscdll._head.get_back(mscdll)
        self._mscdll = mscdll
        self._flag = False

    def __iter__(self):
        return self

    def __next__(self):
        if not self._current:
            raise StopIteration

        if self._current is self._back_ref:

            if self._flag:
                raise StopIteration
            else:
                self._flag = True

        node = self._current
        self._current = self._current.get_back(self._mscdll)

        return node


class MSCDLLNode:
    """
    A class to create valid MSCDLL nodes, which are to be added to MSCDLL instances.

    Attributes:
        value               _links              _id
    
    Main methods:
        __str__             __repr__            get_links
        get_MSCDLL_links    get_name            get_next
        get_back            set_name            set_next
        set_back            set_MSCDLL_links    pprint
    """

    def __init__(self, value, **kwargs):
        """
        Sets the node's value and name (id), and creates the _links dictionary to 
        store the MSCDLL reference's names where the node will be allocated, and
        its 'next' and 'back' nodes in them.

        kwargs:
            name (str|int): the node name (id). Defaults to its memory address to
                make it unique from the rest.
        """
        self.value = value
        self._links = {}
        self._id = id(self)

        if 'name' in kwargs:
            self._id = kwargs['name']

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    def get_links(self):
        """
        Returns a dictionary where the keys are all of the MSCDLL instances the
        node is linked to, and their values, the 'next' and 'back' node references
        in them. 
        """
        return self._links

    def get_MSCDLL_links(self, mscdll):
        """
        Returns a dictionary whose key is the MSCDLL list passed as parameter,
        and its values are this node's 'back' and 'next' references in that list.
        """
        return self._links[mscdll._id]

    def get_name(self):
        """
        Returns the name (id) of the node. 
        """
        return self._id

    def get_next(self, mscdll):
        """
        Returns a reference to this node's next node in the MSCDLL instance 
        passed as parameter.
        """
        return self._links[mscdll._id]['next']

    def get_back(self, mscdll):
        """
        Returns a reference to this node's back node in the MSCDLL instance 
        passed as parameter.
        """
        return self._links[mscdll._id]['back']

    def set_name(self, name):
        """
        Sets the name (id) of this node to the one passed as parameter.
        """
        self._id = name

    def set_next(self, mscdll, node):
        """
        Sets this node's 'next' reference in the MSCDLL list passed as parameter 
        to a valid MSCDLLNode instance, also passed as parameter.
        """
        if isinstance(node, MSCDLLNode) or node is None:
            self._links[mscdll._id]['next'] = node
            return
        
        raise TypeError(
            'Only valid instances of MSCDLLNode or None can be passed as ' + 
            '\'node\' parameter.')

    def set_back(self, mscdll, node):
        """
        Sets this node's 'back' reference in the MSCDLL list passed as parameter 
        to a valid MSCDLLNode instance, also passed as parameter.
        """
        if isinstance(node, MSCDLLNode) or node is None:
            self._links[mscdll._id]['back'] = node
            return
        
        raise TypeError(
            'Only valid instances of MSCDLLNode or None can be passed as ' +
            '\'node\' parameter.')

    def set_MSCDLL_links(self, mscdll):
        """
        Creates a key with the MSCDLL instance's name (id) inside the _links
        dictionary and assigns an empty dictionary as its value.
        """
        if isinstance(mscdll, MSCDLL):
            self._links[mscdll._id] = {}
            return
        
        raise TypeError(
            'Only valid instances of MSCDLL can be passed as \'mscdll\' parameter.')
        
    def pprint(self):
        """
        Prints the node out in a 'debugging' fashion. Emulates JSON format.

        The node name, its value and _links dictionary for all of its MSCDLL assigned
        instances will be printed out.
        """
        string = '{\n'
        string +='    "name": ' + str(self._id) + ',\n'
        string +='    "value": ' + str(self.value) + ',\n'
        string +='    "links": {'
        
        for key, value in self._links.items():
            string += '\n        '+ str(key) + ': {\n'
            
            for k, v in value.items():
                string += f'            {k}: '
                string += '{\n                "name": ' + str(v._id)
                string += ', \n                "value": ' + str(v.value) +\
                          '\n            },\n'
            
            string += '        }'
        
        string += '\n    }\n}'
        print(string)
        return string


class MSCDLLObserver:
    """
    An observer class designed to host MSCDLL instances which are to be connected
    to -and to react to- each other's actions.

    It follows the Observer (Pub-Sub) pattern. MSCDLL instances subscribe to an
    observer and, if they want to affect all lists on purpose or to perform safe 
    operations on itself (like destroying a node without breaking the integrity 
    of other lists that host it), then they call for the 'linked' version of their
    methods instead of their regular ones. If they do so, the action will be 
    redirected to the observer, and the observer will adapt and replicate that 
    action on all of its subscribers.

    Even though an observer instance is capable to call for its methods by itself,
    it is strongly recommended not to do so unless you are really certain on what
    those methods do and how they do it. The observer class is designed to be a 
    catalyst between a caller MSCDLL instance and each list linked to it in a 
    certain way. So, the intended behavior is for that MSCDLL instance to command
    the method to apply to all lists by its own 'linked' version, and the observer
    to adapt that call and redirect it to all other lists.

    Attributes:
        _subscribers         _id
    
    Main methods:
        __init__             __str__               subscribe   
        unsubscribe          unsubscribe_all       get_name
        get_subscriber       get_subscribers       set_name

    Private methods (meant to be called by MSCDLL instances 'linked' methods):
        _append              _prepend              _insert
        _remove              _pop                  _clear
        _split               _clone                _replace
        _indexOf             _valueOf              _reverse
        _get_head            _get_nodes            _is_empty
        _set_nodes_values
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the subscribers list, where all listening MSCDLL instances
        will be stored. It also subscribes all MSCDLL instances passed as args,
        sets its default name (id) to by its address in memory as an int, or 
        to be the optional kwargs['name'].
        """
        self._subscribers = []
        self._id = id(self)

        if 'name' in kwargs:
            self._id = kwargs['name']

        for arg in args:
            self.subscribe(arg)

    def __str__(self):
        string = self._id + ' {\n  '

        for sub in self._subscribers:
            string += str(sub.get_name()) + ',\n  '

        string += '\b\b}' 

        return string

    def unsubscribe_all(self):
        """
        Unsubscribes all MSCDLL instances stored in _subscribers. Each one of 
        those instances will have their _observer set to None, and the observer's
        _subscriber list will be emptied.

        It is much recommended to call for this method on the Observer instance
        before attempting to delete it.
        """
        for sub in self._subscribers:

            if type(sub) is MSCDLL and self == sub._observer:
                sub._observer = None

        self._subscribers = []

    def get_name(self):
        """
        Returns the name (id) of the observer.
        """
        return self._id

    def get_subscribers(self) -> list:
        """
        Returns a reference to the list containing the references to 
        all the observer's subscribers.
        """
        return self._subscribers

    def get_subscriber(self, name):
        """
        Searches for a subscriber whose name (id) matches the one passed
        as a parameter. Returns a reference to the found subscriber or
        None if there was no subscriber found.

        Keep in mind all subscribers must have different names (ids) from
        each other for this method to work.

        Parameters:
            name (str|int): the name (id) of the MSCDLL instance to look for.
        """
        for sub in self._subscribers:

            if sub._id == name:
                return sub
        
        return None

    def set_name(self, name):
        """
        Sets the name of the observer to the one passed as parameter.

        Parameter:
            name (str|int): the name (id) to replace the current observer's name (id).
        """
        self._id = name

    def subscribe(self, mscdll):
        """
        Takes a valid MSCDLL instance and adds it to its _subscribers list. It also
        sets that instance's _observer to point to this one.

        Parameters:
            mscdll (MSCDLL): an MSCDLL instance not already subscribed to this observer.
        """
        if isinstance(mscdll, MSCDLL):

            if mscdll._id not in [sub._id for sub in self._subscribers]:
                self._subscribers.append(mscdll)
                mscdll._observer = self
                return mscdll

            raise ValueError(
                f'The MSCDLL instance is already subscribed to: {mscdll.get_observer()._id}.'
            )
            
        raise TypeError(
            'An instance of MSCDLLObserver can only subscribe instances of MSCDLL.'
        )

    def unsubscribe(self, mscdll):
        """
        Takes an MSCDLL instance inside _subscribers and removes it. It also sets its
        _observer pointer to None.

        Parameters:
            mscdll (MSCDLL): an MSCDLL instance subscribed to this observer.
        """
        if isinstance(mscdll, MSCDLL) and mscdll._id in [sub._id for sub in self._subscribers]:
            self._subscribers.remove(mscdll)
            mscdll._observer = None
            return mscdll

        raise TypeError(
            'An instance of MSCDLLObserver can only unsubscribe instances of MSCDLL that are subscribed to it.'
        )

    def _append(self, node_or_value, **kwargs):
        """
        Calls for each subscriber's append() to add a node or value (which is
        converted to a node), at the end of all of them.

        Parameters:
            node_or_value (MSCDLLNode|any): the same one as MSCDLL's append().

        kwargs:
            name (str|int): the same one as MSCDLL's append().
            overwrite (bool): always set to False, since a node is appended,
                not overriden.

        Returns:
            (dict): a dictionary whose keys are the names (ids) of all
                subscribed lists, and the return of each list's append() as 
                their values.
        """
        appended_nodes = {}

        for sub in self._subscribers:
            appended_nodes[sub._id] = sub.append(node_or_value, **kwargs)

        return appended_nodes

    def _prepend(self, node_or_value, **kwargs):
        """
        Calls for each subscriber's prepend() to add a node or value (which is
        converted to a node), to the beginning of all of them, as their
        head node.

        Parameters:
            node_or_value (MSCDLLNode|any): the same one as MSCDLL's prepend().

        kwargs:
            name (str|int): the same one as MSCDLL's prepend().
            overwrite (bool): always set to False, since a node is appended,
                not overriden.

        Returns:
            (dict): a dictionary whose keys are the names (ids) of all
                subscribed lists, and the return of each list's prepend() as 
                their values.
        """
        prepended_nodes = {}

        for sub in self._subscribers:
            prepended_nodes[sub._id] = sub.prepend(node_or_value, **kwargs)
        
        return prepended_nodes

    def _insert(self, node_or_value, position, **kwargs):
        """
        Calls for each subscriber's insert() to add or replace a node or 
        value (which is converted to a node), on each list at the index 
        specified by the 'position' parameter. 
        
        The node at that position will be replaced by node_or_value parameter 
        if kwargs['overwrite'] is True. Otherwise, it will be inserted in that 
        position, pushing all following nodes to the right by one. 
        
        For each list, if the passed index is invalid, nothing will be inserted 
        to it. The loop will continue to the next subscriber.

        Parameters:
            node_or_value (MSCDLLNode|any): the same one as MSCDLL's insert().
            position (int): the same one as MSCDLL's insert().

        kwargs:
            name (str|int): the same one as MSCDLL's insert().
            overwrite (bool): the same one as MSCDLL's insert().

        Returns:
            (dict): a dictionary whose keys are the names (ids) of all
                subscribed lists, and the return of each list's prepend() as 
                their values.
        """
        inserted_nodes = {}

        for sub in self._subscribers:

            if not (-len(sub) <= position <= len(sub)):
                inserted_nodes[sub._id] = None
                continue

            inserted_nodes[sub._id] = sub.insert(node_or_value, position, **kwargs)
        
        return inserted_nodes

    def _pop(self, **kwargs):
        """
        Calls for each subscriber's pop() to pop a node from them at the
        passed index position, or by the passed node's name.

        Only one kwarg is allowed per method call. Also, for each subscriber, 
        if a node is not found given the passed kwarg, the risen exceptions
        will be caught silently, and nothing will be removed from the list. 

        kwargs:
            name (str|int): the same one as MSCDLL's pop().
            index (int): the same one as MSCDLL's pop().

        Returns:
            (dict): a dictionary whose keys are the names (ids) of all
                subscribed lists, and the return of each list's pop() as 
                their values.
        """
        if ('name'in kwargs, 'index' in kwargs).count(True) != 1:
            raise KeyError('You must pass one kwarg in \'linked_pop()\': \'name\' or \'index\'.')

        popped_nodes = {}
        
        for sub in self._subscribers:

            try:
                popped_nodes[sub._id] = sub.pop(**kwargs)
            except (KeyError, AssertionError, IndexError):
                popped_nodes[sub._id] = None
                continue

        return popped_nodes

    def _remove(self, **kwargs):
        """
        Calls for each subscriber's remove() to remove any instances of nodes
        whose indexes, values or names match the ones passed as kwargs.

        Only one kwarg is allowed per method call. Also, for each subscriber, 
        if a node is not found given the passed kwarg, the risen exceptions
        will be caught silently, and nothing will be removed from the list. 

        kwargs:
            name (str|int): the same one as MSCDLL's remove().
            index (int): the same one as MSCDLL's remove().

        Returns:
            (dict): a dictionary whose keys are the names (ids) of all
                subscribed lists, and the return of each list's remove() as 
                their values.
        """
        removed_nodes = {}
        
        for sub in self._subscribers:
            removed_nodes[sub._id] = sub.remove(**kwargs)

        return removed_nodes


    def _replace(self, node_or_value, **kwargs):
        """
        Calls for each subscriber's replace() to replace a node from them at 
        the passed index kwarg, or by the passed node's name.

        Only one kwarg is allowed per method call. Also, for each subscriber, 
        if a node is not found given the passed kwarg, the risen exceptions
        will be caught silently, and nothing will be replaced from the list.

        kwargs:
            by_position (int): the same one as MSCDLL's replace().
            by_name (int|str): the same one as MSCDLL's replace().
            by_value (any): the same one as MSCDLL's replace().

        Returns:
            (dict): a dictionary whose keys are the names (ids) of all
                subscribed lists, and the return of each list's replace() as 
                their values.
        """
        if not (
            0 < 
            [
                'by_node' in kwargs, 'by_name' in kwargs, 'by_position' in kwargs, 'by_value' in kwargs
            ].count(True) 
            < 2
        ):
            raise KeyError(
                '\'linked_replace\' method requires only one of these three kwargs: '+
                '\'by_position\', \'by_node\', \'by_name\', \'by_value\'')

        replaced_nodes = {}

        if 'by_position' in kwargs:

            for sub in self._subscribers:
                replaced_nodes[sub._id] = ()

                if not (-len(sub) <= kwargs['by_position'] < len(sub) - 1) \
                  and kwargs['by_position'] != 0:
                    continue

                replaced_nodes[sub._id] = sub.insert(node_or_value, kwargs['by_position'], **kwargs)

        else:
            for sub in self._subscribers:
                replaced_nodes[sub._id] = []

                if 'by_name' in kwargs:
                    index_node_tuples = sub.get_nodes(names=[kwargs['by_name']])
                elif 'by_node' in kwargs:
                    index_node_tuples = sub.get_nodes(names=[kwargs['by_node']._id])
                elif 'by_value' in kwargs:
                    index_node_tuples = sub.get_nodes(values=[kwargs['by_value']])

                if not index_node_tuples:
                    continue

                for item in index_node_tuples:
                    replaced_nodes[sub._id].append(sub.insert(node_or_value, item[0], **kwargs))

        return replaced_nodes

    def _reverse(self):
        """
        Calls for each subscriber's reverse() to reverse all of them in place.
        """
        for sub in self._subscribers:
            sub.reverse()

    def _get_nodes(self, **kwargs):
        """
        Calls for each subscriber's get_nodes() to get all of their nodes that 
        match the given kwarg used as a filter.

        Only one kwarg is allowed per method call. Also, for each subscriber, 
        if a node is not found given the passed kwarg, an empty list will be
        returned for it.

        kwargs:
            indexes (list|tuple):  the same one as MSCDLL's get_nodes().
            names (list|tuple):  the same one as MSCDLL's get_nodes().
            values (list|tuple):  the same one as MSCDLL's get_nodes().

        Returns:
            (dict): a dictionary whose keys are the names (ids) of all
                subscribed lists, and the return of each list's get_nodes() as 
                their values.
        """
        node_dict = {}

        if len(kwargs) == 1 or not kwargs:

            for sub in self._subscribers:
                node_dict[sub._id] = []

                if 'indexes' in kwargs:
                    valid_indexes = []

                    for index in kwargs['indexes']:
                
                        if -len(sub) <= index < len(sub):
                            valid_indexes.append(index)
                
                    node_dict[sub._id] = sub.get_nodes(indexes=valid_indexes)
                    
                else:
                    node_dict[sub._id] = sub.get_nodes(**kwargs)
            
        else:
            raise KeyError('You can only pass one kwarg at a time.')
        
        return node_dict

    def _set_nodes_values(self, value, **kwargs):
        """
        Calls for each subscriber's set_nodes_values() to set the values of all 
        matching nodes given the kwarg to the one passed as a parameter. 

        Parameters:
            value (any):  the same one as MSCDLL's set_nodes_values().

        kwargs:
            indexes (list|tuple): the same one as MSCDLL's get_nodes().
            names (list|tuple): the same one as MSCDLL's get_nodes().
            values (list|tuple): the same one as MSCDLL's get_nodes().

        Returns:
            (dict): a dictionary whose keys are the names (ids) of all
                subscribed lists, and the return of each list's set_nodes_values() 
                as their values.
        """
        node_dict = {}

        for sub in self._subscribers:
            node_dict[sub._id] = sub.set_nodes_values(value, **kwargs)

        return node_dict

    def _clone(self, **kwargs):
        """
        Calls for each subscriber's clone() to create and return a shallow copy
        of each of them.

        kwargs:
            clone_list_name (str|int): obligatorily defaults to a combination of 
                the list-being-cloned id and the cloned list id to avoid naming
                conflict. If this kwarg is provided, a KeyError will rise.
            bind_to_self (bool): the same one as MSCDLL's clone().

        Returns:
            (dict): a dictionary whose keys are the names (ids) of all
                subscribed lists, and the return of each list's clone() 
                as their values.
        """
        if 'clone_list_name' in kwargs:
            raise KeyError(
                '\'clone_list_name\' is not a valid kwarg for linked_clone(). Lists will be '+
                'automatically named to avoid conflicts. You can rename them with set_name().'
            )

        clone_list = {}

        for sub in self._subscribers:
            clone_list[sub._id] = sub.clone(**kwargs)
        
        return clone_list

    def _clear(self):
        """
        Calls for each subscriber's clear() to unlink all nodes from them, reset their 
        length and set their head nodes to None.
        """
        for sub in self._subscribers:
            sub.clear()

    def _extend(self, caller_mscdll, unlink_nodes, check_for_repeated_nodes, **kwargs):
        """
        Calls for each subscriber's extend() to extend them according to the mode 
        passed as kwarg.

        Parameters:
            mscdll (MSCDLL): the same one as MSCDLL's extend().
            unlink_nodes (bool): the same one as MSCDLL's extend().
            check_for_repeated_nodes (bool): the same one as MSCDLL's extend().
            
        kwargs:
            mode (string): 
                'append_self': the caller MSCDLL insance will be appended to all 
                    other subscribers.
                'prepend_self': the caller MSCDLL insance will be prepended to all 
                    other subscribers.
                'fuse_all': each subscriber will be appended to the caller MSCDLL
                    instance.
        """
        if 'mode' in kwargs:

            if kwargs['mode'] == 'prepend_self' or kwargs['mode'] == 'append_self':
                
                for sub in self._subscribers:
                    
                    # do nothing if sub == the mscdll instance that called for this method
                    if sub is caller_mscdll:
                        continue
                    
                    # if this method's ValueError, or extend() TypeError or AssertionError rise,
                    # fail silently and continue to the next sub in list
                    try:
                        
                        # case 1: on 'append_self', add the mscdll caller instance to the end of 
                        # each subscripted list. If unlink_nodes is True, we will unlink them
                        # later, since their references are lost and will raise an error here
                        if kwargs['mode'] == 'append_self':
                            sub.extend(caller_mscdll, False, check_for_repeated_nodes)
                        
                        # case 2: on 'prepend_self', do the same as 'append_self', but add the
                        # nodes to the beginning of each subscripted list 
                        else:

                            # same check_for_repeated_nodes as the one in extend(), since we will 
                            # not use extend() while prepending nodes. So, we do it here
                            if check_for_repeated_nodes:

                                shortest_list = sub if sub._length <= caller_mscdll._length else caller_mscdll
                                longest_list = caller_mscdll if caller_mscdll._length >= sub._length else sub
                                self_nodes = [node[1] for node in shortest_list.get_nodes()]

                                for node in longest_list:

                                    # If a node is repeated in the caller instance and the current
                                    # iterating list, raise the ValueError, which is caught to
                                    # ignore the extension on this list and continue with the
                                    # following one
                                    if node in self_nodes:
                                        raise ValueError(
                                            'A node cannot be in more than one list at the same time while performing an extension.'
                                        )
                            
                            # for each node IN REVERSE in the list that called for this method,
                            # prepend that node to each subscribed list. Prepending in reverse
                            # will effectively keep the final order
                            for node in caller_mscdll.iter_reverse():
                                sub.prepend(node)
                    
                    except (ValueError, TypeError, AssertionError):
                        continue

                # if we are to unlink the nodes from the original list for a clear extension,
                # then remove the list reference from each of its nodes and set the list's head
                # and length to 0
                if unlink_nodes:
                    for node in caller_mscdll:
                        node._links.pop(caller_mscdll._id)

                    caller_mscdll._head = None
                    caller_mscdll._length = 0

                # done. All lists are modified accordingly.
                return
  
            # case 3: on 'fuse_all', append each list to the called mscdll instance, one at a time
            if kwargs['mode'] == 'fuse_all':
            
                for sub in self._subscribers:
                    
                    # do nothing if sub == the mscdll instance that called for this method
                    if sub is caller_mscdll:
                        continue
                
                    # extend the original list with each other subscriber
                    caller_mscdll.extend(sub, unlink_nodes, check_for_repeated_nodes)
            
            # caller MSCDLL instance is fused with all other lists. Done.
            return

        # 'fuse_all', 'append_self' or 'prepend_self' were not passed as kwargs. Rise exception
        raise KeyError(
            'You must provide \'append_self\', \'prepend_self\' or \'fuse_all\' as ' +
            'the value of \'mode\' kwarg.'
        )

    def _split(self, idx):
        """
        Calls for each subscriber's split() to split by the index passed as
        parameter. For each subscriber, if the index is invalid, and IndexError
        will be caught silently, skipping the list and thus leaving it intact.

        Parameters:
            idx (int): the same one as MSCDLL's extend().

        Returns:
            (dict): a dictionary whose keys are the names (ids) of all
                subscribed lists, and the return of each list's split() 
                as their values.
        """
        splitted_lists = {}
        
        for sub in self._subscribers:

            try:
                splitted_lists[sub._id] = sub.split(idx, f'{sub._id}_split')
            except IndexError:
                splitted_lists[sub._id] = []

        return splitted_lists

    def _is_empty(self):
        """
        Calls for each subscriber's is_empty() to check if each of them is an
        empty list or not.

        Returns:
            (dict): a dictionary whose keys are the names (ids) of all
                subscribed lists, and the return of each list's is_empty() 
                as their values.
        """
        empty_lists = {}

        for sub in self._subscribers:
            empty_lists[sub._id] = False

            if sub.is_empty():
                empty_lists[sub._id] = True
        
        return empty_lists

    def _get_head(self):
        """
        Calls for each subscriber's get_head() to check return a reference to
        the head node of each list.

        Returns:
            (dict): a dictionary whose keys are the names (ids) of all
                subscribed lists, and the return of each list's get_head() 
                as their values.
        """
        list_heads = {}

        for sub in self._subscribers:
            list_heads[sub._id] = sub.get_head()
        
        return list_heads

    def _indexOf(self, node_or_value):
        """
        Calls for each subscriber's indexOf() to get the indexes of the 
        node(s) whose value matches the value (or node's value) passed as
        parameter, for each list. For each list, an empty tuple will be 
        returned if there is no match. Otherwise, the indexes of each matching
        node will be returned inside a tuple.

        Parameters:
            node_or_value (MSCDLLNode|any): the same one as MSCDLL's indexOf().

        Returns:
            (dict): a dictionary whose keys are the names (ids) of all
                subscribed lists, and the return of each list's indexOf() 
                as their values.
        """
        indexes_dict = {}

        for sub in self._subscribers:
            indexes_dict[sub._id] = sub.indexOf(node_or_value)

        return indexes_dict

    def _valueOf(self, idx):
        """
        Calls for each subscriber's valueOf() to get the node at the index 
        position passed as parameter. For each list, if the index is invalid,
        the risen exceptions will be caught silently and set the returning 
        dictionary key's value to None.

        Parameters:
            idx (int): the same one as MSCDLL's valueOf().

        Returns:
            (dict): a dictionary whose keys are the names (ids) of all
                subscribed lists, and the return of each list's valueOf() 
                as their values.
        """
        values_dict = {}

        for sub in self._subscribers:
            
            # AssertionError rises if list is empty, and IndexError if index is invalid.
            # Catch those two and fail silently, adding None to their dictionary's value.
            # Add the valid lists's found node their dictionary's value.
            try:
                values_dict[sub._id] = sub.valueOf(idx)
            except (AssertionError, IndexError):
                values_dict[sub._id] = None

        return values_dict
