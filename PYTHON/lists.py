#to create a list we use [] to encase what we want listed and seperate them all by commas

test_list = [2, 4, 5, 5, 7]

print(test_list[2])
#prints the item with index number 2

print(type(test_list))
print(type(test_list[2]))
print(len(test_list))


#slicing 


#to pull the first x entries in a list we use [:x]
#to pull the last y entries in a list we use [-y:]

print('first 2 entries: ', test_list[:2])
print('last 3 entries: ', test_list[-3:])
print('which entries: ', test_list[3:])#this outputs from the x entry to the last 

#to remove from a list we use the .remove() method, while putting the item you want to remove in the brackets

test_list.remove(5)
print( 	test_list)

#to add to a list we use the .append(), with what we want to add put in the parenthesis


test_list.append(7)
test_list.append(4)
print(test_list)

#to add an item to a specific spot we use the .insert(index, item) method

test_list.insert(2, 16)
print(test_list)

#to add a multiple elements to a list
new_list = [2, 3, 19, 124]

test_list.extend(new_list)
print(test_list)

test_list.extend([1,2,4,7])
print(test_list)

#testing adding multiple elements to a specific index using insert and an extra list

test_list.insert(2, [27, 49])
print(test_list)
#the above code block adds the list into the list asa whole, ie: "[27,49]" as an elemet

#to add multiple elements from a list to our list
test_list[2:2] = [47, 49, 14]
print(test_list)

#what if we spread the insert co ordinate from say, [x:x] to [x:y]

test_list[2:4] = [101, 111 ,121, 219, 322]
print(test_list)
#the above code results in no significant difference
#we can also print the minmum and maximum of lists 

#print('this is the minimum: ',min(test_list))
#print('this is the maximum: ' ,max(test_list))
#thr above won't work for the specific example because of the difference in types of lists and ints
#to sum all the ints in a list,  we use sum(list)


#samplefor the above few and more 
#assume we have a list of sales made in 10 days in usd

cloth_sales = [245, 300, 950, 110, 153, 334, 876, 999, 1102, 544]

print(min(cloth_sales))
print(max(cloth_sales))
print('total sales of 10 days: ', sum(cloth_sales))
print('total sales of first 5 days: ', sum(cloth_sales[:5]))
five_days_average = (sum(cloth_sales[:5])/5)

print('this is the average sales for first 5 days; ', five_days_average)