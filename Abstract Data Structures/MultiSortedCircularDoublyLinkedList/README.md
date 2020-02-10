Multi Sorted Circular Doubly Linked List Abstract Data Structure
==================================

Overview
----------------------------------
Or __**MSCDLL**__ ADS for short:
- ***Multi*** : any of its nodes can be linked to any other MSCDLL instances, allowing chains of lists to be connected in many ways.
- ***Sorted*** : nodes keep their added order (links to each other), and the order is kept or readjusted when adding new nodes or replacing/removing existing ones.
- ***Circular*** : the last node in the list is linked to the first one, and vice-versa.
- ***Doubly Linked List*** : each node holds a reference to the next and the back nodes in the list they are a part of.

Additionally, many lists can trigger and listen to events on other lists via an observer, and react accordingly. This is made possible by the implementation of a **Pub-Sub** (or **Observer**) design pattern. 
    
This is both convenient if you would like to call for operations in all lists at once, and necessary for the integrity of the whole chain if you were to call for actions in one list that affect other ones. 

Like removing a node in one list while it is linked to a different list, for example. Removing it will cause no problems in the list it was called from for its removal, but would break the integrity in other lists that share that node if they are not commanded to relink their nodes accordingly.

Each method and attribute is commented in detail in the script itself. Please, do refer to them to check what they do and how they do it since the explanations presented here are very, very brief.

Moreover, there are several examples in the script ***examples.py***, so feel free to go check them out. Keep in mind that you need to uncomment one block of code at a time to test their functionality, though. Methods will conflict with each other otherwise.


Instructions
----------------------------------
Begin, of course, by importing this script wherever you want to use a MSCDLL.

From there on, you can instantiate **MSCDLL** objects, which are the lists themselves that host the nodes, establish their links and, well, act as this particular kind of linked lists. You can pass several values as args when instantiating them, in which case they will be converted to nodes and linked to each other. Everything is explained in the constructor and the class' methods.

You can also instantiate **MSCDLLNode** objects individually by calling for their own class. This allows you to create nodes independently from MSCDLL objects and do operations with them as you please. Keep in mind that, even though you can manually link them together with their own methods, you should not do so since you will lack the ability to call for MSCDLL methods to handle them properly, which is the whole purpose. So, link them up using those MSCDLL methods.

If you really want to raise the heat, instantiate a **MSCDLLObserver** and start subscribing MSCDLL objects to it. Once you have a couple, you will be able to use ***linked*** methods in MSCDLL instances properly, which affects all subscribers at once. This *Observer* design opens up a powerful arsenal of possibilites, since you are now available not only to link several lists to each other by their nodes, but also trigger certain actions to all of them, like a collective. Remove, add or insert nodes at the same time wherever you choose, clone or reverse massively, filter and modify nodes from different lists, and much more.

***examples.py*** holds several examples of the funcionality of each method of each class. Feel free to check it out. Make sure the main script is at the same level as it, and to uncomment one block of example code at a time, since the methods will conflict with each other if you do not do so.

The world is yours, go.


MSCDLL class
----------------------------------
The one in charge of creating the type of linked lists with that long name in this README's title. By itself, it tries to emulate a Sorted Circular Doubly Linked List. It has much of its characteristics and behavior, and I adapted many of its methods to look like Python lists'. 

The main functionality is dealt with in this class, which accomplishes its task with the help of MSCDLLNode instances, its basic "data storage" class. MSCDLL will store values on itself using node instances created by that helper class, which is compatible with its own behavior. 

They also have their functionality expanded collectively by MSCDLLObserver class, which help adapt and recreate a method called in an MSCDLL instance to many lists at once.

__**Attributes**__
- ***_head*** : a reference to the first node in the list.           
- ***_id*** : the name (id) of the list.             
- ***_length*** : the total amount of nodes the list holds.              
- ***_observer*** : a reference to its assigned MSCDLL observer instance, or None if it does not have one.
    
