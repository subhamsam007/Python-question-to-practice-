# # Python question to practice-:

# # Week 1: Basics – Variables, Data Types, Input/Output, Loops, Conditionals 


# # Q1. Write a Python program to swap two variables. 

# def swap_2(a,b):
#     temp=a
#     a=b
#     b=temp
#     return a,b

# print(swap_2(5,10))

# # Q2. Take user input and display it back to the user

# user_input_number =  int(input("Enter a number : "))
# unser_input_string= input("enter any string ")
# print(unser_input_string)
# print(user_input_number)

# # Q3. Write a program to check if a number is even or odd.

# def even_odd(num):
#     if num%2==0:
#         print("Even")
#     else:
#         print("Odd")
# print(even_odd(2))


# # Q4. Create a program that prints the multiplication table of a given number.

# def multiplication(num):
#     for i in range(1,11):
#         mul=num *i
#         print(f"{num} x {i} = {mul}")
# print(multiplication(2))

# Q5. Write a program to find the largest of three numbers. 

def largest(num1,num2,num3):
    if num1 >num2 and num1>num3:
        return num1
    elif num2 > num1 and num2> num3:
        return num2
    else :return num3

print(largest(num1=54, num2=25,num3=562))
 
#  Q6. Convert temperature from Celsius to Fahrenheit. 
def celsius_to_fahrengeit ():
    celsius = int(input("enter the celcius : "))
    fahrenheit = round((celsius*1.8) + 32 )
    return fahrenheit
print(celsius_to_fahrengeit())


#  Q7. Write a program to calculate the factorial of a number using a loop. 
# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# Example usage:
# num = int(input("Enter a number: "))
# print("Factorial of", num, "is", factorial(num))