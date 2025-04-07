my_set = {1, 2, 3, 4, 5}
print(f"Original set: {my_set}")

def discard_element(s, element):
	s.discard(element)

element_to_remove = 3
discard_element(my_set, element_to_remove)
print(f"Set after discarding {element_to_remove}: {my_set}")

element_not_present = 6
discard_element(my_set, element_not_present)
print(f"Set after discarding {element_not_present} (not present): {my_set}")