__**Main methods**__
- ***\_\_init\_\_*** 
- ***\_\_iter\_\_***           
- ***\_\_len\_\_*** 
- ***\_\_eq\_\_***            
- ***\_\_setitem\_\_***      
- ***\_\_getitem\_\_***    
- ***\_\_del\_\_***
- ***\_\_repr\_\_***                    
- ***\_\_str\_\_***                                   
- ***get\_head*** : returns a reference to the head node of the list.        
- ***get\_name*** : returns the linked list's name (id).            
- ***get\_nodes*** : takes a kwarg as a filter, searches the list and returns the nodes that match that filter in a list of tuples in the format: (node index in list, node).
- ***get\_observer*** : returns a reference to the list's observer (MSCDLLObserver assigned instance), or None if it does not have any, or if the observer is invalid or does not contain this instance as a subscriber.     
- ***get\_observer\_subscribers*** : returns a list of all linked lists being observed by this list's assigned MSCDLLObserver instance, or None if this list is not subscribed to an observer, or if the observer is invalid or does not contain this instance as a subscriber.             
- ***set\_name*** : changes the linked list name (id), which also includes all of its nodes _link keys that store the list's name.
- ***set\_nodes\_values*** : gets all nodes in the MSCDLL instance filtered by the respective kwarg and replaces their values for the one passed as parameter.  
- ***append*** : takes a node or a value (which it automatically converts to a valid node), and appends it to the linked list.         
- ***prepend*** : takes a node or a value (which it automatically converts to a valid node), and prepends it to the linked list.            
- ***insert*** : inserts the node or value (which will be converted to a MSCDLLNode) passed as parameter in the specified index position. If 'overwrite' is passed as a kwarg, the node found at the given position will be replaced with the node or value (converted to a node) instead.
- ***pop*** : filters the list according to the passed kwarg and removes the node in the MSCDLL instance that matches that kwarg. It returns a reference to that removed node, or None if the node was not found.               
- ***remove*** : given the passed kwarg, it checks on the list for any matching nodes and removes them. It returns a list of tuples with those removed nodes in the format: (index where node was found, removed node). This method differs from pop() as it matches several instances of nodes instead of just one, and returns their list index. The drawback is that it requires a full list traversal given any scenario, where pop() only requires so in its worst case.         
- ***clear*** : removes all nodes from the list, sets the head reference to None and its length to 0.              
- ***replace*** : using the condition passed as kwarg, it searches on the MSCDLL for instances of nodes that match with it and replaces them with the node or value -which will be casted to a valid MSCDLLNode- passed as parameter.
- ***extend*** : extends the MSCDLL instance with another valid one. Like Python's list's extend().
- ***split*** : splits the MSCDLL instance into two parts, where the second one starts from the node in the original list at the index passed as a parameter.            
- ***clone*** : creates a shallow copy of the linked list and returns a reference to it.          
- ***indexOf*** : takes value (or node, in which case it will take its value) and searches in the list for all nodes whose values match with it. It returns a tuple containing the indexes in the  linked list where the matching nodes were found.             
- ***valueOf*** : takes an index value, searches on the list to find the node in that given index and returns it.
- ***reverse*** : switches each node's 'back' and 'next' references and repositions the head reference to the last node in the list, effectively reversing it in place. This method is the equivalent to Python's list[ : : -1 ].       
- ***subscribe*** : calls for subscribe() in the MSCDLLObserver instance passed as a parameter, which adds this list to its subscribers. It also sets that observer instance as this list's observer.       
- ***unsubscribe*** : calls for unsubscribe() in the MSCDLLObserver instance passed as a parameter, which removes this list to its subscribers. It also sets this list's _observer field to none.         
- ***is\_empty*** : returns True is the list is empty. False othewise.
- ***iter\_reverse*** : returns an _MSCDLLReverseIterator instance, which can be used as an iterator that traverses the list in reverse order.    
- ***dprint*** : prints the MSCDLL instance in a 'debugging' fashion.

