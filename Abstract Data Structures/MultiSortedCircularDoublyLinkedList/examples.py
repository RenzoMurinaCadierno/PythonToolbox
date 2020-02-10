################################################################################
########                                                                ########
########         MSCDLL, MSCDLLObserver and MSCDLLNode examples         ########
########                                                                ########
################################################################################


# INSTRUCTIONS:
#
#   > Uncomment each segment of code once at a time and run the script. 
#     Read each segment and check the examples in console to fully understand them.
#
#   > Keep the imports, instantiations and 'print('#' * 80)' references that are 
#     uncommented as they are. You will need them for the examples to work.


from mscdll import MSCDLL, MSCDLLObserver, MSCDLLNode

node_1 = MSCDLLNode('Node 1', name='node_1')
node_2 = MSCDLLNode({'Node': 2}, name='node_2')
node_3 = MSCDLLNode(['Node', 3], name='node_1')

obs_1 = MSCDLLObserver(name='I\'m watching you')
obs_2 = MSCDLLObserver()

mscdll_0 = MSCDLL()
mscdll_1 = MSCDLL(
    node_1, 'asd', True, None, 1, True, [], {}, {'a': 1}, False, True, 
    name='SMCDLL 1',
)
mscdll_2 = MSCDLL(
    'fff', True, [], 1, {}, {'b': 2}, False, 0, {}, node_2,
    name='SMCDLL 2',
    observer=obs_1
)
mscdll_3 = MSCDLL('lala', 2, [False], 0.5, name=3)
mscdll_4 = MSCDLL('lala', 2, [False], node_1, 0.5)
mscdll_5 = MSCDLL('lala', 2, [False], 0.5)

print('#' * 80)  



################################################################################
########                  MSCDLLNode methods examples                   ########
################################################################################


# # __init__
#
# print('\n  > Creating a node named node_4 with value [\'node\', {4}]...\n')
# node_4 = MSCDLLNode(['node', {4}], name='node_4')
# print('#' * 80)   
# print('\nnode_4 string representation is:', node_4)
# print('\nnode_4 detailed representation is:\n')
# node_4.pprint()
#
# # /__init__


# # get_name
#
# print('\nnode_1\'s name (id) is:', node_1.get_name(), '\n')
#
# # /get_name


# # set_name
#
# print('\nnode_1\'s name (id) is:', node_1.get_name(), '\n')
# print('#' * 80)   
# print('\n  > Setting name of node_1 to \'Testing node name\'...\n')
# node_1.set_name('Testing node name')
# print('#' * 80)   
# print('\nnode_1\'s name (id) is:', node_1.get_name(), '\n')
#
# # /set_name


# # get_links
#
# print('\nnode_1\'s links are:\n\n', node_1.get_links(), '\n')
#
# # /get_links


# # get_MSCDLL_links
#
# print('\nnode_1\'s \'SMCDLL 1\' (mscdll_1) links are:\n')
# print(node_1.get_MSCDLL_links(mscdll_1), '\n')
#
# # /get_MSCDLL_links

# # set_MSCDLL_links
#
# print('\nnode_3 detailed representation is:\n')
# node_3.pprint()
# print('#' * 80)   
# print('\n  > Adding a link field for MSCDLL_2 (mscdll_2) list...\n')
# node_3.set_MSCDLL_links(mscdll_2)
# print('#' * 80)   
# print('\nnode_3 detailed representation is:\n')
# node_3.pprint()
#
# # /set_MSCDLL_links


# # get_next
#
# print('\nnode_2 detailed representation is:\n')
# node_2.pprint()
# print('#' * 80)   
# print('\nnode_2\'s mscdll_2 \'next\' reference is:', node_2.get_next(mscdll_2), '\n')
#
# # /get_next


# # get_back
#
# print('\nnode_1 detailed representation is:\n')
# node_1.pprint()
# print('#' * 80)   
# print('\nnode_2\'s mscdll_1 \'back\' reference is:', node_1.get_back(mscdll_1), '\n')
#
# # /get_back


# # set_next
#
# print('\nnode_3 detailed representation is:\n')
# node_3.pprint()
# print('#' * 80)   
# print('\n  > Adding a link field for MSCDLL_2 (mscdll_2) list...\n')
# node_3.set_MSCDLL_links(mscdll_2)
# print('#' * 80)   
# print('\nnode_3 detailed representation is:\n')
# node_3.pprint()
# print('#' * 80)   
# print('\n  > Adding node_2 as node_3\'s mscdll_2 \'next\' reference...\n')
# node_3.set_next(mscdll_2, node_2)
# print('#' * 80)   
# print('\nnode_3 detailed representation is:\n')
# node_3.pprint()
#
# # /set_next


# # set_back
#
# print('\nnode_3 detailed representation is:\n')
# node_3.pprint()
# print('#' * 80)   
# print('\n  > Adding a link field for MSCDLL_2 (mscdll_2) list...\n')
# node_3.set_MSCDLL_links(mscdll_2)
# print('#' * 80)   
# print('\nnode_3 detailed representation is:\n')
# node_3.pprint()
# print('#' * 80) 
# print('\n  > Adding node_2 as node_3\'s mscdll_2 \'back\' reference...\n')
# node_3.set_back(mscdll_2, node_2)
# print('#' * 80)   
# print('\nnode_3 detailed representation is:\n')
# node_3.pprint()
#
# # /set_back


# # pprint
#
# print('\nnode_1 detailed representation is:\n')
# node_1.pprint()
#
# # /pprint



#################################################################################
########       MSCDLL methods examples (not subscribed to observer)      ########
#################################################################################


# # dprint
#
# print('     Debug print (no node details)     '.center(80), '\n')      
# mscdll_1.dprint()                                          
#                                              
# # /dprint


# dprint (showing node details)
#                                        
# print('     Debug print (with node details)     '.center(80), '\n')    
# mscdll_1.dprint(show_details=True)
#                                                   
# /dprint                         


# # __str__
#
# print('\nLazy string representation of mscdll_1:\n')            
# print(mscdll_1, '\n')                                                                                         
#
# # /__str__


# # __len__
#
# print('\nLength (amount of nodes in mscdll_1):', len(mscdll_1), '\n')                                                        
#
# # /__len__


