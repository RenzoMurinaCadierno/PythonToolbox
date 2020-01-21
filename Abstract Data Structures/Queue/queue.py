from modules.sortedSinglyLL import SortedSinglyLL, SSLL_Node

class Queue(SortedSinglyLL):
    """
    A class that tries to emulate the behavior of a Queue data structure.

    It extends (and limits some capabilities of) its parent class: 
    a Sorted Singly linked list.

    Methods:
        __str__ : Overrides super().__str__() to print out the queue
                  in a more intuitive way.
        clear : Removes all nodes from the queue. This is an unmodified 
                super() method to make you remember you can still use 
                all of those on instances of this class too.
        clone : Overrides super().clone() so that an instance of the
                Queue class is returned, and not one of the parent's.
        peek : Returns a reference to the top of the queue.
        dequeue : Removes the node from the top of the queue and returns
                  a reference to it.
        enqueue : Adds a node at the end of the queue.
        split : Overrides super().split() so that both halves can be
                returned as queue instances.
    """

    def __init__(self, *args):
        super().__init__(*args)

    def clear(self):                                                   
        """
        Same as parent's clear(). Left here to remember it is a 
        thing also for Queue instances.
        """   
        super().clear()

    def clone(self, _queue_instance=None):                            
        """ 
        Clones the Queue and returns an a reference to the new one.

        _queue_instance is a private variable used by self.split().
        Do not assign a value to it unless you are trying to clone 
        another queue using this instance's method, in which case, 
        it is more practical to use that other queue's own split().

        This method is intended to override super().clone(), as that
        class clone() returns the second half of the list as an
        instance of itself, and not of its children's (we need a
        Queue to be returned, not a SortedSinglyLL).
        """
        clone = Queue()
        current = _queue_instance._head if _queue_instance else self._head
        
        while current:
            node = SSLL_Node(current.get_value())
            clone.append(node)
            current = current._next

        return clone

    def peek(self):                                  
        """
        Returns a reference to the top of the queue.
        """
        return self._head

    def dequeue(self):                                      
        """
        Removes the top element from the queue and returns a reference to it.
        """
        return super().pop(0)    

    def enqueue(self, node_or_value):                         
        """
        Pushes the object passed as a parameter to the end of the queue.

        If the object is not a valid node instance, it is converted to one.
        """
        node = self._nodify(node_or_value)
        self.append(node)

    def split(self, idx):                                  
        """
        Splits the queue into two, where the second half starts with the
        index passed as a parameter.

        A valid split can only occur from index 1 onwards. 

        This method is the only one intended to assign a different parameter
        to clone(), since it is required to pass the second half of the list 
        as a Queue instance, thus overriding the default parent class it 
        would normally return. Check the behaviour of super().split(idx)
        for a better understanding.
        """
        splitted = super().split(idx)
        second_half_clone = self.clone(splitted)
        return second_half_clone

    def __str__(self):
        return super().__str__(start="<TOP> ", end=' <END>', separator='<-')


    ################################################################
    # Uncomment the methods below if you really want to restrict   #
    # this class to the default basic behavior of a Stack. Note,   #
    # however, that clone() and split() methods will stop working  #
    # since they depend on super().append(), and it will be        #
    # overwritten.                                                 #
    # If you choose to activate all of the following methods, then #
    # only clear(), peek(), dequeue() and enqueue() -as well as    #
    # all other parent's methods that do not require the activated #
    # ones- will work.                                             #
    ################################################################
    #                                                              #
    # def append(self, value):                                     #
    #     print('You can only enqueue into a queue.')              # 
    #     return False                                             #
    #                                                              #   
    # def insert(self, value):                                     #
    #     print('You can only enqueue into a queue.')              #
    #     return False                                             #
    #                                                              #
    # def set_nodes(self, value, overwrite=False):                 #
    #     print('You cannot overwrite items inside a queue.')      #
    #     return False                                             #
    #                                                              #
    # def __setitem__(self, idx, value):                           #
    #     print('You cannot set items directly into a queue.')     #
    #     return False                                             #
    ################################################################


if __name__ == '__main__':


    #######################################################
    ####  Uncomment each segments of code down below,  ####
    ####  one segment at a time, to test the methods.  ####
    ####                                               ####
    ####  Remember that you can still test all super() ####
    ####  methods if you desire, provided that you     ####
    ####  respect what's mentioned in the comments     ####
    ####  above.                                       ####
    #######################################################


    q = Queue(True, 1, None, [1,2], {"a":3}, [])


    # print(q)                               # enqueue
    # q.enqueue("asd")                       #    
    # print(q)                               # /enqueue


    # print(q)                               # dequeue
    # removed_node = q.dequeue()             # 
    # print(removed_node)                    #   
    # print(q)                               # /dequeue


    # print(q)                               # peek
    # end = q.peek()                         #    
    # print(end)                             #
    # print(q)                               # /peek


    # print(q)                               # clear
    # q.clear()                              #
    # print(q)                               # /clear


    # print(q)                               # split
    # half_queue = q.split(3)                #    
    # print(half_queue)                      #
    # print(q)                               #
    # half_queue.enqueue("I'm in 2nd half!") #
    # q.dequeue()                            #
    # print(half_queue)                      #
    # print(q)                               # /split


    # print(q)                               # clone
    # clone = q.clone()                      #    
    # print(q)                               #
    # print(clone)                           # 
    # q.enqueue("I'm not in clone!")         #
    # clone.dequeue()                        #
    # print(q)                               #
    # print(clone)                           # /clone