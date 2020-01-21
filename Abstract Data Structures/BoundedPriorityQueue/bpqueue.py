from modules.array import Array
from modules.queue import Queue

class BPQueue():
    """
    A class which attempts to emulate the basic behavior of a Bounded 
    Priority Queue (BPQueue).

    A BPQueue introduces the concept of priority when storing, enqueing, 
    dequeuing or peeking any of its elements. Its constructor takes an 
    integer which represents the lowest priority level and creates an 
    array of that many Queue instances. The first Queue will be stored 
    in array[0] and it is considered to be the highest priority, where 
    elements are be dequeded by default. The last queue will be inside 
    array[-1], where elements are normally enqueued. 
    
    However, enqueue(), dequeue() and peek() accept an integer value for a 
    priority level as a parameter. If given, the individual queue related 
    to that priority level will be affected by those methods. For example, 
    if you call for enqueue(item, 3), the item is enqueued to the Queue 
    whose priority is 3. Dequeue(5) will dequeue the first item in the queue 
    whose priority is 5. And so on.

    This class supports those three basic Queue methods as well as cloning, 
    getting indexes of items, splitting by priority level and printing both for 
    debugging (in detail) and for visualizing the queue as a whole in a 
    comfortable way.

    Methods:
        __init__
        __contains__
        __iter__
        __len__
        __str__
        clone : Creates and returns a shallow copy of self.
        dequeue : Dequeues a node from the BPQueue or from one of its priority 
            level queues.
        dprint : Prints out the BPQueue in great detail.
        enqueue : Enqueues a node from the BPQueue or from one of its priority 
            level queues.
        indexOf : Returns a tuple containing the BPQueue position index(es) and 
            the in-priority-level queue index(es) a value.
        get_lowest_priority_lvl : Returns the lowest priority level value of 
            the BPQueue.
        get_queue : Returns the Queue instance associated to the priority level.
        peek : Returns the next node to be dequeued from the BPQueue or from one 
            of its priority level queues.
        pprint : Prints out the BPQueue in a more readable version than 
            print(self).
        split : Splits the BPQueue in two by a specified priority level.

    Helper methods:
        _is_valid_priority_level : Helper method to validate that the priority 
            level is in range.

    Inner classes:
        _BPQueueIterator : Generates and return a BPQueue iterator object when 
            __iter__ is called.

    Author: Renzo Nahuel Murina Cadierno
    Contact: nmcadierno@hotmail.com
    Github: https://github.com/RenzoMurinaCadierno
    """
    
    def __init__(self, min_priority_level):
        """
        Creates an Array instance whose length is min_priority_level and stores 
        a Queue instance inside each of its slots.

        By default, items will be dequeued from the Queue in array[0] and enqueued 
        to the one in array[min_priority_level].
        """
        assert type(min_priority_level) is int, \
            'Minimum priority level must be an integer value.'

        self._priority_arr = Array([Queue() for i in range(min_priority_level + 1)])
        self._length = 0

    def __contains__(self, value):
        for queue in self._priority_arr:

            if not queue.is_empty():
                current = queue._head

                while current:

                    if current.value == value:
                        return True
                    
                    current = current._next
        
        return False

    def __iter__(self):
        return self._BPQueueIterator(self._priority_arr)


    def __len__(self):
        return self._length

    def __str__(self):
        string = '<TOP> '

        for queue in self._priority_arr:
            current = queue._head

            while current:
                string += str(current.value) + ' <- '
                current = current._next
        
        string += '<END>' if string == '<TOP> ' else '\b\b\b<END>'
        return string

    def clone(self):
        """
        Creates and returns a shallow copy of self: a new BPQueue instance with the 
        same length as self, its same priority levels and node clones in them, 
        linked together in the same fashion as self.
        """

        new_bpq = BPQueue(len(self._priority_arr))
        new_bpq._priority_arr = Array([Queue() for _ in range(len(self._priority_arr))])

        for i, queue in enumerate(self._priority_arr):

            if not queue.is_empty():
                current = queue._head

                while current:
                    new_bpq._priority_arr[i].enqueue(current.value)
                    new_bpq._length += 1
                    current = current._next

        return new_bpq

    def dequeue(self, priority_level=None):
        """
        Dequeues the node from the queue associated to the priority level passed as
        parameter. If no priority level is passed, it defaults to the regular queue
        behavior.

        Parameters:
            priority_level (int): The priority level of the queue to dequeue the node.
                Defaults to the highest priority (value 0), like a regular queue.
        
        Return:
            (SSLL_Node): An instance of the dequeded node. Rises an error if the BPQueue 
                or the Queue in the specified priority level (if any) are empty.
        """
        if not priority_level:

            for queue in self._priority_arr:

                if not queue.is_empty():
                    self._length -= 1
                    return queue.dequeue()
        
        else:
            self._is_valid_priority_level(priority_level)
            queue = self._priority_arr[priority_level]

            if not queue.is_empty():
                self._length -= 1
                return queue.dequeue()

        raise AssertionError('Cannot dequeue from an empty queue.')

    def dprint(self):
        """
        Prints out a detailed description of the BPQueue.

        This method will display each node in the BPQueue ordered by priority
        level, showing its BPQueue index, in-priority-queue index and value.

        It will also print out the lazy (short) graphical version of the
        BPQueue, as well as its length, lowest priority level value and nodes
        per priority level.
        """
        print('\n', '-' * 80)
        print('*** Detailed BPQ Display ***'.center(80))
        bpq_idx = 0
        nodes_per_level = []
        string = '<BPQ>'

        for i, queue in enumerate(self._priority_arr):
            string += f'\n\n<Priority {i}>'

            if queue.is_empty():
                string += f'\nNo nodes with priority {i}'
                continue

            current = queue._head

            while current:
                string += f'\n> BPQ idx: {bpq_idx}, In-PQ idx: {current._idx}, Value: {str(current.value)}'
                bpq_idx += 1

                if not current._next:
                    nodes_per_level.append(current._idx)

                current = current._next
                

        string += '\n\n</BPQ>\n'
        print(string)
        print('-' * 80)
        print('*** Lazy BPQ Display ***'.center(80))
        print('\n', self)
        print('-' * 80)
        print('*** BPQ Extra information ***'.center(80))
        print('> Length:', self._length)
        print('> Lowest priority level:', self.get_lowest_priority_lvl())
        print('> Number of nodes per priority level:')

        for i, value in enumerate(nodes_per_level):
            print(f'  > {i}:', f'{value + 1}'.rjust(3,"0"), end=' ')
            print('*' * (value + 1))

        print('-' * 80)

    def enqueue(self, node_or_value, priority_level=None):
        """
        Enqueues a node to the Queue associated with the priority level passed as
        parameter.

        Parameters:
            node_or_value (any): The node to be enqueued. If an instance of any
                other class that is not SSLL_Node is passed, the object is converted
                to one.
            priority_level (int): The priority level of the queue to enqueue the node.
                Defaults to the lowest priority (highest value), like a regular queue.
        
        KEEP IN MIND you should no enqueue items into a BPQueue by directly
        enqueuing to its individual queues, since it will compromise self._length,
        as well as the methods that utilize that attribute. 
        
        This is, you should NOT do something like this:
            BPQueue._priority_arr[i].enqueue(node_or_value)
        
        Instead, use this built-in enqueue method for the class, like it is inteded.
            BPQueue.enqueue(node_or_value, i)
        """
        if not priority_level and priority_level != 0:
            priority_level = self.get_lowest_priority_lvl()

        self._is_valid_priority_level(priority_level)
        self._priority_arr[priority_level].enqueue(node_or_value)
        self._length += 1

    def indexOf(self, value, **kwargs):
        """
        Returns a tuple containing the BPQueue position index(es) and the 
        in-priority-level queue index(es) of the value passed as a parameter.
        
        Parameters:
            value (any): The value of the node to look for in the BPQueue.

        kwargs:
            lazy (bool): On True, the method will return a tuple with the indexes 
                on the first matching value it encounters, thus ending the search
                prematurely. On True, the whole BPQueue will be scanned, and a
                tuple of tuples containing all BPQueue position indexes and
                in-priority-level queue indexes where the node value matches the
                value passed as a parameter.

        Return:
            (tuple): A single tuple with the value's BPQueue position and
                in-priority-level queue index if kwargs['lazy'] is True, or a tuple
                containing all tuples with those indexes where instances of that
                value match with node values in the BPQueue. 
        """
        indexes = []
        lazy = True

        if 'lazy' in kwargs:
            if not kwargs['lazy']:
                lazy = False

        for i, queue in enumerate(self._priority_arr):

            if not queue.is_empty():
                current = queue._head
                
                while current:

                    if current.value == value:

                        if lazy:
                            return (i, current._idx)

                        indexes.append((i, current._idx))

                    current = current._next

        return tuple(indexes)

    def get_lowest_priority_lvl(self) -> int:
        """
        Returns the lowest priority level value of the BPQueue.

        Keep in mind that 0 is the actual highest priority, which will be the 
        queue where values are first dequeued. The integer returned by this
        method is the lowest priority, where nodes are normally enqueued.
        
        Return:
            (int): the lowest priority level integer value of the BPQueue.
        """
        return len(self._priority_arr) - 1

    def get_queue(self, priority_level: int):
        """
        Returns the Queue instance associated to the priority level.

        Parameters:
            priority_level (int): The priority level of the queue to be returned.
        
        Return:
            (Queue): The Queue instance associated to the priority level.
        """
        return self._priority_arr[priority_level]

    def peek(self, priority_level=None):
        """
        Returns a pointer to the node to be dequeued on the Queue associated to the
        priority level passed as parameter. If no priority level is passed, it 
        defaults to the regular queue behavior, in FIFO order.
        
        Parameters:
            priority_level (int): The priority level of the queue to peek from.
                Defaults to the highest priority (value 0), like a regular queue.

        Returns:
            (SSLL_Node): An instance of the first node to be dequeded, or None if
                the BPQueue or the Queue associated to the priority level (if any)
                are empty.
        """
        if not priority_level:

            for queue in self._priority_arr:

                if not queue.is_empty():
                    return queue.peek()

        else:
            self._is_valid_priority_level(priority_level)
            queue = self._priority_arr[priority_level]

            if not queue.is_empty():
                return queue.peek()

        return None

    def pprint(self, horizontal=False):
        """
        Prints out the BPQueue in a more readable fashion.

        kwargs:
            horizontal (bool): On True, the node's values will be shown next to
                their associated priority level, linked by an arrow pointing to
                the nodes that are first to be dequeued by priority.
                On False, each node's values will be separated vertically, which
                offers more space to display them if they are lengthy.
        """
        if horizontal:
            string = '<TOP>'

            for i, queue in enumerate(self._priority_arr):
                string += f'\n<|{i}|> '
                current = queue._head

                while current:
                    string += f'{current.value} <- ' if current._next else f'{current.value}' 
                    current = current._next

            string += '\n<END>'
            print(string)

        else:
            string = '<TOP> \n  |'

            for i, queue in enumerate(self._priority_arr):
                string += f'\n<|{i}|>'
                current = queue._head
                if not current:
                    string += ' \n  |'
                while current:
                    string += f'\n  |- {current.value}'
                    current = current._next

            string += '\n<END>'
            print(string)
        
    def split(self, priority_level: int):
        """
        Splits the BPQueue in two by a specified priority level.
        
        Creates and returns a new BPQueue instance with containing all Queues in self,
        starting from the one related to the priority level passed as a parameter
        onwards.

        The original BPQueue will be modified, since the last node of the queue whose
        priority level is one less than the parameter will be unlinked from the its
        _next, which was the first node of the queue to be split up. Its length will
        be reduced, as well as the priority level array, only to hold the Queues before
        the priority level passed as parameter.

        The new BPQueue's length will be the number of nodes counting from the first
        one in the priority array linked to the priority level passed as parameter, as
        well as the number of priority queues, which will be the ones counting from the
        priority level onwards.

        Parameters:
            priority_level (int): The priority level of the where we want to split the
                BPqueue at.

        Returns:
            (BPQueue): A new BPQueue instance containing all Queues from the one splitted
                onwards, whose length is the number of nodes inside those queues.
                The original queue will be modified as detailed above.
        """
        assert 0 < priority_level <= self.get_lowest_priority_lvl(), \
            'You can only split the list from priority 1 onwards to minimum priority.'

        min_priority_level = self.get_lowest_priority_lvl()
        new_bpq = BPQueue(min_priority_level - priority_level)
        j = 0

        for i in range(priority_level, min_priority_level + 1):
            new_bpq._priority_arr[j] = self._priority_arr[i]
            current_node = new_bpq._priority_arr[j]._head

            while current_node:
                new_bpq._length += 1
                current_node = current_node._next

            j += 1

        current_bpq = Array(priority_level)
        self._length = 0

        for i in range(priority_level):
            current_bpq[i] = self._priority_arr[i]
            current_node = current_bpq[i]._head

            while current_node:
                self._length += 1
                current_node = current_node._next

        self._priority_arr = current_bpq
        return new_bpq

    def _is_valid_priority_level(self, priority_level):
        """
        Helper method to validate that the priority level is in range.
        """
        assert 0 <= priority_level <= self.get_lowest_priority_lvl(), \
            'Priority level out of range.'
        
        return True

    class _BPQueueIterator:
        """
        Inner class to generate and return a BPQueue iterator object when
        __iter__ is called.
        """
        def __init__(self, priority_arr):
            self._priority_arr = priority_arr

        def __iter__(self):
            return self

        def __next__(self):
            for queue in self._priority_arr:

                if not queue.is_empty():
                    return queue.dequeue()

            raise StopIteration


