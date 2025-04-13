
fruits = {'apple', 'banana', 'orange'}
basket = {'apple', 'banana', 'orange', 'grape', 'kiwi'}
result = fruits.issubset(basket)

print(result)  # we expect True because all firuts are in the basket
# shortcut for issubset is <=
print(fruits <= basket)  # Alternative syntax, same result