# Esto es una función
def lower_number(num1,num2):

    if num1<=num2:
        lowest=num1        
    else:
        lowest=num2
    return lowest

first_num = int(input("enter the first number:"))
second_num = int(input("enter the second number:"))
print("the lowest is " + str(lower_number(first_num,second_num)))