# # __eq__
#
# print('\nmscdll_3 == mscdll_1? -', mscdll_3 == mscdll_1, '\n')      
# print('#' * 80)               
# print('\nmscdll_3 == mscdll_5? -', mscdll_3 == mscdll_5, '\n')      
#
# # /__eq__                              


# # __del__
#
# print('\nShowing mscdll_1 contents:\n')
# print(mscdll_1, '\n')
# print('#' * 80)
# print('\n  > Deleting mscdll_1...\n')
# del mscdll_1
# print('#' * 80)
# print('\n  > Trying to show mscdll_1 contents:\n')
# try:
#     print(mscdll_1, '\n')
# except NameError:
#     print('    >>> List was successfully deleted if no other pointers are referencing it.\n')
#
# # /__del__


# # __iter__
#
# print('\n  > Displaying each node in mscdll_1 in detail:\n')
# for node in mscdll_1:
#     node.pprint()
#     print('-' * 80)
#
# # /__iter__


# # __getitem__
#
# print('\nLazy string representation of mscdll_1:\n')            
# print(mscdll_1, '\n')     
# print('#' * 80) 
# print('\nNode index 0 in mscdll_1 is:')
# mscdll_1[0].pprint()
# print('#' * 80)
# print('\n(positive index) Last node in mscdll_1 is:')
# mscdll_1[len(mscdll_1)-1].pprint()
# print('#' * 80)
# print('\n(negative index) Last node 0 in mscdll_1 is:')
# mscdll_1[-1].pprint()
#
# # /__getitem__


# # __setitem__
#
# print('\nLazy string representation of mscdll_1:\n')            
# print(mscdll_1, '\n')     
# print('#' * 80) 
# print('\nNode index 0 in mscdll_1 is:')
# mscdll_1[0].pprint()
# print('#' * 80)
# print('\n  > Changing node index 0 to node_2 (instance of MSCDLLNode)...\n')
# mscdll_1[0] = node_2
# print('#' * 80)
# print('\nNode index 0 in mscdll_1 is:')
# mscdll_1[0].pprint()
# print('#' * 80)
# print('\nLast node in mscdll_1 is:')
# mscdll_1[-1].pprint()
# print('#' * 80)
# print('\n  > Changing last node to a random string (not an instance of MSCDLLNode)...\n')
# mscdll_1[-1] = 'random'
# print('#' * 80)
# print('\nLast node in mscdll_1 is:')
# mscdll_1[-1].pprint()
#
# # /__setitem__


# # indexOf
#
# print('\nLazy string representation of mscdll_1:\n\n', mscdll_1, '\n')
# print('#' * 80)
# print('\nIndexes of values \'[]\' in mscdll_1 are:\n')
# print(mscdll_1.indexOf([]), '\n')
# print('#' * 80)
# print('\nIndexes of values \'True\' in mscdll_1 are:\n')
# print(mscdll_1.indexOf(True))
# print('\n  > Note that indexOf is designed to treat truthy and falsy values the same.')
# print('\n  > To discriminate between them, use get_nodes method instead.\n')
#
# # /indexOf


# # valueOf
#
# print('\nLazy string representation of mscdll_1:\n\n', mscdll_1, '\n')
# print('#' * 80)
# print('\nValue of index 2 in mscdll_1 is:\n')
# print(mscdll_1.valueOf(2), '\n')
# print('#' * 80)
# print('\nValue of index -2 in mscdll_1 is:\n')
# print(mscdll_1.valueOf(-2), '\n')
#
# # /valueOf


# # iter_reverse
#
# print('\nLazy string representation of mscdll_1:\n\n', mscdll_1, '\n')
# print('#' * 80)
# print('\n  > Displaying each node in mscdll_1 in reverse:\n')
# for node in mscdll_1.iter_reverse():
#     print(node, end=', ')
# print('\n')
#
# # /iter_reverse


# # get_head
#
# print('\nLazy string representation of mscdll_1:\n\n', mscdll_1, '\n')            
# print('#' * 80)
# print('\nHead node is:')
# mscdll_1.get_head().pprint()                                        
#
# # /get_head


# # get_nodes
#
# print('\nLazy string representation of mscdll_1:\n\n', mscdll_1, '\n')
# print('#' * 80)
# print('#' * 80)
# print('\n  > Getting all nodes in mscdll_1...\n')  
# nodes = mscdll_1.get_nodes()             
# print('#' * 80)  
# print('\nAll nodes in mscdll_1 (each node in tuple: (index, node)):\n\n', nodes, '\n')
# print('#' * 80)
# print('#' * 80)
# print('\n  > Getting all nodes in mscdll_1 with values of True and {}...\n')  
# nodes = mscdll_1.get_nodes(values=[True, {}])             
# print('#' * 80)  
# print('\nNodes value True or {} in mscdll_1:\n\n', nodes, '\n')
# print('#' * 80)   
# print('#' * 80)       
# print('\n  > Getting all nodes in mscdll_1 named \'node_1\'...\n')  
# nodes = mscdll_1.get_nodes(names=['node_1'])             
# print('#' * 80)  
# print('\nNodes named \'node_1\' in mscdll_1:\n\n', nodes, '\n')
# print('#' * 80)   
# print('#' * 80)       
# print('\n  > Getting nodes in mscdll_1 at indexes 1, 3, -3 and -1...', '\n')  
# nodes = mscdll_1.get_nodes(indexes=[1, 3, -1, -3])             
# print('#' * 80)  
# print('\nNodes at indexes 1, 3, -3 and -1 in mscdll_1:\n\n', nodes, '\n')                                                  
#
# # /get_nodes

# # set_nodes_values (replace all nodes)
#
# mscdll_3.dprint()
# print()
# print('#' * 80)
# print('\n  > Setting all nodes\' values to \'replaced\'...\n')  
# mscdll_3.set_nodes_values('replaced')
# print('#' * 80)
# print()
# mscdll_3.dprint()
#
# # /set_nodes_values


# # set_nodes_values (replace certain nodes)
#
# print('\nLazy string representation of mscdll_1:\n\n', mscdll_1, '\n')
# print('#' * 80)
# print('\n  > Setting all nodes\' with value \'True\' and 1 to \'False\'...\n')  
# mscdll_1.set_nodes_values(False, values=[True, 1])
# print('#' * 80)
# print('\nLazy string representation of mscdll_1:\n\n', mscdll_1, '\n')
#
# # /set_nodes_values



