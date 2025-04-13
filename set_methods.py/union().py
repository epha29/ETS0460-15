
disciples = {"Peter", "John", "James"}
new_believers = {"Mary", "Paul", "John"}
everyone = disciples.union(new_believers)

print(everyone) # we expect the merge of the two sets
print(f"by using shourtcut{disciples / new_believers}") # this is equivalent to the above line of code
