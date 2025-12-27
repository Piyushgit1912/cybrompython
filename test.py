# fibbonacci series
# n= int(input("enter any number:-"))
# a=0
# b=1
# i=0

# while i<n:
#     print(a,end=" ")
#     c=a+b
#     a=b
#     b=c
#     i=i+1
    
# d={}

# key=input('input key -:')
# value=input('enter value:-')

# d[key]=value

# print("dictionary is:-", d)

# d={}
# n=int(input('how many values u want to add :- '))
# i=0
# while i<n:
#     key=input('input key -:')
#     value=input('enter value:-')

#     d[key]=value
#     i+=1
# print('this is final dict :-',d)



# n=int(input("enter number:-"))
# sum=0
# i=1
# while i<=n:
#     sum=sum+i
#     i=i+1
# print(sum)

#sum of even/odd

# n=int(input("enter number:-"))
# sum=0
# for i in range(0,n+1,2):
#     sum=sum+i
# print(sum)

# def sum_odd():
#     sum = 0
#     num = 1

#     for i in range(10):
#         sum = sum + num
#         num = num + 2

#     return sum

# print("Sum of first 10 odd numbers is:", sum_odd())

# square with lambda

# n = int(input("Enter a number: "))
# square = lambda x: x*x
# print("Square is:", square(n))

# n = int(input("Enter a number: "))
# print(square := lambda x: x*x ,'\n', square(n))


# nums = [1, 2, 3, 4, 5]
# squares = list(map(lambda x: x*x, nums))
# print(squares)


# books = []   # empty list to store books

# while True:
#     print("\n--- Library Management System ---")
#     print("1. Add Book")
#     print("2. Display Books")
#     print("3. Issue Book")
#     print("4. Return Book")
#     print("5. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         book = input("Enter book name: ")
#         books.append(book)
#         print("Book added successfully")

#     elif choice == 2:
#         if len(books) == 0:
#             print("No books available")
#         else:
#             print("Available Books:")
#             for b in books:
#                 print( b)

#     elif choice == 3:
#         book = input("Enter book name to issue: ")
#         if book in books:
#             books.remove(book)
#             print("Book issued successfully")
#         else:
#             print("Book not available")

#     elif choice == 4:
#         book = input("Enter book name to return: ")
#         books.append(book)
#         print("Book returned successfully")

#     elif choice == 5:
#         print("Thank you for using Library Management System")
#         break

#     else:
#         print("Invalid choice")

# while True:
#     a = int(input("Enter first number: "))
    # b = int(input("Enter second number: "))

    # print("1. Addition")
    # print("2. Subtraction")
    # print("3. Multiplication")
    # print("4. Division")
    # print('5:- exit')

    # choice = int(input("Enter your choice (1-4): "))

    # if choice == 1:
    #     print("Result:", a + b)

    # elif choice == 2:
    #     print("Result:", a - b)

    # elif choice == 3:
    #     print("Result:", a * b)

    # elif choice == 4:
    #     if b != 0:
    #         print("Result:", a / b)
    #     else:
    #         print("Division by zero not allowed")
    # elif choice==5:
    #     break
    # else:
    #     print("Invalid choice")


