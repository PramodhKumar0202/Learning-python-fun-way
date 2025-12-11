# Tuples are basically same as lists, but immutable. 
# So it means that you can't make any changes to tuples after you made them. So, why do we need them?
#TUPLES (Immutable Ordered Collection)
#--------------------------------------------------
empty_tuple = () # or tuple()
list_data = [0,1,2,3,4,5,0,1,2,3,4,5]       # List Can Be Modified     (Mutable)
data      = (0,1,2,3,4,5,0,1,2,3,4,5)       # Tuples Can't be Modified (Immutable)
data_pts  = ((0,0,0), (1,2,3), (2,4,6))     # Nested Tuples Example

#Get Single List Item
#-------------------------
print(data[0])
print(data[2])
print(data[4])
print(data_pts[1])

#Get Multiple Items (Slice)
#-------------------------
print(data[:2]) # Get Until 2nd Item (excl)
print(data[2:]) # Get From 2nd Item (incl)
print(data[1:3]) # Get From First(incl) until Third (excl)

# You Can't Change Tuple Item!
data[0] = 'New Value'
print(data)

#Popular Functions with Tuples
#-------------------------
data      = (0,1,2,3,4,5,0,1,2,3,4,5)       # Tuples Can't be Modified (Immutable)
print(len(data))            # Get Length
print(min(data))            # Min Value
print(max(data))            # Max value
print(sum(data))            # Sum Numbers
print(sorted(data))         # Create new sorted list
print(tuple(sorted(data)))  # Convert List Into Tuple

#Tuple Methods (Built-In Functionality)
#-------------------------
data      = (0,1,2,3,4,5,0,1,2,3,4,5)
print(data.count(3))
print(data.index(3))
