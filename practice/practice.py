# a = int(input("Enter the First number :"))
# b = int(input("Enter the Second number :"))
# a,b=b,a
# print("a =", a)
# print("b =", b)
# Example 4: Write a program to swap two variables without using third variable.

# Example 4: Write a program to swap two variables with using third variable.

# a=int(input('enter the first number-'))
# b= int (input('enter the second number-'))
# temp=a
# a=b
# b=temp
# print('a>-',a)
# print('b>-',b)
# enter the first number-50
# enter the second number-20
# a>- 20
# b>- 50


# Example 6: Write a program to swap two variables using Addition and Subtraction.
# a=int(input('enter the first number-'))
# b= int (input('enter the second number-'))
# sum=a+b
# sub=a-b
# print('a>-',sum)
# print('b>-',sub)

# a = int(input("Enter the First number :"))
# b = int(input("Enter the Second number :"))
# a = a + b
# b = a - b
# a = a - b
# print("swap")
# print("a =", a)
# print("b =", b)


# Example 9: Write a program to find the square root of given no. Answer:-
# x=int(input("Enter a no."))
# print(x**(1/2))


# Example 10: Write a program to find largest no among the three input numbers.
a = float(input("Enter the First number :"))
b = float(input("Enter the Second number :"))
c = float(input("Enter the Third number :"))
if a > b and a > c:
    print(f'Largest  number is a = {a}')
elif b > c:
     print(f'Largest number is b = {b}')
else:
       print(f'Largest number is c =  {c}')
