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

#Set Methods: Compare Sets
#-------------------------
a = {1,2,3,4}
b = {3,4,5,6}

print(a.union(b))                # Join 2 Sets
print(a.intersection(b))         # Find Items in BOTH sets
print(a.difference(b))           # Set A items that are missing in set B
print(a.symmetric_difference(b)) # Symmetric difference between 2 sets
print(a.issubset(b))             # Is set a completely inside set b?
print(a.issuperset(b))           # Does set_a contain all from set_B?

#Popular Functions with Lists
#-------------------------
set_nums = {10, 30, 20, 50, 40 , 10, 20}

print(len(set_nums ))     # Get Length             > 5
print(sorted(set_nums ))  # Create new sorted list > [10,20,30,40,50]
print(sum(set_nums ))     # Sum Numbers            > 150
print(min(set_nums ))     # Get Min Value          > 10
print(max(set_nums ))     # Get Max Value          > 50