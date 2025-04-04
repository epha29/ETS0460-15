                                             #  dictionaries

                                            Dictionaries in Python

A dictionary in Python is a collection of key-value pairs. Each key is unique, and it is used to access its corresponding value. Dictionaries are mutable, meaning their contents can be changed after creation                                            

# my_dic()

my_dic is a Python dictionary that stores key-value pairs. It is used to represent information about a person, such as their name, age, and city.

                         what is the syntax?
 my_dic={
    "key1": "value1"
    "key2": "value2"
    "key3": "value3"

 }
 
to update the value we use 
 
 my_dic["key"]="new value"
 
 # copy_dict().py
 
 Description

The copy() method in Python creates a shallow copy of a dictionary. This means that it copies the dictionary’s keys and values but not nested objects. If the dictionary contains mutable objects (e.g., lists, other dictionaries), only references to those objects are copied, not the actual objects themselves.
 
  what is the synta?
 new_dict = original_dict.copy()

original_dict → The dictionary to be copied.
new_dict → A new dictionary with the same key-value pairs as original_dict.
                  
 # dict.clear().py

The clear() method is used to remove all items from a dictionary, leaving it empty {}.

                     what is the syntax?
dictionary.clear()

 # dict.get()

 The get() method in Python is used to retrieve the value of a specified key from a dictionary. If the key does not exist, it returns a default value (or None if no default value is provided).
  
   what the syntax?

   dictionary.get (key, default_value )

 key: the key ehose value you want to retrieve
default_value : optional thr value to return if the key is not found.is not provided it defaults to none

 # dict.formkeys().py

 The fromkeys() method returns a dictionary with the specified keys and the specified value.
 
        what is the syntax?
        
dictionary = dict.fromkeys(keys, value)

# dict.items().py

The .items() method in Python returns a view object that displays a list of dictionary’s key-value tuples. This is useful when you want to loop through all key-value pairs in a dictionary.
 
                 what is the syntax?

  dictionary.items()

# dict.pop().py

The pop() method in Python is used to remove a specified key from a dictionary and return its corresponding value. If the key does not exist, you can provide a default value to return; otherwise, it raises a KeyError 

                what is the syntax?
        dictionary.pop()
       
# dict.popitem().py
the popitem() method in Python is used to remove and return the last key-value pair from a dictionary. This method is useful when you want to remove items in last-in, first-out (LIFO) order.
                           what is the syntax?
dictionary.popitem()


# dict.setdefault().py

     method in Python is used to retrieve the value of a specified key in a dictionary. If the key does not exist, it inserts the key with a specified default value and returns that default value

                  what the syntax?

    dictionary.setdefault(key, default_value)

 # dict.keys().py

   is a built-in Python method that returns a view object containing all the keys in a dictionary. The keys are returned as an iterable object that reflects any changes made to the dictionary.
                     what is the syntax?
   keys_view = dictionary.keys() 