#Set is an Unordered Unique Collection and it's great for getting rid of duplicates or when you need to compare 2 sets of data and quickly find the difference.
# To create a set you can use curcly braces {1,2,1} and write your data separated by commas. 
# All duplicates will be removed. If you want to create an empty set you have to use set() function because empty braces will create a dict instead of set 
# SETS (Unordered Unique Collection)
#--------------------------------------------------
empty_set = set()
set_items = {10, 20, 30, 10, 20, 'AB','BA', 'AB', True, True, False}

print(set_items)

#Convert  List/Tuple
#-------------------------
list_data        = [1,2,3,4, 1,2,3,4]     # original list
set_data         = set(list_data)         # list -> set (remove duplicates)
unique_list_data = list(set_data)         # set -> list (make it list again)

# Print Results:
print(list_data)          #> [1,2,3,4,1,2,3,4] 
print(set_data)           #> {1,2,3,4}
print(unique_list_data)   #> [1,2,3,4]

#Set Methods (Built-In Functionality)
#-------------------------
items = {10, 20, 30, 'AB', 'BA', 'AB', True, True, True}

copy_set = items.copy()     # Copy the set
removed  = items.pop()      # Remove & return a random element
items.clear()                # Remove all elements
items.remove(3)              # Remove element (error if missing)
items.discard(3)             # Remove element (no error if missing)
items.add(10)                # Add a single element