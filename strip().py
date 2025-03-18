#used for remove unwanted spaces from a text
text = "                                       python is the simplest machine language"
stripped_text = text.strip()    # to remove leading and trailing spaces in the above text
print(f"The original is = {text}")           # The output will show the original text with spaces
print(f"The stripped text is = {stripped_text}")    # # The output will show the text without space

#remove unwanted text from a text
text2= "zyxhello students" 
stripped_text2 =text2.strip("zyx")
print(f" the origninal text is ={text2}") #The output will show the original text with zyx that we donot want 
print (f" the stripped text is = {stripped_text2}") # The output will show the text without zyx 

#remove unwanted symbol from a text
text3 ="******** how was your day beti************"
stripped_text3 =text3.strip("*")
print(f" The original text is = {text3}") #The output will show the original text with ** that we donot want 
print (f"the stripped text is ={stripped_text3}")# The output will show the text without zyx 

text4 =" hellow world            "
stripped_text4 = text4.rstrip()
print(f" The original text is ={text4}") 
print (f"the stripped text is ={stripped_text4}")

text5= "        hellow world "
stripped_text5=text5.lstrip()
print(f"The orignal text is ={text5}")
print(f"the stripped text is ={stripped_text5} ")