# # get_name
#
# print('\nName (id) of mscdll_1 is:', mscdll_1.get_name(), '\n')                 
# print('#' * 80)    
# print('\nName (id) of mscdll_4 is:', mscdll_4.get_name(), '\n')                                                                       
#
# # /get_name


# # set_name
#
# print('\nName (id) of mscdll_1 is:', mscdll_1.get_name(), '\n')                 
# print('#' * 80)
# print('\n  > Changing name of mscdll_1 to \'renamed\'...\n')
# mscdll_1.set_name('renamed')    
# print('#' * 80)
# print('\nName (id) of mscdll_1 is:', mscdll_1.get_name(), '\n')
# print('#' * 80)
# print('\nAll nodes\' _links[mscdll_1] keys were renamed too. Showing head node as example:\n')
# mscdll_1[0].pprint()  
#
# # /set_name


# # append
#
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('Last node in mscdll_1 is:')
# mscdll_1[-1].pprint()
# print('#' * 80, '\n')
# print('  > Appending node_2 to mscdll_1...\n')
# mscdll_1.append(node_2)
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('Last node in mscdll_1 is:')
# mscdll_1[-1].pprint()
#
# # /append


# # prepend
#
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('Head node in mscdll_1 is:')
# mscdll_1[0].pprint()
# print('#' * 80, '\n')
# print('  > Prepending node_2 to mscdll_1...\n')
# mscdll_1.prepend(node_2)
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('Head node in mscdll_1 is:')
# mscdll_1[0].pprint()
#
# # /prepend


# # insert
#
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('#' * 80)
# print('#' * 80, '\n')
# print('  > Inserting node_2 at index 1 (second place)...\n')
# mscdll_1.insert(node_2, 1)                  # <--
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('#' * 80)
# print('#' * 80)
# print('\n  > Inserting value \'123\' at index -1 (before last node)...\n')
# mscdll_1.insert(123, -1)                    # <--
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('#' * 80)
# print('#' * 80)
# print('\n  > Inserting value \'LAST ONE\' at the end of the list (using \'end\' or len(mscdll_1) parameters)...\n')
# mscdll_1.insert('LAST ONE', 'end')          # <--
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('#' * 80)
# print('#' * 80)
# print('\n  > Replacing node at index 2 with value [REPLACED], naming the new node \'switched\':\n')
# mscdll_1.insert(['REPLACED'], 2, name='switched', overwrite=True)  # <--
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('#' * 80)
# print('\n\'REPLACED\' node\'s details:\n')
# mscdll_1[2].pprint()
#
# # /insert


# # replace
#
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('#' * 80)
# print('#' * 80)
# print('\n  > Replacing head node with node_2 (by position)...\n')
# mscdll_1.replace(node_2, by_position=0)            # <--
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('#' * 80)
# print('#' * 80)
# print('\n  > Replacing all nodes with value \'True\' with \'False\' (by value):\n')
# mscdll_1.replace('False', by_value=True)           # <--
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('#' * 80)
# print('#' * 80)
# print('\n  > Replacing all nodes named \'node_2\' with \'123\' (by name)...\n')
# mscdll_1.replace(123, by_name='node_2')            # <--
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('#' * 80)
# print('#' * 80)
# print('\n  > Replacing head node with node_1 (by node)...\n')
# mscdll_1.replace(node_1, by_node=mscdll_1[0])     # <--
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# mscdll_1.dprint()
#
# # /replace


# # pop
#
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('#' * 80)
# print('\n  > Popping node at index -1 (by index)...\n')
# popped_node = mscdll_1.pop(index=-1)            # <--
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('#' * 80)
# print('\n  > Printing out popped node...\n')
# popped_node.pprint()
# print('#' * 80)
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('#' * 80)
# print('\n  > Popping node named node_1 (by name)...\n')
# popped_node = mscdll_1.pop(name='node_1')       # <--
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('#' * 80)
# print('\n  > Printing out popped node:\n')
# popped_node.pprint()
#
# # /pop


# # remove
#
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('#' * 80)
# print('\n  > Removing nodes at indexes 2 and -2 (by indexes)...\n')
# removed_nodes = mscdll_1.remove(indexes=[2, -2])            # <--
# print('#' * 80)
# print('\n  > Printing out removed node tuples (target index, removed node):\n')
# print(removed_nodes)
# print()
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('#' * 80)
# print('#' * 80)
# print('\n  > Removing nodes with values \'{}\' and \'[]\' (by values)...\n')
# removed_nodes = mscdll_1.remove(values=[[], {}])            # <--
# print('#' * 80)
# print('\n  > Printing out removed node tuples (target index, removed node):\n')
# print(removed_nodes)
# print()
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('#' * 80)
# print('#' * 80)
# print('\n  > Removing nodes named \'node_1\' (by names)...\n')
# removed_nodes = mscdll_1.remove(names=['node_1'])           # <--
# print('#' * 80)
# print('\n  > Printing out removed node tuples (target index, removed node):\n')
# print(removed_nodes)
# print()
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
#
# # /remove


# # split
#
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('#' * 80)
# print('\n  > Splitting list by index 3 and naming it \'splitted\'...\n')
# splitted_list = mscdll_1.split(3, 'splitted')            # <--
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('#' * 80)
# print('\nSplitted list lazy representation:\n\n', splitted_list, '\n')
# print('#' * 80)
# print('\n Splitted list\' name:', splitted_list.get_name(), '\n')
#
# # /split

# # extend
#
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('#' * 80)
# print('\n  > Extending mscdll_1 with mscdll_2 and unlinking nodes from mscdll_2...\n')
# mscdll_1.extend(mscdll_2, True)             # <--
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('#' * 80)
# print('\nmscdll_2 lazy representation:\n\n', mscdll_2, '\n')
# print('#' * 80)
# print('#' * 80)
# print('\n  > Extending mscdll_1 with mscdll_3 without unlinking nodes from mscdll_3...\n')
# mscdll_1.extend(mscdll_3, False)            # <--
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('#' * 80)
# print('\nmscdll_3 lazy representation:\n\n', mscdll_3, '\n')
# print('#' * 80)
# print('#' * 80)
# print('\n  > Extending mscdll_1 with mscdll_4 and checking for repeated nodes...')
# print('\n      > This is supposed to rise a ValueError, since node_1 is repeated in mscdll_1 and mscdll_4\n\n')
# try:
#     mscdll_1.extend(mscdll_4, True, True)       # <--
# except ValueError:
#     print('*** If this message shows up, extend() triggered a ValueError ***'.center(80))
# print()
#
# # /extend


