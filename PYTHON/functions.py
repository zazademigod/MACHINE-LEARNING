#the head that defines the function "test_input" is the name of the function 
#input_var is the name of the variables we would be using to access the body of the function

def test_input(input_var):
    output_var = input_var * 2
    return output_var

#this is for calling the function we defined above, we simply equate the name of the new variable to the called function name and the value in parenthesis
new_sample = test_input(19)

print(new_sample)

#to try for a function that takes responses then implements the function

#def take_res(input_var1):
#    accept = input_var1 * 4 + 1
#    return accept


#to test we call the newly created function

#new_samp = take_res(input())
#print (new_samp)

#a new example using func to calculate the amount of a staff takehome after a 22% tax from a pay of 24usd per hour whilw working an unknown number of hours per week

def tax_cut(hours_work):

#amount of money before the tax deduction
    pre_tax = hours_work * 24

#amount of money after tax deductions
    after_tax = pre_tax * (.78)
    after_tax = print('amount of money after tax deductions: ', int(after_tax))
    return after_tax
    

#calling the function with the hours worked being 40 hours
salary = tax_cut(40)
print (salary)

#now to do the same thing but with just arguments 

def take_home(wage_per, num_hours2, tax_percent):

#for the total pay without tax deductions
    pre_tax = wage_per * num_hours2

#amount to be paid as tax
    tax_amt = pre_tax * tax_percent

#for the total after tax has been deducted
    post_tax = pre_tax * (1 -tax_percent)

    total_paid = print("Amount before tax: ", pre_tax, '\n' "Tax to be paid: ", tax_amt, '\n' "Balance after tax: ", post_tax )
    return total_paid


#calling the take_home function

salary2 = take_home(22, 40, .20)
print (salary2)
    