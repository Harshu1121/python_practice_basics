age=int(input("Enter  your age:"))
def check_age(age):
    if age in range(14):
        print("Child")
    elif age in range(15,19):
        print("Teenage")
    elif age in range(19,61):
        print("Adult")
    elif age > 60 :
        print("old age")
    else:
        print("enter valid number!!!")               

check_age(age)        