if __name__ == '__main__':

    from random import randint, choice
    
    # Instantiate a Queue with max priority level of 0 and maximum of 7.
    bpq = BPQueue(7)

    # Generate and enqueue some random values (3-digit hex colors)
    values = [i for i in '0123456789ABCDEF']
    for i in range(len(bpq._priority_arr)):
        for _ in range(randint(1,3)):
            k = '#'
            for _ in range(0,3):
                k += choice(values)
            bpq.enqueue(k, i)


    #######################################################
    ####  Uncomment each segments of code down below,  ####
    ####  one segment at a time, to test the methods.  ####
    ####                                               ####
    ####  Remember that you can still test all super() ####
    ####  methods if you desire, provided that you     ####
    ####  respect what's mentioned in the comments     ####
    ####  above.                                       ####
    #######################################################


# print(len(bpq))                                           # __len__


# print('Hello!' in bpq)                                    # __contains__
# bpq.enqueue('Hello!')                                     # 
# print('Hello!' in bpq)                                    # /__contains__


# for value in bpq:                                         # __iter__
#     print(value)                                          # /__iter__


# print(bpq)                                                # __str__


# print('-' * 80)                                           # clone
# print('Original list:\n', bpq)                            # 
# print('-' * 80, '\nCloning list...')                      #
# clone = bpq.clone()                                       #
# print('-' * 80, '\nOriginal list:\n', bpq, '\n')          #
# print('Cloned list:\n', clone)                            #
# print('-' * 80, '\nEnqueuing items in both lists...')     #
# bpq.enqueue("I'm in the original BPQ")                    #
# clone.enqueue("And I'm in clone")                         #
# print('-' * 80, '\nDequeuing 1 item in original list...') #
# bpq.dequeue()                                             #
# print('-' * 80, '\nOriginal list:\n', bpq, '\n')          #
# print('Cloned list:\n', clone)                            #
# print('-' * 80)                                           # /clone


