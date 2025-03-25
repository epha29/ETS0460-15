text="Nature is a beautiful gift to us."
text2="the trees,rivers, and mountains fill the world with life and peace"
print(f"the original text is {text}and {text2}")
result=" ".join([text,text2])# we expect the output to be the two text combined
print(result)
words=("machine","puzzle","creates","an endless","echo")  
print(f"the original words are {words}")# we expect the output to be the original wods
result2=" ".join(words)# we expect the output to be the words combined 
print(result2)
result3=" , ".join(words)# we expect the output to be combined but separated by comma
print(result3)
