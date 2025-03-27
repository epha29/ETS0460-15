text="Truly, truly, I say to you, you will see heaven " 
print(text.count("you")) # we expect the output to be 2 
print(text.find("you"))# to check the index of the first occurence of the word you
#what if defined the starting and ending index 
print(text.count("you",0, 26))# we expect the output to be 1 because we are only checking the first 26 character 