# # clone
#
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('#' * 80)
# print('\n  > Cloning mscdll_1 and naming it clone_list...\n')
# clone_list = mscdll_1.clone(clone_list_name='clone_list')     # <--
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('#' * 80)
# print('\nClone of mscdll_1 lazy representation:\n\n', clone_list, '\n')
# print('#' * 80)
# print('\n  > Printing out head node of mscdll_1...\n')
# mscdll_1.get_head().pprint()
# print('\n', '#' * 80)
# print('\n  > Printing out head node of cloned list...\n')
# clone_list.get_head().pprint()
# print('#' * 80)
# print('#' * 80)
# print('\n  > Cloning mscdll_1 again, this time binding the nodes\' fields...\n')
# clone_list_2 = mscdll_1.clone(bind_to_self=True)     # <--
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('#' * 80)
# print('\nClone of mscdll_1 lazy representation:\n\n', clone_list, '\n')
# print('#' * 80)
# print('\n  > Printing out head node of mscdll_1...\n')
# mscdll_1.get_head().pprint()
# print('\n', '#' * 80)
# print('\n  > Printing out head node of cloned list...\n')
# clone_list_2.get_head().pprint()
# 
# # /clone


# # reverse
#
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('#' * 80)
# print('\n  > Reversing mscdll_1...\n')
# mscdll_1.reverse()
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
#
# # /reverse


# clear
#
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('#' * 80)
# print('\n  > Clearing mscdll_1...\n')
# mscdll_1.clear()
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
#
# /clear


# is_empty
#
# print('\nmscdll_1 is empty? -', mscdll_1.is_empty(), '\n')
# print('#' * 80)
# print('\n  > Clearing mscdll_1...\n')
# mscdll_1.clear()
# print('#' * 80)
# print('\nmscdll_1 is empty? -', mscdll_1.is_empty(), '\n')
#
# /is_empty



################################################################################
########                    Observer method examples                    ########
################################################################################


# # get_name
#
# print('\nobs_1 name is:', obs_1.get_name(), '\n')
#
# # /get_name


# # set_name
#
# print('\nobs_1 name is:', obs_1.get_name(), '\n')
# print('#' * 80)
# print('\n  > Changing name of obs_1 to \'Looker\'...\n')
# obs_1.set_name('Looker')              # <--
# print('#' * 80)
# print('\nobs_1 name is:', obs_1.get_name(), '\n')
#
# # /set_name


# # get_subscribers
#
# print('\nobs_1 subscribers are:', obs_1.get_subscribers(), '\n')
#
# # /get_subscribers


# # subscribe
#
# print('\nobs_1 subscribers are:', obs_1.get_subscribers())
# print('\nmscdll_1 observer is:', mscdll_1.get_observer(), '\n')
# print('#' * 80)
# print('\n  > Subscribing smcdll_1 to obs_1...\n')
# obs_1.subscribe(mscdll_1)             # <--
# print('#' * 80)
# print('\nobs_1 subscribers are:', obs_1.get_subscribers())
# print('\nmscdll_2 observer is:', mscdll_2.get_observer()._id, '\n')
#
# # /subscribe


# # unsubscribe
#
# print('\nobs_1 subscribers are:', obs_1.get_subscribers())
# print('\nmscdll_2 observer is:', mscdll_2.get_observer()._id, '\n')
# print('#' * 80)
# print('\n  > Unsubscribing mscdll_2...\n')
# obs_1.unsubscribe(mscdll_2)           # <--
# print('#' * 80)
# print('\nobs_1 subscribers are:', obs_1.get_subscribers())
# print('\nmscdll_2 observer is:', mscdll_2.get_observer(), '\n')
#
# # /unsubscribe


# # unsubscribe_all
#
# print('\nobs_1 subscribers are:', obs_1.get_subscribers(), '\n')
# print('#' * 80)
# print('\n  > Subscribing smcdll_1 to obs_1...\n')
# obs_1.subscribe(mscdll_1)   
# print('#' * 80)
# print('\nobs_1 subscribers are:', obs_1.get_subscribers())
# print('\nmscdll_1 observer is:', mscdll_1.get_observer()._id)
# print('\nmscdll_2 observer is:', mscdll_2.get_observer()._id, '\n')
# print('#' * 80)
# print('\n  > Unsubscribing all from obs_1...\n')
# obs_1.unsubscribe_all()               # <--
# print('#' * 80)
# print('\nobs_1 subscribers are:', obs_1.get_subscribers())
# print('\nmscdll_1 observer is:', mscdll_1.get_observer())
# print('\nmscdll_2 observer is:', mscdll_1.get_observer(), '\n')
#
# # /unsubscribe_all



#################################################################################
#####   MSCDLL methods examples (subscribed to observer - linked methods)   #####
#################################################################################


# # get_observer
#
# print('\nmscdll_2 observer\'s name is:', mscdll_2.get_observer()._id)
# print('\nmscdll_2 observer\'s __str__ (and object repr) is:\n\n', mscdll_2.get_observer(), '\n')
#
# # /get_observer


# # get_observer_subscribers
#
# print('\nobs_1 subscribers are:', obs_1.get_subscribers(), '\n')
# print('#' * 80)
# print('\n  > Subscribing smcdll_1 to obs_1...\n')
# obs_1.subscribe(mscdll_1)
# print('#' * 80)
# print('\nobs_1 subscribers are:', mscdll_1.get_observer_subscribers(), '\n')
#
# # /get_observer_subscribers


# # subscribe
#
# print('\nobs_1 subscribers are:', obs_1.get_subscribers())
# print('\nmscdll_1 observer is:', mscdll_1.get_observer(), '\n')
# print('#' * 80)
# print('\n  > Subscribing smcdll_1 to obs_1...\n')
# mscdll_1.subscribe(obs_1)                             # <--
# print('#' * 80)
# print('\nobs_1 subscribers are:', obs_1.get_subscribers())
# print('\nmscdll_1 observer is:', mscdll_1.get_observer()._id, '\n')
#
# # /subscribe


