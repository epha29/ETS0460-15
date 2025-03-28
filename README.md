# section-A

 # string method()
 
   # strip() 
 this docementation is about srip() 
 The strip() method is a built-in string method in Python used to remove leading and trailing characters (whitespace by default) from a string. It is commonly used to clean up strings by removing unwanted spaces or specific characters from the beginning and end.
  
  #what is the syntax
 
      string.strip([chars])
A string specifying the set of characters to remove from the beginning and end of the string. If not provided or set to None, the strip() method removes whitespace by default (spaces, tabs, and newlines).

Their are also related methods like
strip()  is used to remove both leading and trailing charcter or space 
lstrip()  is used to remove only leading charcter or space 
rstrip()  is used to remove only and trailing charcter or space 

# capitalize() 
The capitalize() method returns a string where the first character is upper case, and the rest is lower case.
 It does not modify numbers, symbols, or already uppercase letters.

what is the syntax
 
      string.capitalize()

 # replace()
 
The replace() method is used to replace occurrences of a substring within a string with another substring. It returns a new string with the replacements.

what is the syntax?

string.replace(old, new, count)

old: The substring you want to replace.
new: The substring you want to replace it with.
count (optional): The maximum number of replacements to perform. If not specified, all occurrences of old are replaced.

# append()
The append() method in Python is used to add a single element to the end of a list. It modifies the original list in place, meaning it does not create a new list but instead updates the existing one.
  
  what is the syntax?
 list.append(element)
 
 list: The list to which you want to add an element.
element: The item to add to the list. This can be of any data type like ( ephrem, getahun , bontu)

 # srartswith()
  The startswith() method in Python is used to check if a string starts with a specific substring. It returns True if the string starts with the given substring and False otherwise.

 what is the syntax?

       string.startswith(substring,satrt,end)

substring- (Required) The string to check at the beginning.
start-(Optional) The index where the check should begin.
end-(Optional) The index where the check should stop.

result values are 

true- if the string is starting with a given substring 
fase- if not starting with agiven substring 

# endswith()
The endswith() method in Python is used to check whether a string ends with a specific substring. It returns True if the string ends with the given substring and False otherwise.
    
what is the syntax?

        string.endswith(substring, start, end)
  
 substring - string to check at the end
 start-(optional) the index where checking should begin
 end-(optional) the where the cheking should stop
 
 result values are
 
 true-if the string is end with a given substring
 false-if not ends with a given substring

# join()
  is a string method that concatenates (joins) elements of an iterable (such as a list, tuple, or set) into a single string. The joining process inserts the original string (on which `join()` is called) between each element of the iterable.
     what is the syntax?
    
    separator.join(iterable)

separator: The string used to join the elements (e.g., " ", ",", "-").

iterable: A sequence of strings (list, tuple, or any iterable containing strings).

# format()
 
 is a powerful string formatting technique in Python that allows you to insert values into a string template using placeholders.
         what is the syntax?
 
 string with {} placeholders".format(values)

# isalpha()
    method in Python is a string method that checks whether a given string consists only of alphabetic characters (A-Z, a-z). It returns `True` if all characters are letters and `False` otherwise.

                 what is the Syntax?
                 
              string.isalpha()
Return Value:

- Returns `True` if all characters in the string are alphabetic.
- Returns `False` if the string contains any non-alphabetic characters, including digits, spaces, or special symbols.

# encode()
method in Python converts a string into a bytes object using a specified encoding (default is UTF-8)
 
 what is the  syntax?
  
  string.encode()
   
   # count()

   The `count()` method in Python returns the number of occurrences of a substring within a given string.

                what is the Syntax?

    string.count(substring, start, end)

- `substring` (required): The string to search for.
- `start` (optional): The starting index where the search begins.
- `end` (optional): The ending index where the search stops.
# isalnum()
The `isalnum()` method in Python checks whether all characters in a string are **alphanumeric** (i.e., only letters and digits). It returns `True` if the string contains only letters (a-z, A-Z) and/or digits (0-9) and has at least one character; otherwise, it returns `False`

             what is the Syntax?
   
    string.isalnum()

- Returns `True` if all characters are letters and/or digits.
- Returns `False` if the string contains **spaces, symbols, or special characters**.
  
  
  # isdidgit()
  method is a built-in string method in Python that checks if all characters in a string are digits (0-9).
                            
                             what is the syntax?
       string.isdigit()