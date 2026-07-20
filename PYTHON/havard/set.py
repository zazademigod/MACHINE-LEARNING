# create aan empty set

sample = set()

# add elements to he set 

sample.add("david")
sample.add('food')
sample.add('test')
sample.add('ball')
sample.add('food')
print(sample)#this still outpuuts the same four elements as sets don't allow repititions

# to delete elements from a set
sample.remove('food')
print (sample)

# to see the length or know how many elements are in any objec 

print(f"the set sample has {len(sample)} elements")