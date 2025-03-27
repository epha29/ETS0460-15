text= "Ephrem29"
print(text.isalnum())# we expect the output to be true because the string is alphanumeric
text2="effa"
print(text2.isalnum())# we expect the output to be true because the string is  alphanumeric
# what if we have a string with special characters
text3="@ effa"
print(text3.isalnum())# we expect  the output to be false because the string is not alphanumeric
#what if  we have an empty string
print("".isalnum())# we expect the output to be false because the string is empty 
# the isalnum() method returns true if all the characters in the string are alphanumeric and there is at least one character,otherwise it returns false