number=int(input("enter the number:"))
for i in range(1,11):
    if i==5:                            # skiping fifth iteration
        continue
    print(f"{number}x{i}={number*i}")

 