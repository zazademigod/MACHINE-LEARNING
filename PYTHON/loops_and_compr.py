#loops example with lists(for loop)

planets = ['mecury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']

for i in planets:
    if planets.index(i) < (len(planets)-1):
        print(i, end = '<>')

print('\n',planets)

#how the for loop works: its uses the "for" to specify the variable name and values to loop over 
#it uses the "in" word to link them together, the object to the right of the in can be any object that supports iteration
#in addition to lists we can loop over tuples
#Example with tuple

prime_nums = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

for x in prime_nums:
    x = x * 1
print(x)#this returns the last item in the loop as its the last iterated item 

#range() is a function that returns a sequence of numbers 

for t in range(10):
    print(t)

#WHILE LOOP
#this is quite different from for loop, this iterates until some condition is met 

i = 0
while i < 15:
    print(i, end =' ')
    i +=1 #this increases the value of i by 1 after each iteration

#while loop is evaluated as a boolean and is executed until false

#LIST COMPREHENSIONS
#essentially a shorthand for loops, easy way to understand this is by looking at some examples
#example with list comprehension
shapes = [y**2 for y in range(10)]

print('\n',shapes)

#example without list comprehension

shapes = [] #have to first declare a list
for n in range(10):
    shapes.append(n**2)
print('\n',shapes)

#list comprehension using if

upper_planets = sorted([i.upper() for i in planets if len(i) > 5])

print(upper_planets)

#list comprehensions combined with functions like min(), max(), sum() can give one line solutions to problems that would otehrwise have required multiple lines

#example of achieveing something with and without list  comprhension
#find the number of negative numbers in a list 

def count_negs(nums):
    negs = 0
    for n in nums:
        if n < 0:
            negs += 1	    
    return negs

list_of_nums = [1, -4, 3, 14, -12, -9, 0, -1, -1, -3]
no_negatives = count_negs(list_of_nums)
print(f'The number of negative numbers in the list is {no_negatives} ')

#now using list comprehensions

def count_negats(nums):

    return len([n for n in nums if n < 0])

print(count_negats(list_of_nums))
#that is shorter,  and can even be shorter

def count_negts(nums):

    return sum([n < 0 for n in nums])

#EXERCISE 

#a function to return true if there is a lucky number in a list(any number that divided by 7)

#without list comprehension
def lucky_num(nums):
    for n in nums:
        if n % 7 == 0:
            return True
    return False
#the above function operates as such, the for starts the iteration and returns true only if there is a number that fulfils the condition 
#after the iteration has been completed, if there is no number that fulfils the condition its returns the false outside the if  



