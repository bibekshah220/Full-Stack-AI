# what is a module?
# a module is a file containing Python definitions and statements   

# how to create a module?
# create a file with a .py extension    

# how to import a module?
# import the module using the import statement    

# how to use a module?
# use the module by calling its functions and classes

# how to import specific functions from a module?
# import specific functions from a module using the from statement

# how to import all functions from a module?
# import all functions from a module using the * statement

import math
print(math.sqrt(16)) # square root of 16

from math import sqrt
print(sqrt(16)) # square root of 16

from math import *
print(sqrt(16)) # square root of 16

import math as m
print(m.sqrt(16)) # square root of 16

from math import sqrt as s
print(s(16)) # square root of 16