__**Methods linked to the observer to call for all lists**__
- ***linked\_append*** : calls for the assigned observer's *\_append* method to append a node or a value (which is converted to a node) to all of its subscribers.
- ***linked\_prepend*** : calls for the assigned observer's *\_prepend* method to prepend a node or a value (which is converted to a node) to all of its subscribers   
- ***linked\_insert***** : calls for the assigned observer's *\_insert* method to insert a node or a value (which is converted to a node) into all of its subscribers at the given position index, or to overwrite the node at that index if 'overwrite' is True.
- ***linked\_pop*** : calls for the assigned observer's *\_pop* method to pop a node from all of its subscribers at the given position index.           
- ***linked\_remove*** : calls for the assigned observer's *\_remove* method to remove a node from all of its subscribers at the given the passed kwarg.           
- ***linked\_clear*** : calls for the assigned observer's *\_clear* method to unlink all nodes from all of its subscribers. Each list's length is set to 0 and head reference to None.
- ***linked\_replace*** : calls for the assigned observer's *\_replace* method to replace all nodes found filtering by the passed kwarg in all of its subscribers with the node or value passed as parameter.       
- ***linked\_replace*** : calls for the assigned observer's *\_extend* method to extend all of its subscribers as indicated by the passed kwarg.          
- ***linked\_clone*** : calls for the assigned observer's *\_clone* method to clone all of its subscribers.
- ***linked\_reverse*** : calls for the assigned observer's *\_reverse* method to reverse all of its subscribers in place.        
- ***linked\_indexOf*** : calls for the assigned observer's *\_indexOf* method on each of its subscribers to get the index position of the nodes whose values match the value or node passed as a parameter (if a node was passed, its value will be considered).          
- ***linked\_valueOf*** : calls for the assigned observer's *\_valueOf* method on each of its subscribers to get the node's values on the index position passed as a parameter.
- ***linked\_split*** : calls for the assigned observer's *\_split* method to split all of its subscribers by the given index.         
- ***linked\_set\_nodes\_values*** : calls for the assigned observer's *\_set\_nodes\_values* method change each of their subscribers' nodes' values that match the filter stated in the kwarg values to the value passed as parameter.
- ***linked\_get\_head*** : calls for the assigned observer's *\_get\_head* method on all of its subscribers to get an instance of their head nodes.
- ***linked\_get\_nodes*** : calls for the assigned observer's *\_get\_nodes* method to get all nodes in all of its subscribers using the passed kwarg as a filter.     
- ***linked\_is\_empty*** : calls for the assigned observer's *\_is\_empty* method on all of its subscribers to check if whether they are empty or not.    

__**Helper methods**__
- ***\_assert_subscription*** : checks if the list is subscribed to a valid MSCDLLObserver instance, and that MSCDLLObserver has the list as one of its subscribers. Returns True if so. Otherwise, it raises a AssertionError.   
- ***\_nodify*** : takes an instance of MSCDLLNode or any value and: (1) if it is a node, it adds the caller's MSCDLL instance's name to the node's **\_links**' keys and an empty dictionary as its value, or (2) if it is any value, it converts it to a MSCDLLNode and with that node it does the same as in (1).
- ***\_get\_node\_by\_idx*** : takes an integer index (idx) and returns a reference to the node in that index position in the list. Accepts negative indexing, like a regular Python list.
- ***\_get\_node\_by\_name*** : given the node's name (id) passed as parameter, it searches on the list for a node with that name and returns it. Otherwise, it returns None.


Iterator classes
----------------------------------
- **_MSCDLLIterator Class** : A class resposible for generating iterator objects that traverse  the MSCDLL forwards. From the head node to the last one.
- **_MSCDLLReverseIterator** : A class resposible for generating iterator objects that traverse the MSCDLL backwards. From the last node to the head one.