# # unsubscribe
#
# print('\nobs_1 subscribers are:', obs_1.get_subscribers())
# print('\nmscdll_2 observer is:', mscdll_2.get_observer()._id, '\n')
# print('#' * 80)
# print('\n  > Unsubscribing smcdll_2 from obs_1...\n')
# mscdll_2.unsubscribe()                           # <--
# print('#' * 80)
# print('\nobs_1 subscribers are:', obs_1.get_subscribers())
# print('\nmscdll_2 observer is:', mscdll_1.get_observer(), '\n')
#
# # /unsubscribe


# # linked_get_head
#
# print('\n  > Subscribing smcdll_1 and smcdll_0 to obs_1...')
# obs_1.subscribe(mscdll_1)
# obs_1.subscribe(mscdll_0)
# print('\nobs_1 subscribers are:', obs_1.get_subscribers(), '\n')
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('\nmscdll_2 lazy representation:\n\n', mscdll_2, '\n')
# print('\nmscdll_0 lazy representation:\n\n', mscdll_0, '\n')
# print('#' * 80)
# print('\n  > Getting head node references from all lists...\n')
# head_references = mscdll_1.linked_get_head()          # <--
# print('#' * 80)
# print('\n  > Returned dictionary format: { \'SMCDLL name\': <head node referece> }\n')
# print(head_references, '\n')
#
# # /linked_get_head


# # linked_get_nodes
#
# print('\n  > Subscribing smcdll_1 and smcdll_3 to obs_1...')
# obs_1.subscribe(mscdll_1)
# obs_1.subscribe(mscdll_3)
# print('\nobs_1 subscribers are:', obs_1.get_subscribers(), '\n')
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('\nmscdll_2 lazy representation:\n\n', mscdll_2, '\n')
# print('\nmscdll_3 lazy representation:\n\n', mscdll_3, '\n')
# print('#' * 80)
# print('\n  > Getting all nodes in all lists...\n')  
# nodes = mscdll_1.linked_get_nodes()             
# print('#' * 80)  
# print('\nAll nodes in each list (each node in tuple: (index, node)):\n')
# print(' >>', mscdll_1._id, ':', nodes[mscdll_1._id], '\n')
# print(' >>', mscdll_2._id, ':', nodes[mscdll_2._id], '\n')
# print(' >>', mscdll_3._id, ':', nodes[mscdll_3._id], '\n')
# print('#' * 80)
# print('\n  > Getting all nodes in all lists with value \'True\' and \'False\'...\n')  
# nodes = mscdll_1.linked_get_nodes(values=[True, False])             
# print('#' * 80)  
# print('\nNodes in each list with value \'True\' and \'False\' (each node in tuple: (index, node)):\n')
# print(' >>', mscdll_1._id, ':', nodes[mscdll_1._id], '\n')
# print(' >>', mscdll_2._id, ':', nodes[mscdll_2._id], '\n')
# print(' >>', mscdll_3._id, ':', nodes[mscdll_3._id], '\n')
#
# # /linked_get_nodes


# # linked_set_nodes_values (changing all node's values)
#
# print('\n  > Subscribing smcdll_1 and smcdll_3 to obs_1...')
# obs_1.subscribe(mscdll_1)
# obs_1.subscribe(mscdll_3)
# print('\nobs_1 subscribers are:', obs_1.get_subscribers(), '\n')
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('\nmscdll_2 lazy representation:\n\n', mscdll_2, '\n')
# print('\nmscdll_3 lazy representation:\n\n', mscdll_3, '\n')
# print('#' * 80)
# print('\n  > Getting all nodes in all lists...\n')  
# nodes = mscdll_1.linked_get_nodes()             
# print('#' * 80)  
# print('\nAll nodes in each list (each node in tuple: (index, node)):\n')
# print(' >>', mscdll_1._id, ':', nodes[mscdll_1._id], '\n')
# print(' >>', mscdll_2._id, ':', nodes[mscdll_2._id], '\n')
# print(' >>', mscdll_3._id, ':', nodes[mscdll_3._id], '\n')
# print('#' * 80)
# print('\n  > Setting all nodes\' values to \'replaced\'...\n')  
# nodes = mscdll_1.linked_set_nodes_values('replaced')     # <--         
# print('#' * 80)  
# print('\nAll nodes in each list (each node in tuple: (index, node)):\n')
# print(' >>', mscdll_1._id, ':', nodes[mscdll_1._id], '\n')
# print(' >>', mscdll_2._id, ':', nodes[mscdll_2._id], '\n')
# print(' >>', mscdll_3._id, ':', nodes[mscdll_3._id], '\n')
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('\nmscdll_2 lazy representation:\n\n', mscdll_2, '\n')
# print('\nmscdll_3 lazy representation:\n\n', mscdll_3, '\n')
#
# # /linked_set_nodes_values


# # linked_set_nodes_values (changing some nodes' values by index)
#
# print('\n  > Subscribing smcdll_1 and smcdll_3 to obs_1...')
# obs_1.subscribe(mscdll_1)
# obs_1.subscribe(mscdll_3)
# print('\nobs_1 subscribers are:', obs_1.get_subscribers(), '\n')
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('\nmscdll_2 lazy representation:\n\n', mscdll_2, '\n')
# print('\nmscdll_3 lazy representation:\n\n', mscdll_3, '\n')
# print('#' * 80)
# print('\n  > Getting all nodes in all lists...\n')  
# nodes = mscdll_1.linked_get_nodes()             
# print('#' * 80)  
# print('\nAll nodes in each list (each node in tuple: (index, node)):\n')
# print(' >>', mscdll_1._id, ':', nodes[mscdll_1._id], '\n')
# print(' >>', mscdll_2._id, ':', nodes[mscdll_2._id], '\n')
# print(' >>', mscdll_3._id, ':', nodes[mscdll_3._id], '\n')
# print('#' * 80)
# print('\n  > Setting nodes\' values in indexes 0, 2, 4 and -1 to \'024last\'...\n')  
# nodes = mscdll_1.linked_set_nodes_values('024last', indexes=[0, 2, 4, -1])    # <--         
# print('#' * 80)  
# print('\nAll nodes in each list (each node in tuple: (index, node)):\n')
# print(' >>', mscdll_1._id, ':', nodes[mscdll_1._id], '\n')
# print(' >>', mscdll_2._id, ':', nodes[mscdll_2._id], '\n')
# print(' >>', mscdll_3._id, ':', nodes[mscdll_3._id], '\n')
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('\nmscdll_2 lazy representation:\n\n', mscdll_2, '\n')
# print('\nmscdll_3 lazy representation:\n\n', mscdll_3, '\n')
#
# # /linked_set_nodes_values


