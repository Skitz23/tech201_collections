# Lists

# Lists == Arrays

# heres's out first list
shopping_list = ["milk", "Eggs", "Bread", "fruit", "cheese" ]

print(type(shopping_list)) #<class 'list'>
print(shopping_list)

print(shopping_list[0]) # Milk
print(shopping_list[3]) # Fruit
print(shopping_list[-1]) # cheese

# rewriting a value in our list
shopping_list[0] = "sugar"
print(shopping_list[0])
print(shopping_list)

# List methods

# add to a List
shopping_list.append("vegtables")
# print(shopping_list)
# print(shopping_list[5])
# print(len(shopping_list))

# remove from a list

shopping_list.remove("bread")
print(len(shopping_list))
print(shopping_list)

# remoce last item of the list, without specifying iy

shopping_list.pop()
print(shopping_list)

# Tuples

# Exactly the same as lists, except they are immutable
# Tuples are useful for elements you want ensure some data stays the same

essentials = ("bread", "eggs", "milk")

print(essentials)
print(essentials.count("bread"))

# essentials[0] = "beans" # will not work with Tuples

