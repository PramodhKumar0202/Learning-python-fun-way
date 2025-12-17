# Dictionary is a mapped ordered mutable collection. 
# It means that it stores data as key-value pairs like a real dictionary where each word (key) 
# has a meaning (value) and they are separated with a colon :
# Syntax
empty_dict   = {}                    # or dict()
dict_example = {'key1' : 'value1',
                'key2' : 'value2'}
#  Notice that dictionary also uses curly braces {} like sets. 
# This is because dictionary also can not contain duplicate keys.

d1 = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
d2 = {0:'value1', 1:'value2', 2:'value3'}

data_types = {
    "int"     : "A whole number, like 1, 2, or 3.",
    "float"   : "A number that can have a decimal point, like 2.5 or 0.1.",
    "str"     : "Words or letters, like 'hello' or 'apple'.",
    "bool"    : "True/False. Similar to Yes/No parameter in Revit.",
    "list"    : "A group of things you can change, like [1, 2, 'apple'].",
    "tuple"   : "A collection of things you can’t change, like (1, 2, 'apple').",
    "dict"    : "Pairs of things, like {'name': 'John', 'age': 10}.",
    "set"     : "A group of unique things, like {1, 2, 3}. Duplicates ignored.",
    "NoneType": "Means nothing or empty, like an empty box."
}

#Access Values
#-------------------------
print(data_types['dict'])                          # Classic getter
print(data_types['set'])                           # Classic getter
print(data_types.get('NoneType'))                  # Use Method to Get
print(data_types['Missing'])                       # KeyError: 'Missing'
print(data_types.setdefault('int', 'MyValue'))     # Use Default if Missing

# Dictionaries are mutable collection, so we can make changes. 

# To add or modify data we need to specify the key in square brackets 
# and assign a new value like this: my_dict['key'] = 'NewValue' .
# This will either create a new pair in a dict or override existing key-value.

 #Add/Modify Data
#-------------------------
data_types['int'] = 'Just a number'                # Modify Existing
data_types['complex'] = 'It is too complex...'     # New Pair

print(data_types)

 #Membership Operators (Necessary for Logic)
#-------------------------
print('list' in data_types)         # True
print('test' not in data_types)     # False 

#Dict Methods (Built-In Functionality)

#Lastly, let's jump a bit ahead of ourselves so I can mention the most used built-in methods for dictionaries. They will help you extract the right data from a dict as a list:

    # .keys() - Get List of all Keys in a dictionary

    # .values() - Get a list of all Values in a dictionary

    # .items() - Get a list of both Keys and Values as tuples.

 #   Dict Methods (Built-In Functionality)
#-------------------------
print(list(data_types.keys()))      # Get list of Keys
print(list(data_types.values()))   # Get list of Values
print(list(data_types.items()))      # Get list of Key+Value Tuples
data_types.update(dict_example)
print(data_types.pop('bool'))
