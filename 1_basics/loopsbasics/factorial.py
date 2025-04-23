# using while loop

number=int(input("enter number:"))
fact=1

while number>0:
    fact*=number
    number-=1
print("factorial is:",fact)
