text= "i love maths.maths is awesome "
new_text=text.replace("maths","history") # we are replacing the word maths with history
print(new_text)
new_text=(text.replace("maths","history",1))
print(new_text)
text2="Dreams are magical. Dreams inspire us. Dreams shape our future" 
new_text2=text2.replace("Dreams","hope",2) # we must expcet the out put the first two words(Dreams) will be replaced by hope because we have given the limit as 2
print(new_text2)
