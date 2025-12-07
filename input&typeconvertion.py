num_a = input("Enter First Number: ")
num_b = input("Enter Second Number: ")

total = num_a + num_b
print(total)

#The type()  function takes any object in your code as an argument, and it returns the class of that object. 

num_a = "10"
num_b = 20
list_nums = ["10", 20]

# 🔎Check Types
print(type(num_a))
print(type(num_b))
print(type(list_nums))

# So, we know that we get strings from the input() function. But we need to convert it into integer or float  to do some math.
#     str() – Create an empty string "" or convert a value into a string

#     int() – Create 0 or convert a value into an integer 

#     float() – Create 0.0 or convert a value into a floating-point number

#     bool() – Create False or convert a value into True/False

#     list() – Create [] or convert an iterable into a list

#     tuple() – Create () or convert an iterable into a tuple

#     set() – Create empty set or convert an iterable into a set (unique elements)

#     dict() – Create empty dict or convert a mapping/sequence of pairs into a dictionary

str_num_a = input("Enter First Number: ")
str_num_b = input("Enter Second Number: ")

# 🔁Convert String to Int
num_a = int(str_num_a)
num_b = int(str_num_b)

# 🧮Calculate Total
total = num_a + num_b
print(total)

str_num_a = input("Enter First Number: ")
str_num_b = input("Enter Second Number: ")

# 🔁Convert String to Int
num_a = float(str_num_a)
num_b = float(str_num_b)

# 🧮Calculate Total
total = num_a + num_b
print(total)

# Numbers
x          = 10
str_x      = str(x)       # Convert integer to string: '10'
float_x    = float(x)     # Convert integer to float: 10.0
bool_x     = bool(x)      # Convert integer to boolean: True (non-zero is True)
bool_neg_x = bool(0)      # Convert 0 to boolean: False

# Strings
s          = "123"
int_s      = int(s)       # Convert string to integer: 123
float_s    = float(s)     # Convert string to float: 123.0
bool_s     = bool(s)      # Convert  string to boolean: True (if not empty)
bool_empty = bool("")     # Convert empty string to boolean: False

# Booleans
bool_true  = bool(1)       # True
bool_false = bool(0)      # False
bool_list  = bool([])      # Convert empty list to boolean: False
bool_dict  = bool({})      # Convert empty dict to boolean: False
bool_str   = bool("Hello")  # Convert non-empty string to boolean: True