# # linked_indexOf (has the same conditions as indexOf)
#
# print('\n  > Subscribing smcdll_1 and smcdll_3 to obs_1...')
# obs_1.subscribe(mscdll_1)
# obs_1.subscribe(mscdll_3)
# print('\nobs_1 subscribers are:', obs_1.get_subscribers(), '\n')
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('\nmscdll_2 lazy representation:\n\n', mscdll_2, '\n')
# print('\nmscdll_3 lazy representation:\n\n', mscdll_3, '\n')
# print('#' * 80)
# print('\n  > Getting nodes with value \'True\' in all lists...\n')
# nodes = mscdll_1.linked_indexOf(True)          # <--
# print('#' * 80)
# print('\nAll nodes with truthy values on each list:')
# print('\n  > Returned dictionary format: { \'SMCDLL name\': (<indexes>) }\n')
# print(nodes, '\n')
#
# # /linked_indexOf


# # linked_valueOf
#
# print('\n  > Subscribing smcdll_1 and smcdll_3 to obs_1...')
# obs_1.subscribe(mscdll_1)
# obs_1.subscribe(mscdll_3)
# print('\nobs_1 subscribers are:', obs_1.get_subscribers(), '\n')
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('\nmscdll_2 lazy representation:\n\n', mscdll_2, '\n')
# print('\nmscdll_3 lazy representation:\n\n', mscdll_3, '\n')
# print('#' * 80)
# print('\n  > Getting nodes at index 5 in all lists...\n')
# nodes = mscdll_1.linked_valueOf(5)          # <--
# print('#' * 80)
# print('\nAll nodes at index 5 on each list:')
# print('\n  > Returned dictionary format: { \'SMCDLL name\': (<indexes>) }\n')
# print(nodes, '\n')
#
# # /linked_valueOf


# # linked_append
#
# print('\n  > Subscribing smcdll_1 and smcdll_3 to obs_1...')
# obs_1.subscribe(mscdll_1)
# obs_1.subscribe(mscdll_3)
# print('\nobs_1 subscribers are:', obs_1.get_subscribers(), '\n')
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('\nmscdll_2 lazy representation:\n\n', mscdll_2, '\n')
# print('\nmscdll_3 lazy representation:\n\n', mscdll_3, '\n')
# print('#' * 80)
# print('\n  > Appending value \'LAST ONE\' named \'last\' to all subscribers...\n')
# appended_nodes = mscdll_1.linked_append('LAST ONE', name='last')   # <--
# print('#' * 80)
# print('\nAppended nodes on each list:')
# print('\n    > Returned dictionary format: { \'SMCDLL name\': [<tuples>] }')
# print('    > Tuple format: (insertion index, appended node)\n')
# print(appended_nodes, '\n')
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('\nmscdll_2 lazy representation:\n\n', mscdll_2, '\n')
# print('\nmscdll_3 lazy representation:\n\n', mscdll_3, '\n')
# print('#' * 80)
# print('\n  > Printing details of last node in mscdll_1...\n')
# print('#' * 80)
# mscdll_1[-1].pprint()
#
# # /linked_append


# # linked_prepend
#
# print('\n  > Subscribing smcdll_1 and smcdll_3 to obs_1...')
# obs_1.subscribe(mscdll_1)
# obs_1.subscribe(mscdll_3)
# print('\nobs_1 subscribers are:', obs_1.get_subscribers(), '\n')
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('\nmscdll_2 lazy representation:\n\n', mscdll_2, '\n')
# print('\nmscdll_3 lazy representation:\n\n', mscdll_3, '\n')
# print('#' * 80)
# print('\n  > Prepending value \'FIRST!\' named \'first\' to all subscribers...\n')
# prepended_nodes = mscdll_1.linked_prepend('FIRST!', name='first')   # <--
# print('#' * 80)
# print('\nPrepended nodes on each list:')
# print('\n    > Returned dictionary format: { \'SMCDLL name\': [<tuples>] }')
# print('    > Tuple format: (insertion index, prepended node)\n')
# print(prepended_nodes, '\n')
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('\nmscdll_2 lazy representation:\n\n', mscdll_2, '\n')
# print('\nmscdll_3 lazy representation:\n\n', mscdll_3, '\n')
# print('#' * 80)
# print('\n  > Printing details of first (head) node in mscdll_2...\n')
# print('#' * 80)
# mscdll_2[0].pprint()
#
# # /linked_prepend


# # linked_insert (accepts the same kwargs as insert)
#
# print('\n  > Subscribing smcdll_1 and smcdll_3 to obs_1...')
# obs_1.subscribe(mscdll_1)
# obs_1.subscribe(mscdll_3)
# print('\nobs_1 subscribers are:', obs_1.get_subscribers(), '\n')
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('\nmscdll_2 lazy representation:\n\n', mscdll_2, '\n')
# print('\nmscdll_3 lazy representation:\n\n', mscdll_3, '\n')
# print('#' * 80)
# print('\n  > Inserting value [\'Before, last\'] named \'last-1\' at position -1 in all subscribers...\n')
# inserted_nodes = mscdll_1.linked_insert(['Before', 'last'], position=-1, name='last-1')  # <--
# print('#' * 80)
# print('\nInserted nodes on each list:')
# print('\n    > Returned dictionary format: { \'SMCDLL name\': [<tuples>] }')
# print('    > Tuple format: (insertion index, inserted node)\n')
# print(inserted_nodes, '\n')
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('\nmscdll_2 lazy representation:\n\n', mscdll_2, '\n')
# print('\nmscdll_3 lazy representation:\n\n', mscdll_3, '\n')
# print('#' * 80)
# print('\n  > Printing details of previous-to-last node in mscdll_3...\n')
# print('#' * 80)
# mscdll_3[-2].pprint()
#
# # /linked_insert


