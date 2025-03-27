text= "ephrem"
print(f"is aplhabetic:{text.isalpha()}")# we expect true because all the characters are alphabetic
# what if we hve a space in the string 
text2= "ephrem getahun"
print(f"is alphabetic:{text2.isalpha()}")# we expect false because there is a space in the string
# what if we have a number in the string 
text3="ephrem29"
print(text3.isalpha())# we expect false because there is a number in the string 
