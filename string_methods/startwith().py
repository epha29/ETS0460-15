text="Nature is a beautiful gift to us. The trees, rivers, and mountains fill the world with life and peace. Let’s protect and cherish it for future generations"
result = text.startswith("Nature") # we expace the output to be true because the text starts with Nature
print(result)
text2=("hello everyone my name is ephrem getahun and i am electromechanical engineer")
result2=text2.startswith("Hello") # we expect the output to be false because python is case sensitive 
print(result2)
result2=text2.find("name")# we expcet the output to be 18 because the word name starts from the 18th index
print(result2)
 #what if we want to check starting from a specific index 
result3=text2.startswith("name",18)#  we expect the output to be true because the text start with name in the identified index
print(result3)