my_dic={"name":"beti","age":20,"city":"adama"}
print(my_dic["name"])# we expect the output to be "beti" because the value of the key "name " is beti
print(my_dic["age"])
print(my_dic["city"])
my_dic["name"]= "ephrem" # this part is used to update the value of the key "name" in the dictionary 
my_dic["age"]=23
my_dic["city"]= "kality"
print(my_dic)
# what if we want loop through the dictionary
for key in my_dic:
    print(key) # this part is used to loop through the dicitionary and print the keys of the dictionary 
    # what if we want to print the keys and the values of the dictionary 
    print(key  , my_dic[key])
