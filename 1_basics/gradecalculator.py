score=int(input("Enter your grade:"))
if score>=101:
    print("check the marks again")
    exit()
if score >=90:
    grade="A"
elif score>=80:
    grade="B"
elif score>=70:
    grade="C"
elif score>=60:
    grade="D"
else:
    grade="F"
print("grade:",grade)                    