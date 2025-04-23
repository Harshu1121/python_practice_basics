# find the first non repeted char
str=input("enter string:")

for char in str:
    print(char)
    if str.count(char)==1:
        print("char is:",char)
        break
    