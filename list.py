my_list = ['Wall', 'Floor', 'Roof', 'Ceiling', 'Floor']

print(my_list[:2])
print(my_list[2:])
print(my_list[1:2])

# Popular Functions with Lists
#-------------------------
my_list = ['Wall', 'Floor', 'Roof', 'Ceiling']
numbers = [10, 30, 20, 50, 40 ]
print(len(my_list))     # Get Length             >(5)
print(sorted(my_list))  # Create new sorted list 
print(sum(numbers))     # Sum Numbers            >(150)
print(min(numbers))     # Get Min Value          >(10)
print(max(numbers))     # Get Max Value          >(50)

my_list = ['Wall', 'Floor', 'Roof', 'Ceiling', 'Floor']
my_list2 = ['Door', 'Window']

#List Methods (Built-In Functionality)
#-------------------------
my_list.append('Door')        # Add Single Item
my_list.extend(my_list2)      # Join 2 Lists
my_list += my_list2           # Join 2 Lists
my_list.sort()                # Sort List Alphanumerically
print(my_list.count('Door'))  # Count value inside list
print(my_list.index('Roof'))  # Find index of value
my_list.insert(2,'Sofa')      # Insert Item at certain Index
my_list.remove('Floor')       # Remove Value from List (if possible)
item = my_list.pop(2)         # Remove and Return Value at given Index (last by default)
my_list.reverse()             # Reverse List Order
my_list.clear()               # Clear all items from list
y = my_list.copy()            # Create independant copy of a list!

#Nested Lists
#-------------------------
points = [
    [0,0,0],
    [2,2,0],
    [4,4,0],
    [6,6,0],
]

#🔎 Read Data
#-------------------------
pt2 = points[1]
print(points[1][2])
print(pt2[0], pt2[1], pt2[2])