# print('-' * 80)                                           # indexOf
# print('Enqueuing {"a":1 } at the end of the BPqueue...')  #
# print('Enqueuing [1,2,3] on priorities 2, 5 and 6...')    #
# print('-' * 80)                                           #
# bpq.enqueue({'a': 1})                                     # 
# bpq.enqueue([1,2,3], 2)                                   # 
# bpq.enqueue([1,2,3], 5)                                   # 
# bpq.enqueue([1,2,3], 6)                                   #
# print('(Priority index, inner bpq index) of {"a": 1}:')   #
# print('\t>', bpq.indexOf({'a': 1}))                       #
# print('-' * 80)                                           #
# print('(Priority index, inner bpq index) of [1,2,3]:')    #
# print('\t> Lazy ON: (first encountered item):', end=' ')  #   
# print(bpq.indexOf([1,2,3], lazy=True))                    #
# print('\t> Lazy OFF: (all encountered items):', end=' ')  #
# print(bpq.indexOf([1,2,3], lazy=False))                   #
# print('-' * 80)                                           # /indexOf


# print('Lowest priority:', bpq.get_lowest_priority_lvl())  # get_lowest_priority_lvl


# print('-' * 80, '\nQueue priority 0:\n')                  # get_queue
# print(bpq.get_queue(0))                                   #
# print('-' * 80, '\nQueue priority 7:\n')                  #
# print(bpq.get_queue(7), '\n', '-' * 80)                   # /get_queue


