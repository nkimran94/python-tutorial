grocery_list = ["rice", "potato", "tomato","water","noodles",]
l1 = list()
print(grocery_list)
grocery_list.append("brocoli")
print(grocery_list)
print(l1)

print(grocery_list[-1])
grocery_list.sort()
print(grocery_list)

for item in grocery_list:
    if item == "potato":
        continue 
    print(item)
print("finished")