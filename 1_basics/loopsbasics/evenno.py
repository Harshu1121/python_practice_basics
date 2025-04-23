import math
n = int(input("enter the number:"))

sum_even=[]
for i in range(1,n+1):
    if i%2==0:
        sum_even.append(i)
        

print("the sum of even is",sum(sum_even))