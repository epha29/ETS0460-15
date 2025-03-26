text=" hi this is a test text to encode"
text.encode()
print(text.encode())# we expect the output to be the encoded text 
# what if we want to get the first text before encode. we can use the decode method
print(text.encode().decode())# we expcet the output to be the text before encoding 
