# set methods of python

# set.difference()
The difference() method returns a new set that contains all the items that are present in the first set but not in the second. It’s like finding the difference between two sets.
        
        what is the syntax?

set1.difference(set2)

# set.difference_update()

Modifies the original set by removing all elements that are also present in one or more other sets/sets

The difference_update() method is different from the difference() method, because the difference() method returns a new set, without the unwanted items, and the difference_update() method removes the unwanted items from the original set.
             
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