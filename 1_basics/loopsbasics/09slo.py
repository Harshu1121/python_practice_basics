# unique list
items=["apple","banna","orange","apple","mango"]

unique_item=set()

for i in items:
    if i  in unique_item:
        print("duplicate",i)
        break
    unique_item.add(i)