# print('-' * 80, '\nEnqueuing True (last in queue)...')    # enqueue                  # get_queue
# bpq.enqueue(True)                                         # 
# print('-' * 80, '\nCurrent queue:\n')                     #
# bpq.pprint(True)                                          #
# print('-' * 80, '\nEnqueuing [1,2] as priority 0...')     #
# bpq.enqueue([1,2], 0)                                     #
# print('-' * 80, '\nCurrent queue:\n')                     #
# bpq.pprint(True)                                          #
# print('-' * 80, '\nEnqueuing {"5"} as priority 5...')     #
# bpq.enqueue({'5'}, 5)                                     #
# print('-' * 80, '\nCurrent queue:\n')                     #
# bpq.pprint(True)                                          #
# print('-' * 80)                                           # /enqueue


# print('-' * 80, '\nCurrent queue:\n')                     # dequeue
# bpq.pprint(True)                                          #
# print('-' * 80, '\nDequeing (priority 0)...')             #                   # get_queue
# bpq.dequeue()                                             # 
# print('-' * 80, '\nCurrent queue:\n')                     #
# bpq.pprint(True)                                          #
# print('-' * 80, '\nDequeuing on priority 7...')           #
# bpq.dequeue(7)                                            #
# print('-' * 80, '\nCurrent queue:\n')                     #
# bpq.pprint(True)                                          #
# print('-' * 80, '\nDequeuing on priority 4...')           #
# bpq.dequeue(4)                                            #
# print('-' * 80, '\nCurrent queue:\n')                     #
# bpq.pprint(True)                                          #
# print('-' * 80)                                           # /dequeue


