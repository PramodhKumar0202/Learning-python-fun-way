# So far you know how to create variables and store simple data ( var = 'Text' ). But  you'll also want to store more than a single value, that's where Collection data types.

#Collection Data-Types in Python (List | Tuple | Set | Dictionary)
#--------------------------------------------------------
# 🔹List  |         | Mutable   | Ordered   | Collection | ⭐ 90%+
# 🔹Tuple |         | Immutable | Ordered   | Collection |
# 🔹Set   | Unique  | Mutable   | Unordered | Collection |
# 🔹Dict  | Mapped  | Mutable   | Ordered*  | Collection |


# Mutable     - You can make changes
# Immutable - You can NOT make changes (it's fixed data).

empty_list = [] # or list()
my_list    = ['Wall', 'Floor', 'Roof', 'Ceiling']

print(my_list)

# get single list item 
print(my_list)
print(my_list[0])  # First Item (count starts from 0)
print(my_list[2])  # Third Item (count starts from 0)
print(my_list[-1]) # Last Item
print(my_list[-2]) # Second Last Item
print(my_list[100]) #IndexError: list index out of range

# LIST -SLICING 

# You can also use Slicing if you want to get multiple items from a list. 
# It allows you to get a chunk of data by specifying Start, End or Step positions.
# (e.g. my_list[start:stop:step]). And you don't have to specify all of them at once.

# get multiple items
my_list    = ['Wall', 'Floor', 'Roof', 'Ceiling', 'Wall', 'Floor', 'Roof', 'Ceiling']
print(my_list[:2])      # Get Until 2nd Item (excl)
print(my_list[2:])      # Get From 2nd Item (incl)
print(my_list[1:3])     # Get From First(incl) until Third (excl)
print(my_list[::2])     # Get Every 2nd item
print(my_list[2:6:2])   # Get Every 2nd Item from 2nd (incl) until 6th (excl)
print(my_list[::-1])    # Trick to Reverse List
print(my_list[:])       # Same List Copy

# example
my_list = ['Categories', 'Wall', 'Floor', 'Roof', 'Ceiling']
header  = my_list[0]
data    = my_list[1:]
print(header)
print(data)

#Replace Items
my_list    = ['Wall', 'Floor', 'Roof', 'Ceiling']
my_list[2] = 'NewItem'
my_list[-1] = 'LastItem'
my_list[1:3] = ['a','b']
print(my_list)

 #Membership Operators (Necessary for Logic)
#-------------------------
my_list = ['Wall', 'Floor', 'Roof', 'Ceiling']

print('Wall' in my_list)
print('wall' in my_list)
print('Door' not in my_list)