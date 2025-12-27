# Q.1(a) Write a Python program to change a given string to a newly string where the first and last chars have been exchanged. 
# Example: 
# Input:”welcome” 
# Output:”eelcomw” 

# l=input('enter a string:-')
# chars=list(l)
# chars[0],chars[-1]=chars[-1],chars[0]
# newstring="".join(chars)
# print(newstring)

# s=input('enter a string:-')
# output= s[-1]+s[1:-1]+s[0]
# print(output)

# Q.1(b) Write a Python program to count the occurrences of each word in a given sentence. 
 
# Example: 
# Input:”welcome to cybrom” 
# Output:3 

# s=input('enter a string:-')
# l=s.split()
# print(len(l))

# sentence= input('enter a string;-')
# occurences=0
# word=""
# for char in sentence +" ":
#     if char!=" ":
#         word+=char
#     else:
#         if word!="":
#             occurences+=1
#             word=""

# print(f'occurence={occurences}')



# # Add a space at the end to catch the last word
# for char in sentence + " ":
#     if char != " ":
#         current_word += char
#     else:
#         # if current_word is not empty, it means we found a word
#         if current_word != "":
#             word_count += 1
#             current_word = "" # Reset for next word

# print("Output:", word_count)


# Q.2(a) Write a Python program to check the given number is prime or not. 
# Example1 : 
# Input:7 
# Output:Prime Numbe

# num = int (input('enter a number:-'))
# for i in range(2,num):
   
#     if num%i==0:
#         print('not prime number ')
#         # ans=False
#         break

# else:
#  print('prime number')
 
# num = int (input('enter the number :-:'))
# if num>1:
#     for i in range(2,num):
#         if num%i==0:
#             print('not prime number')
#             break
#     else:
#         print('is a prime number ')
# else :
#     print ('enter valid number should greater than 2')


num=int(input('enter the number:- '))

for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
















