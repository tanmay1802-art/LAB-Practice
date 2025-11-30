
first="Tanmay"
last="Sarkar"
full=first+" "+last
print(full)

name1="ALI"
name2="maohammed"
all=f"{name1} {name2}"
print(all)

course="Programming with Python"
print(course.lower())
print(course.upper())
print(course.title())
print(course.replace("p","j"))
print(course.find("Pyt"))
print("Pro" in course)
print("Swift" not in course)


if 10=="10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")

###
for i in range(5):
    print("Attempt",(i+1),(i+1) *".")

for i in range(1,5):
    print("Attempt",i ,i * ".")


########
succesfull=True
for  i in range(3):
    print("Attempt")
    if succesfull:
        print("Successfull")
        break
else:
    print("Successful")

####nested loop
for i in range(4):
    for y in range(5):
        print(f"{i},{y}")