# # linked_replace (accepts the same kwargs as replace)
#
# print('\n  > Subscribing smcdll_1 and smcdll_3 to obs_1...')
# obs_1.subscribe(mscdll_1)
# obs_1.subscribe(mscdll_3)
# print('\nobs_1 subscribers are:', obs_1.get_subscribers(), '\n')
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('\nmscdll_2 lazy representation:\n\n', mscdll_2, '\n')
# print('\nmscdll_3 lazy representation:\n\n', mscdll_3, '\n')
# print('#' * 80)
# print('\n  > Replacing values \'True\' with \'False\' in all subscribers...\n')
# replaced_nodes = mscdll_1.linked_replace(False, by_value=True)  # <--   # <--
# print('#' * 80)
# print('\nReplaced nodes of each list:')
# print('\n    > Returned dictionary format: { \'SMCDLL name\': [<tuples>] }')
# print('    > Tuple format: (target index, replacement node, replaced node)\n')
# print(replaced_nodes)
# print('\n\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('\nmscdll_2 lazy representation:\n\n', mscdll_2, '\n')
# print('\nmscdll_3 lazy representation:\n\n', mscdll_3, '\n')
#
# # /linked_replace


# # linked_pop (accepts the same kwargs as pop)
#
# print('\n  > Subscribing smcdll_1 and smcdll_3 to obs_1...')
# obs_1.subscribe(mscdll_1)
# obs_1.subscribe(mscdll_3)
# print('\nobs_1 subscribers are:', obs_1.get_subscribers(), '\n')
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('\nmscdll_2 lazy representation:\n\n', mscdll_2, '\n')
# print('\nmscdll_3 lazy representation:\n\n', mscdll_3, '\n')
# print('#' * 80)
# print('\n  > Popping nodes at index 5 from all subscribers...\n')
# popped_nodes = mscdll_1.linked_pop(index=5)    # <--
# print('#' * 80)
# print('\nPopped nodes of each list:\n')
# print('  > Returned dictionary format: { \'SMCDLL name\': <removed node> }\n')
# print(popped_nodes)
# print('\n\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('\nmscdll_2 lazy representation:\n\n', mscdll_2, '\n')
# print('\nmscdll_3 lazy representation:\n\n', mscdll_3, '\n')
#
# # /linked_pop


# # linked_remove (accepts the same kwargs as remove)
#
# print('\n  > Subscribing smcdll_1 and smcdll_3 to obs_1...')
# obs_1.subscribe(mscdll_1)
# obs_1.subscribe(mscdll_3)
# print('\nobs_1 subscribers are:', obs_1.get_subscribers(), '\n')
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('\nmscdll_2 lazy representation:\n\n', mscdll_2, '\n')
# print('\nmscdll_3 lazy representation:\n\n', mscdll_3, '\n')
# print('#' * 80)
# print('\n  > Removing nodes indexes 0, 1, -5 and -1 from all subscribers...\n')
# removed_nodes = mscdll_1.linked_remove(indexes=[0, 1, -5, -1])    # <--
# print('#' * 80)
# print('\nRemoved nodes of each list:')
# print('\n    > Returned dictionary format: { \'SMCDLL name\': [<tuples>] }')
# print('    > Tuple format: (target index, removed node)\n')
# print(removed_nodes)
# print('\n\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('\nmscdll_2 lazy representation:\n\n', mscdll_2, '\n')
# print('\nmscdll_3 lazy representation:\n\n', mscdll_3, '\n')
#
# # /linked_remove


# # linked_split (accepts the same args as split)
#
# print('\n  > Subscribing smcdll_1 and smcdll_3 to obs_1...')
# obs_1.subscribe(mscdll_1)
# obs_1.subscribe(mscdll_3)
# print('\nobs_1 subscribers are:', obs_1.get_subscribers(), '\n')
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('\nmscdll_2 lazy representation:\n\n', mscdll_2, '\n')
# print('\nmscdll_3 lazy representation:\n\n', mscdll_3, '\n')
# print('#' * 80)
# print('\n  > Splitting all lists at index 2...\n')
# splitted_references = mscdll_1.linked_split(2)    # <--
# print('#' * 80)
# print('\nReferences to each splitted list:')
# print('\n    > Returned dictionary format: (\'SMCDLL name\': [<tuples>])')
# print('    > Tuple format: (target index, splitted list reference)\n')
# print(splitted_references)
# print('\n\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('\nmscdll_2 lazy representation:\n\n', mscdll_2, '\n')
# print('\nmscdll_3 lazy representation:\n\n', mscdll_3, '\n')
# splitted_references = [item for item in splitted_references.items()]
# print('\nSplitted mscdll_1 lazy representation:\n\n', splitted_references[0][1], '\n')
# print('\nSplitted mscdll_2 lazy representation:\n\n', splitted_references[1][1], '\n')
# print('\nSplitted mscdll_3 lazy representation:\n\n', splitted_references[2][1], '\n')
#
# # /linked_split


# # linked_extend(mode='append_self')
#
# print('\n  > Subscribing smcdll_1 and smcdll_3 to obs_1...')
# obs_1.subscribe(mscdll_1)
# obs_1.subscribe(mscdll_3)
# print('\nobs_1 subscribers are:', obs_1.get_subscribers(), '\n')
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('\nmscdll_2 lazy representation:\n\n', mscdll_2, '\n')
# print('\nmscdll_3 lazy representation:\n\n', mscdll_3, '\n')
# print('#' * 80)
# print('\n  > Extending all lists with smcdll_3 and unlinking nodes from mscdll_3...')
# print('\n    > Keep in mind all errors will fail silently.')
# print('\n    > If an exception is encountered, the program will simply ignore the current iterating list.\n')
# mscdll_3.linked_extend(True, True, mode='append_self')     # <--
# print('#' * 80)
# print('\n\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('\nmscdll_2 lazy representation:\n\n', mscdll_2, '\n')
# print('\nmscdll_3 lazy representation:\n\n', mscdll_3, '\n')
#
# # /linked_extend(mode='append_self')


