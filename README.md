# section-A
# strip() string method
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