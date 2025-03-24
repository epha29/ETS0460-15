text="i can do all things through christ"
result=text.endswith("christ")# we expect the output to be true because the text ends with christ 
print(result)
result3=text.find("can")# we expect the output to be 2 because the word can starts from the 2nd index 
print(result3)
result2=text.endswith("can",0,5) # we expect thw output to be true because the text ends with can in the identified index
print(result2)