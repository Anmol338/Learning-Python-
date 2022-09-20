import sys
import ctypes

# from sys import getsizeof
# var1 = 100
# print(getsizeof(var1))

var1 = 100
print(sys.getsizeof(var1))      # Size occupied by var1
var2 = id(var1)                 # Address of var1
print(var2)

##print(library.function(variable,casting).value extract)
print(ctypes.cast(var2, ctypes.py_object).value) # Finding the value of address