# print('-' * 80, '\nCurrent queue:\n')                     # peek
# bpq.pprint(True)                                          #
# print('-' * 80, '\nPeeking (priority 0)...')              #                   # get_queue
# first_in_queue = bpq.peek()                               # 
# print('    >', first_in_queue)                            #
# print('-' * 80, '\nPeeking on priority 7...')             #
# print('    >', bpq.peek(7))                               #            #
# print('-' * 80, '\nPeeking on priority 3...')             #
# print('    >', bpq.peek(3))                               #
# print('-' * 80, '\nQueue unmodified:\n')                  #
# bpq.pprint(True)                                          #
# print('-' * 80)                                           # /peek


# bpq.dprint()                                              # dprint


# bpq.pprint(horizontal=True)                               # pprint


# bpq.pprint(horizontal=False)                              # pprint


# print('-' * 80, '\nCurrent queue:\n')                     # split
# bpq.pprint(True)                                          #
# print('-' * 80, '\nSplitting by priority 4...')           # 
# second_half = bpq.split(4)                    #
# print('-' * 80, '\nCurrent queue:\n')                     # 
# bpq.pprint(True)                                          #
# print('-' * 80, '\nSplitted queue:\n')                    # 
# second_half.pprint(True)                                  #
# print('-' * 80, '\nEnqueuing to current queue...')        # 
# bpq.enqueue('Enqueued value')                             #
# print('-' * 80, '\nDequeuing from splitted queue...')     # 
# second_half.dequeue()                                     #
# print('-' * 80, '\nCurrent queue:\n')                     # 
# bpq.pprint(True)                                          #
# print('-' * 80, '\nSplitted queue:\n')                    # 
# second_half.pprint(True)                                  # /split
