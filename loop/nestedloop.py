n=int(input("enter any num:-"))
y=1
# for x in range (1,n+1):
#     for i in range (1, x+1):
#         print(y, end=" ")
#     print()

#     enter any num:-4
# 1 
# 1 1
# 1 1 1
# 1 1 1 1

for x in range (1,n+1):
    for i in range (1, x+1):
        print(y, end=" ")
        y=y+2
    print()
# enter any num:-3
# 1 
# 1 2
# 1 2 3
# PS C:\Users\hp\Desktop\loop>