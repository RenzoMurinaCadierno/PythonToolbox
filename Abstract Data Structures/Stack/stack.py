from modules.sortedSinglyLL import SortedSinglyLL, SSLL_Node

class Stack(SortedSinglyLL):
    """
    A class that tries to emulate the behavior of a Stack data structure.

    It extends (and limits some capabilities of) its parent class: 
    a Sorted Singly linked list.

    Methods:
        __str__ : Overrides super().__str__() to print out the stack
                  in a more intuitive way.
        clone : Overrides super().clone() so that an instance of the
                Stack class is returned, and not one of the parent's.
        peek : Returns a reference to the top of the stack.
        pop : Removes the node from the top of the stack and returns
              a reference to it.
        push : Adds a node to the top of the stack.
        split : Overrides super().split() so that both halves can be
                returned as Stack instances.
    """

    def __init__(self, *args):
        super().__init__(*args)

    def clear(self):
        """
        Same as parent's clear(). Left here to remember it is a 
        thing also for Stack instances.
        """   
        super().clear()

    def clone(self, _stack_instance=None):
        """ 
        Clones the Stack and returns an a reference to the new one.

        _stack_instance is a private variable used by self.split().
        Do not assign a value to it unless you are trying to clone 
        another stack using this instance's method, in which case, 
        it is more practical to use that other stack's own split().

        This method is intended to override super().clone(), as that
        class clone() returns the second half of the list as an
        instance of itself, and not of its children's (we need a
        Stack to be returned, not a SortedSinglyLL).
        """
        clone = Stack()
        current = _stack_instance._head if _stack_instance else self._head
        
        while current:
            node = SSLL_Node(current.get_value())
            clone.append(node)
            current = current._next

        return clone

    def peek(self):
        """
        Returns a reference to the top of the stack.
        """
        return self._head

    def pop(self):
        """
        Removes the top element from the stack and returns a reference to it.
        """
        head = super().pop(0)
        return head

    def push(self, node_or_value):
        """
        Pushes the object passed as a parameter to the top of the stack.

        If the object is not a valid node instance, it is converted to one.
        """
        node = self._nodify(node_or_value)
        self.prepend(node)

    def split(self, idx):
        """
        Splits the stack into two, where the second half starts with the
        index passed as a parameter.

        A valid split can only occur from index 1 onwards. 

        This method is the only one intended to assign a different parameter
        to clone(), since it is required to pass the second half of the list 
        as a Stack instance, thus overriding the default parent class it 
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
    # only clear(), peek(), pop() and push() -as well as all other #
    # parent's methods that do not require the activated ones-     #
    # will work.                                                   #
    ################################################################
    #                                                              #
    # def append(self, value):                                     #
    #     print('You can only push into a stack.')                 # 
    #     return False                                             #
    #                                                              #   
    # def insert(self, value):                                     #
    #     print('You can only push into a stack.')                 #
    #     return False                                             #
    #                                                              #
    # def set_nodes(self, value, overwrite=False):                 #
    #     print('You cannot overwrite items inside a stack.')      #
    #     return False                                             #
    #                                                              #
    # def __setitem__(self, idx, value):                           #
    #     print('You cannot set items directly in a stack.')       #
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
    ####  above                                        ####
    #######################################################


    s = Stack(True, 1, None, [1,2], {"a":3}, [])
    
    # print(s)                            # push
    # s.push("asd")                       #    
    # print(s)                            # /push

    # print(s)                            # pop
    # s.pop()                             #    
    # print(s)                            # /pop

    # print(s)                            # peek
    # top = s.peek()                      #    
    # print(top)                          #
    # print(s)                            # /peek

    # print(s)                            # split
    # half_stack = s.split(3)             #    
    # print(half_stack)                   #
    # print(s)                            # /split

    # print(s)                            # clone
    # clone = s.clone()                   #    
    # print(s)                            #
    # print(clone)                        # 
    # s.push("I'm not in clone!")         #
    # clone.pop()                         #
    # print(s)                            #
    # print(clone)                        # /clone