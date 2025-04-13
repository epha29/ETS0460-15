# set methods of python

# set.difference()
The difference() method returns a new set that contains all the items that are present in the first set but not in the second. It’s like finding the difference between two sets.
        
        what is the syntax?

set1.difference(set2)

# set.difference_update()

Modifies the original set by removing all elements that are also present in one or more other sets/sets

The difference_update() method is different from the difference() method, because the difference() method returns a new set, without the unwanted items, and the difference_update() method removes the unwanted items from the original set.
As a shortcut, you can use the -= operator instead
             
             what is the syntax?

set.difference_update(*others)
 
 # dicard().py

The 'discard()' method attempts to remove a specified element from aset.
If the element is present in the set, it is removed. If the element is not
present, the set remains unchanged, and no error is raised.
 

                    what is the syntax?

my_set.discard(element)
 
# issuperset().py

method checks whether a set contains all the elements of another set (or iterable). It returns True if the set is a superset of the specified set, otherwise False

                   what is the syntax ?

set.issuperset(other_set)

# intersection().py
the intersection_update() method removes the items that is not present in both sets (or in all sets if the comparison is done between more than two sets).
The intersection_update() method is different from the intersection() method, because the intersection() method returns a new set, without the unwanted items, and the intersection_update() method removes the unwanted items from the original set.
As a shortcut, you can use the &= operator instead, 
# pop().py
Removes and returns an arbitrary element from the set.
Since sets are unordered, you cannot predict which element will be removed.
                    
                    what is the syntax?
         set.pop()  

# symmetric_difference().py

The symmetric_difference() method returns a set that contains all items from both set, but not the items that are present in both sets.
Meaning: The returned set contains a mix of items that are not present in both sets.
As a shortcut, you can use the ^ operator instead,

                     what is the syntax?
set.symmetric_difference(set1)
set^ set1

# issubset().py
The issubset() method returns True if all items in the set exists in the specified set, otherwise it returns False.
As a shortcut, you can use the <= operator instead, 
                    
                    what is the Syntax?

set.issubset(set1)

# union().py 
The union() method returns a set that contains all items from the original set, and all items from the specified set(s).
You can specify as many sets you want, separated by commas.
It does not have to be a set, it can be any iterable object.
If an item is present in more than one set, the result will contain only one appearance of this item.
As a shortcut, you can use the | operator instead, 

                  what is the Syntax?

set.union(set1, set2...)