MSCDLLNode class
----------------------------------
The "data storage" class, responsible for creating valid node objects to store inside MSCDLL instances.

The nodes generated here are able to hold any kind of values, are unique from each other by default (you can change this property, though), and have a dictionary to store links to their back and next nodes of every single list they are in.

__**Attributes**__
- ***value*** : the node's value.         
- ***\_links*** : a dictionary whose keys are the MSCDLL lists' names the node is assigned to. A node has no limits to how many lists it can be in, but must not be inside the same list more than once.             
- ***\_id*** : the node name (id).

__**Main methods**__
- ***\_\_init\_\_***       
- ***\_\_str\_\_***         
- ***\_\_repr\_\_***        
- ***get\_links*** : returns a dictionary where the keys are all of the MSCDLL instances the node is linked to, and their values, the 'next' and 'back' node references in them. 
- ***get\_name*** : returns the name (id) of the node.            
- ***get\_next*** : returns a reference to this node's next node in the MSCDLL instance passed as parameter.
- ***get\_back*** : returns a reference to this node's back node in the MSCDLL instance passed as parameter.  
- ***get\_MSCDLL\_links*** : returns a dictionary whose key is the MSCDLL list passed as parameter, and its values are this node's 'back' and 'next' references in that list. 
- ***set\_name*** : sets the name (id) of this node to the one passed as parameter.           
- ***set\_next*** : sets this node's 'next' reference in the MSCDLL list passed as parameter to a valid MSCDLLNode instance, also passed as parameter.
- ***set\_back*** : sets this node's 'back' reference in the MSCDLL list passed as parameter to a valid MSCDLLNode instance, also passed as parameter.         
- ***set\_MSCDLL\_links*** : creates a key with the MSCDLL instance's name (id) inside the *_links* dictionary and assigns an empty dictionary as its value. 
- ***pprint*** : prints the node out in a 'debugging' fashion. Emulates JSON format.


MSCDLLObserver Class
----------------------------------
An observer class designed to host MSCDLL instances which are to be connected to -and to react to- each other's actions.

It follows the Observer (Pub-Sub) pattern. MSCDLL instances subscribe to an observer and, if they want to affect all lists on purpose or to perform safe operations on itself (like destroying a node without breaking the integrity of other lists that host it), then they call for the 'linked' version of their methods instead of their regular ones. 

If they do so, the action will be redirected to the observer, and the observer will adapt and replicate that action on all of its subscribers.

Even though an observer instance is capable of calling for its methods by itself, it is strongly recommended not to do so unless you are really certain on what those methods do and how they do it. This observer class is designed to be a catalyst between a caller MSCDLL instance all other lists that share its same observer.

So, the intended behavior is for that MSCDLL instance to command the method to apply to all lists by its own 'linked' version, and for the observer to adapt that call and redirect it to all other lists.

__**Attributes**__
- ***\_subscribers*** : a list holding all MSCDLL instances subscribed to it.       
- ***\_id*** : the name (id) of the observer.
    
__**Main methods**__
- ***\_\_init\_\_***          
- ***\_\_str_\_***              
- ***subscribe*** : takes a valid MSCDLL instance and adds it to its *_subscribers* list. It also sets that instance's *_observer* to point to this one. 
- ***unsubscribe*** : takes an MSCDLL instance inside *_subscribers* and removes it. It also sets its *_observer* pointer to None.        
- ***unsubscribe\_all*** : unsubscribes all MSCDLL instances stored in *_subscribers*. Each one of those instances will have their *_observer* set to None, and the observer's *_subscriber* list will be emptied.     
- ***get\_name*** : returns the name (id) of the observer.
- ***get\_subscriber*** : searches for a subscriber whose name (id) matches the one passed as a parameter. Returns a reference to the found subscriber or None if there was no subscriber found.   
- ***get\_subscribers*** : returns a reference to the list containing the references to all the observer's subscribers.         
- ***set\_name*** : sets the name of the observer to the one passed as parameter.

