text= "hi my Name is Ephrem"
capitalized_text=text.capitalize() # we expect that the first character will uppercase
print(f"the original text is {text} ")
print(f"the capitalizied text is {capitalized_text}")

# what about when the text start with non alphabetic character

text1= "123 hi my name is ephrem"
capitalized_text1= text1.capitalize() # we expect that no change because the the first character is not alphabetic 
print(f"the original text is {text1} ")
print(f"the capitalizied text is {capitalized_text1}")

#what about when ower text Already Capitalized
 
text2="HI MY NAME IS EPHREM "
capitalized_text2=text2.capitalize()  #we expect that the first character will be uppercase and the rest lowercase
print(f"the original text is {text2} ")
print(f"the capitalizied text is {capitalized_text2}")
