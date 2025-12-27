x= 10
print(type(x))
s= 'python is easy'
#print(s, type(s),len(s), max(s))
# print(), min(), max(), len()id(), sum(), input(),these are some built in functions in python does apply on strings
#print(id(s),max(s),len(s),min(s))
#sum() wll not supported in strings case
# if we print s.(or any str variable name followed by .) many inbuilt methods will shown in suggestion list who starts and ends in with underscore are called magic methods and dinder methods
# lower(),
#  upper(),
#  title(), sentence ke har starter word ko capital kar dega
# capatilize(),
#  index(), 
# count(),    word repeatation  ko count karta hai  
#  split(),
#  join(),
#  find(),          will find the index of any substring 
#  replace(),
#  swapcase(), will change the case of each character in string
print(s.swapcase())
print(s.capitalize() , s.lower(), s.title(), s.upper())
y="rubber"
print(y.swapcase(), y) # original string will not change because strings are immutable  # alag print hoga quki immutable hai aur alag alag id se pstore hoga
print(s.find('Y'))                  
print(y.count('b'))

      
