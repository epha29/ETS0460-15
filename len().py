#description: len() function is used to get the length of the string 
text="effa29"
print(len(text))# we expect the output to be 6 because the length of the string is 6
# what if we have a space in the string 
text2="effa 29"
print(len(text2))# we expect the output to be 7 becaise the length of the string is 7
# what if we have a special character in the string
text3="effa@29"
print(len(text3))# we expect the output to be 7 because the length of the string is 7
# what if we have an empty string 
print(len(""))# we expect the output to be 0 becuase the length of the string is 0
