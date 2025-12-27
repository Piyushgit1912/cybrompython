# f= open('n1.txt','x')
# it will create a file in the folder and open
# #  File exists: 'n1.txt'
# f=open('n3.txt','w')
# print(f.name)
# print(f.mode)
# print(f.readable())
# print(f.writable())
# print(f.encoding)
# print(f.closed)

# existing file pe x mode kam nhi karega (same file cn not created ) 

# f=open('ns.text','a')
# print(f.name)
# print(f.mode)
# print(f.readable())
# print(f.writable())
# print(f.encoding)
# print(f.closed)

# f=open('n6.txt', 'a+')
# data='from python class ' 
# f.write(data)                   # single string ko e file pe likhne ke liye use karte h 
# f.close()

# f=open('n6.txt', 'a+')
# data=['\n','python\n','java\n','phph\n'] 
# f.writelines(data)                   # single string ko e file pe likhne ke liye use karte h 

# read() --> read all data
#     read(n) --> read n bitss of data 
#     readline() --> single line data 
#     readlines() --> read all lines of data 

# f=open('n6.txt')
# f=open('n6.txt','r+')
# data = f.read()
# print(data)
# f.close()

# f=open('n6.txt')
# f=open('n6.txt','r+')
# data = f.read(10)
# print(data)
# data = f.read(5)
# print(data)
# f.close()
# # this is da
# ta to
# this is da    space is also a character 

# f=open('n6.txt','r+')
# data = f.readline()
# print(data)
# f.close()
# this is data to n 6 this is data to n 6    >> one line will read 

f=open('n6.txt','r+')
data = f.readlines()
print(data)
f.close()