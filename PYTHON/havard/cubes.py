#this is simply just importing functions from a different module, in this instance a module i created earlier
from functions import cube

for i in range(10):
    print(f"the cube of {i} is {cube(i)}")

#an iindirect method would be 

import functions

for i in range(10):
    print(f'the cube of {i} is {functions.cube(i)}')
    #they output the same