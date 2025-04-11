# genesis 7: 2, GOD tells Noah to take clean animals in pairs of seven and unclean animales in pairs of two
all_animals={ "sheep","cow","Pig","lion","goat"}
unclean={"Pig"}
x=all_animals.difference_update(unclean);
print(all_animals)# we expect the output to be set of all_animals except the unclean animals
all_animals-=unclean # this is equivalent to the above line of code
