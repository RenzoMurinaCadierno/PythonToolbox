Bounded Priority Queue Abstract Data Structure
==================================

Overview
----------------------------------
A class which attempts to emulate the basic behavior of a Bounded Priority Queue (BPQueue).

A BPQueue introduces the concept of priority when storing, enqueing, dequeuing or peeking any of its elements. Its constructor takes an integer which represents the lowest priority level and creates an array of that many Queue instances. The first Queue will be stored in array[0] and it is considered to be the highest priority, where elements are be dequeded by default. The last queue will be inside array[-1], where elements are normally enqueued. 
    
However, enqueue(), dequeue() and peek() also accept an optional integer value for a priority level as a parameter. If given, only the individual queue related to that priority level will be affected by those methods. For example, if you call for enqueue(item, 3), the item is enqueued to the Queue whose priority is 3. Dequeue(5) will dequeue the first item in the queue whose priority is 5. And so on.

This class supports those three basic Queue methods as well as cloning, getting indexes of items, splitting by priority level and printing both for debugging (in detail) and for visualizing the queue as a whole in a comfortable way.

Attributes, methods and classes
----------------------------------
**Methods:**
- *\_\_init\_\_*
- *\_\_contains\_\_*
- *\_\_iter\_\_*
- *\_\_len\_\_*
- *\_\_str\_\_*
- _clone_ : Creates and returns a shallow copy of self.
- _dequeue_ : Dequeues a node from the BPQueue or from one of its priority level queues.
- _dprint : Prints out the BPQueue in great detail.
- _enqueue_ : Enqueues a node from the BPQueue or from one of its priority level queues.
- _indexOf_ : Returns a tuple containing the BPQueue position index(es) and the in-priority-level queue index(es) a value.
- _get\_lowest\_priority\_lvl_ : Returns the lowest priority level value of the BPQueue.
- _get\_queue_ : Returns the Queue instance associated to the priority level.
- _peek_ : Returns the next node to be dequeued from the BPQueue or from one of its priority level queues.
- _pprint_ : Prints out the BPQueue in a more readable version than _print(self)_.
- _split_ : Splits the BPQueue in two by a specified priority level.

**Helper methods:**
    *_is_valid_priority_level* : Helper method to validate that the priority level is in range.

**Inner classes:**
    *_BPQueueIterator* : Generates and return a BPQueue iterator object when *\_\_iter\_\_* is called.

Instructions
----------------------------------
Make sure the 'modules' folder is in the same directory as bpqueue.py.

Just import this file in your script and instantiate the main class. From there on, you can create BPQueue objects. Everything is commented in the code and in the module files, feel free to check them out.

There are examples in the main program down below in the script. They are designed to show you the usage.

TODOs
----------------------------------
BPQueue is fully functional. You can enqueue, dequeue and peek like a regular queue or you can do so by priority levels. Cloning, splitting by priority levels, getting nodes by index and printing both for visual comprehension and debugging are all supported and working fine.

However, there might yet be some improvements and additions to implement in order to make it more efficient and to add extra -and useful- functionalities to the class. I will type some that come to my mind, but will not commit to them now or in the near future, since I want to keep on moving forwards with Data Structures and other projects I want to tackle.

Feel free to have a go at them if you want to practice, or leave me a message if you want to request a pull to update this same script. I am open to co-working, and I will not hesitate to give you credits for your contributions ;)

- ***split_by_node(self, node_or_value)*** : You can use the current _split_ method to divide the BPQueue into two given priority level, but it would be handy to be able to do so by a specific node -or value, we can nodify it with Queue's *_nodify()*-. Tackling this idea would involve separating all nodes in the priority Queue where target node is situated. Previous nodes would be the last ones in the BPQueue (without changing priority), and nodes  in the same Queue counting from the target one onwards would be part of priority 0 Queue inside a new BPQueue.
-***split_by_index(self, node_bpq_idx)*** : If a method to get the node by its BPQueue index is developed, a split in the same fashion as above can be performed by targetting a node using that index instead of its value. A very simple general indexing was attempted in *dprint*, so that could be a starting point.
-***Deque*** : A deque is a queue where nodes can be peeked, enqueued or dequeued from both of its ends. Currently, BPQueue can target any inner priority queue or itself as a whole Queue, but it can only apply the main methods in a traditional way. Even though this is fine since a Queue is intended to work that way, we could introduce the ability to apply them to both ends on any priority queue or on itself, which could be useful for certain operations. A deque can be an extension of the methods inside BPQueue, or a whole new class.
-***UPQueue*** : A BPQueue is what its title implies: a BOUNDED queue. That means, its priority levels are set when it is constructed and cannot change, since they are stored in an Array. Even though this might be convenient due to speed and memory efficiency (an Array does not grow or shrink, which does not consume storage space or time since it does not copy elements to a new Array), it severely limits the flexibility a Python list can offer us in terms of expansion and reduction. An UNBOUNDED Priority Queue can be created as a whole class, very similar to BPQueue, but not limited to any given priority level. We can start with some -or even none-, and add them on-the-way as we need. This can prove to be a good challenge, and a very useful project.

What learned from this project
----------------------------------
- Queues are implemented in everyday life, but they can be severy limited by their own structure. I mean, people can still change to different queues in a supermarket if they see them emptier than the others. Or people with limited capabilities can be positioned on queues with a higher priority than others, or up front the queue they are in. Several computers can queue documents to only one printer, but it is too demanded, some papers that are urgent can be queued in front of any other one in line. Examples like this make a Priority Queue really useful.
- Challenge myself out of my confort zone every once in a while (not to say several times). When designing *split()*, I quickly came up with a solution of just making two different BPQueues, shallow copy the nodes and their relationships, add them to the queues and return a reference to both heads. Though this proved to be costly, so I scraped it all out and designed an alternative way around that involved creating a new array with length equal to the amount of nodes from the splitted one onwards, link those nodes to that array, unlink them from the previous one, cut the original array to hold all previous nodes, and reindex the new one. Much more efficient in terms of storage and speed.
- Once you get a grasp of Arrays and Sorted Linked Lists, it is a blast how easy it they are dealing with, and how many issues they are capable of solving. They have their fair share of drawbacks, though.
- One struggles a bit harder using a Singly Sorted Linked List that has a next but not a previous field. Iterations to get to a desired node are real and repeat themselves lots throughout each script. The more I code, the more I am convinced that that extra memory space assigned to link a node to its predecessor worths the pain.
- I really should start focusing a little in GUI instead of just the console. Not that I do not know how to design a GUI (I'm lacking practice, though), but it's just that I much more of a wiring guy, not a designer myself. But GUIs are a must at programming, so I should stop whining and get on it.

### Thank you for reading and for taking your time to check this project out!
