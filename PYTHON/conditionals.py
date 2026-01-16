print("hello, World!")

#sample for reference

def add_five(top_up):
    top_up = top_up + 5
    return top_up

#test for the function

new_no = add_five(7)
print(new_no)


#first conditional function

def add_8_or_4(sum_no):
    if (sum_no < 5):
        sum_no += 8
    elif(sum_no == 5):
        sum_no += 5
    else:
        sum_no += 4
    return sum_no

new_num = add_8_or_4(11)
print(new_num)

new_num2 = add_8_or_4(6)
print(new_num2)

new_num2 = add_8_or_4(5)
print(new_num2)

#for comparison and assignment using =
set_var = 2
set_var == 1 #this checks if the value of set_var is equal to 1
set_var2 = 1 #this assigns teh value of setvar2 to 1




#a function to test the grade of students from a to f

def get_grade(score):
    if score < 60:
        grade = '"F"'
    elif score < 70:
        grade = '"D"'
    elif score < 80:
        grade = '"C"'
    elif score < 90:
        grade = '"B"'
    else:
        grade = '"A"'
    return grade

stu_mark = get_grade(89)
print(stu_mark)