__**Private methods**__
(meant to be called by MSCDLL instances 'linked' methods)
- ***\_append*** : calls for each subscriber's *append()* to add a node or value (which is converted to a node), at the end of all of them.             
- ***\_prepend*** : calls for each subscriber's *prepend()* to add a node or value (which is converted to a node), to the beginning of all of them, as their head node.             
- ***\_insert*** : calls for each subscriber's *insert()* to add or replace a node or value (which is converted to a node), on each list at the index specified by the 'position' parameter. 
- ***\_remove*** : calls for each subscriber's *remove()* to remove any instances of nodes whose indexes, values or names match the ones passed as kwargs.     
- ***\_pop*** : calls for each subscriber's *remove()* to remove a node from them at the passed index kwarg, or by the passed node's name.               
- ***\_clear*** : calls for each subscriber's *clear()* to unlink all nodes from them, reset their length and set their head nodes to None.
- ***\_split*** : calls for each subscriber's *split()* to split by the index passed as parameter.
- ***\_extend*** : calls for each subscriber's *extend()* to extend them according to the mode passed as kwarg.              
- ***\_clone*** : calls for each subscriber's *clone()* to create and return a shallow copy of each of them.              
- ***\_replace*** : calls for each subscriber's *replace()* to replace a node from them at the passed index kwarg, or by the passed node's name.
- ***\_indexOf*** : calls for each subscriber's *indexOf()* to get the indexes of the node(s) whose value matches the value (or node's value) passed as parameter, for each list.            
- ***\_valueOf*** : calls for each subscriber's *valueOf()* to get the node at the index position passed as parameter.            
- ***\_reverse*** : calls for each subscriber's *reverse()* to reverse all of them in place.
- ***\_get\_head*** : calls for each subscriber's *get\_head()* to check return a reference to the head node of each list.           
- ***\_get\_nodes*** : calls for each subscriber's *get_nodes()* to get all of their nodes that match the given kwarg used as a filter.          
- ***\_is\_empty*** : calls for each subscriber's *is\_empty()* to check if each of them is an empty list or not.
- ***\_set\_nodes\_values*** : calls for each subscriber's set_nodes_values() to set the values of all matching nodes given the kwarg to the one passed as a parameter. 


What I learned from this project
----------------------------------
- You ought not to delete elements from the same list you are iterating. Since you are attempting to change the list size while still looping through it, the run-time integrity breaks and the program crashes.
- Python's 'is' operator is very similar to Javascript's '==='. I did not know, I thought it was just a more humanly-readable way to type '=='. A whole new world opened up for me now that I am aware that you can check for value equality using one operator, and for value and type equality at the same one using another.
- When dealing with an Observer design pattern, it is very important to unlink a subscriber from its observer before deleting that subscriber itself. If we don't, then the observer will still think its subscriber is bound to it, and keep trying to call for its methods when a sending messages, alas, rising exceptions or provoking a wonky behavior.
- One does not need to tell the observer to rename a list, as we can just rename the its nodes' links that refer to it and the list name (id) itself. Connected lists share nodes. If a node changes the name of a list reference it is connected to, it will automatically adjust itself for all lists that node is linked to.
- I exhausted ideas to traverse a circular list. Some options in the script might not seem optimal, but I left them to remember particular ways I came up with to do so when I revisit this ADS later.
- I thought I understood linked lists when I managed to make SinglySortedLinkedList ADS work. Gosh I was naive back then.
- I really, REALLY need to teach myself to keep projects simple and brief. This one is fully functional, but I certainly overdid it. It took me a good amount of time to complete it, time I could have spent learning or practising other topics. I regret little, though. It was an awesome experience.
  
  
### Thank you for reading and for taking your time to check this project out!
