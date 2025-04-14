a={12,34,62,45}
b={45,78,89,65}
a.symmetric_difference_update(b)
print(a)# we expect the output will be the symmetric difference of a and b 
# shortcut for symmetric_difference_update is^=
print(f"by using the shotcut for symmetric difference update the output is {a}")