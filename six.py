a = 10
b = 5
c = 20

if a>b and c >a:
    print("And is working")

if a>b or c >a:
    print("or is working")

#####################

a = 1
while a <= 10:
    print(a)
    a +=1


a = 1
while a < 10:
    print(a)
    if a == 5:
        break
    a += 1

city = ["London", "NewYork", "Delhi"]

for mycity in city:
    print(mycity)

city = ["London", "NewYork", "Delhi"]
if "NewYork" in city:
    print("yes")
else:
    print("no")

#####################
country = ("India", "Sweden", "Finland")
for srikant in country:
    print(srikant)

country = ("India", "Sweden", "Finland")
if "India" in country:
    print("ok")

##################