# # linked_extend(mode='prepend_self')
#
# print('\n  > Subscribing smcdll_1, smcdll_3 and mscdll_4 to obs_1...')
# obs_1.subscribe(mscdll_1)
# obs_1.subscribe(mscdll_3)
# obs_1.subscribe(mscdll_4)
# print('\nobs_1 subscribers are:', obs_1.get_subscribers(), '\n')
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('\nmscdll_2 lazy representation:\n\n', mscdll_2, '\n')
# print('\nmscdll_3 lazy representation:\n\n', mscdll_3, '\n')
# print('\nmscdll_4 lazy representation:\n\n', mscdll_4, '\n')
# print('#' * 80)
# print('\n  > Extending all lists with smcdll_4 without unlinking nodes...')
# print('\n    > Keep in mind all errors will fail silently.')
# print('\n    > If an exception is encountered, the program will simply ignore the current iterating list.\n')
# mscdll_4.linked_extend(False, True, mode='prepend_self')     # <--
# print('#' * 80)
# print('\nNOTE:\n')
# print('  > mscdll_1 and mscdll_4 shares the same node_1. An exception will rise and fail silently.')
# print('  > mscdll_1 will not be extended with mscdll_4 because of this.')
# print('  > Since nodes will not be unlinked from mscdll_4, nodes will not be removed from it.')
# print('\n\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('\nmscdll_2 lazy representation:\n\n', mscdll_2, '\n')
# print('\nmscdll_3 lazy representation:\n\n', mscdll_3, '\n')
# print('\nmscdll_4 lazy representation:\n\n', mscdll_4, '\n')
#
# # /linked_extend(mode='prepend_self')


# # linked_extend(mode='fuse_all')
#
# print('\n  > Subscribing smcdll_1 and smcdll_3 to obs_1...')
# obs_1.subscribe(mscdll_1)
# obs_1.subscribe(mscdll_3)
# print('\nobs_1 subscribers are:', obs_1.get_subscribers(), '\n')
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('\nmscdll_2 lazy representation:\n\n', mscdll_2, '\n')
# print('\nmscdll_3 lazy representation:\n\n', mscdll_3, '\n')
# print('#' * 80)
# print('\n  > Fusing all lists to mscdll_1 and unlinking nodes from fused lists...')
# print('\n    > Keep in mind all errors will fail silently.')
# print('\n    > If an exception is encountered, the program will simply ignore the current iterating list.\n')
# mscdll_1.linked_extend(True, False, mode='fuse_all')     # <--
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('\nmscdll_2 lazy representation:\n\n', mscdll_2, '\n')
# print('\nmscdll_3 lazy representation:\n\n', mscdll_3, '\n')
#
# # /linked_extend(mode='fuse_all')


# # linked_clone (does not accept clone_list_id to avoid naming conflicts)
#
# print('\n  > Subscribing smcdll_1 and smcdll_3 to obs_1...')
# obs_1.subscribe(mscdll_1)
# obs_1.subscribe(mscdll_3)
# print('\nobs_1 subscribers are:', obs_1.get_subscribers(), '\n')
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('\nmscdll_2 lazy representation:\n\n', mscdll_2, '\n')
# print('\nmscdll_3 lazy representation:\n\n', mscdll_3, '\n')
# print('#' * 80)
# print('\n  > Cloning all lists...\n')
# cloned_references = mscdll_1.linked_clone()    # <--
# print('#' * 80)
# print('\nReferences to each cloned list:')
# print('\n    > Returned list format: [<cloned_lists_references>]')
# print('    > Tuple format: (target index, cloned list reference)\n')
# print(cloned_references)
# print('\n\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('\nmscdll_2 lazy representation:\n\n', mscdll_2, '\n')
# print('\nmscdll_3 lazy representation:\n\n', mscdll_3, '\n')
# for i, value in enumerate(cloned_references.values()):
#     print(f'\nCloned mscdll_{i+1} lazy representation:\n\n', value, '\n')
#
# # /linked_clone


# # linked_reverse
#
# print('\n  > Subscribing smcdll_1 and smcdll_3 to obs_1...')
# obs_1.subscribe(mscdll_1)
# obs_1.subscribe(mscdll_3)
# print('\nobs_1 subscribers are:', obs_1.get_subscribers(), '\n')
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('\nmscdll_2 lazy representation:\n\n', mscdll_2, '\n')
# print('\nmscdll_3 lazy representation:\n\n', mscdll_3, '\n')
# print('#' * 80)
# print('\n  > Reversing all lists...\n')
# mscdll_1.linked_reverse()                # <--
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('\nmscdll_2 lazy representation:\n\n', mscdll_2, '\n')
# print('\nmscdll_3 lazy representation:\n\n', mscdll_3, '\n')
#
#
# # /linked_reverse

# # linked_clear
#
# print('\n  > Subscribing smcdll_1 and smcdll_3 to obs_1...')
# obs_1.subscribe(mscdll_1)
# obs_1.subscribe(mscdll_3)
# print('\nobs_1 subscribers are:', obs_1.get_subscribers(), '\n')
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('\nmscdll_2 lazy representation:\n\n', mscdll_2, '\n')
# print('\nmscdll_3 lazy representation:\n\n', mscdll_3, '\n')
# print('#' * 80)
# print('\n  > Clearing all lists...\n')
# mscdll_1.linked_clear()                # <--
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('\nmscdll_2 lazy representation:\n\n', mscdll_2, '\n')
# print('\nmscdll_3 lazy representation:\n\n', mscdll_3, '\n')
#
# # /linked_clear


# # linked_is_empty
#
# print('\n  > Subscribing smcdll_1 and smcdll_0 to obs_1...')
# obs_1.subscribe(mscdll_1)
# obs_1.subscribe(mscdll_0)
# print('\nobs_1 subscribers are:', obs_1.get_subscribers(), '\n')
# print('#' * 80)
# print('\nmscdll_1 lazy representation:\n\n', mscdll_1, '\n')
# print('\nmscdll_2 lazy representation:\n\n', mscdll_2, '\n')
# print('\nmscdll_0 lazy representation:\n\n', mscdll_0, '\n')
# print('#' * 80)
# print('\n  > Checking if lists are empty...\n')
# empty_lists = mscdll_1.linked_is_empty()             # <--
# print('#' * 80)
# print('\n  > Returned dictionary format: { \'SMCDLL name\': True | False }\n')
# print(empty_lists, '\n')
#
# # /linked_is_empty


print('#' * 80)     

# mscdll_6 = MSCDLL(
#     111, 'asd', True, None, 1, True, {}, 2, {'a': 1}, False, True, 
#     name='',
# )

# print('node:',mscdll_6._get_node_by_idx(11))
# mscdll_6.dprint()
