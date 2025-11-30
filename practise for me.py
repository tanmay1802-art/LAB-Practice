#2. Write a Python program to find element in setA but not in setB.
from tabnanny import check

from npractisse import total

setA={1,2,3,4,5,6}
setB={2,5,8,6}
difference=setA-setB
print(difference)

#3. Write a Python program to convert string to set, set to list and set to tuple.
string=("nice to meet you")
string_to_set=set(string)
print(string_to_set)

my_set=(string_to_set)
set_to_list=list(my_set)
print(set_to_list)

my_list=(set_to_list)
list_to_tuple=tuple(my_list)
print(list_to_tuple)

#4. Using set, write a Python program to count number of vowels from given strings
#Programming with Python”.

characters=("Programming with Python")
vowels=('a','e','i','o','u')
characters_lower=characters.lower()
vowel_count=sum(1 for a in characters.lower() if a in vowels)
print(vowel_count)


character=("Programming with Python")
vowels=('a','e','i','o','u',)
count=sum(1 for x in character if x in vowels)
print(count)



#5. Write a Python program to add an item (state: Kedah) into the dictionary. Given a
#dictionary {name: “Amira”, “age”: 35}
dict={"name":"Amira", "age":35}
dict["state"]="Kedah"
print(dict)

#6. From question 5 above, write a Python program to display all items in the dictionary
#using loops.
dict={"name":"Amira","Age":35,"State":"Kedah"}
for key,value in dict.items():
    print(f"{key}:{value}")

#7. Given a values numbers = {145, 100, 65, 79}, write a Python program to sum all the
#values in the dictionary.

values={145,100,65,79}
total=sum(values)
print(total)

#8. Given a dictionary keys and items myData = { 1:"hello",2:22,2:22,3:"hello",3:33}, write
#a Python program to check if multiple keys exist in a dictionary.

myData = { 1:"hello",2:22,2:22,3:"hello",3:33}
check=[1,2,3,4]
all_exist=all(key in myData for key in check)
if all_exist:
    print("All keys exist in the dictionary.")
else:
    print("Not all keys exist in the dictionary.")

# 8. Given a dictionary keys and items myData = { 1:"hello",2:22,2:22,3:"hello",3:33}, write
 # a Python program to check if multiple keys exist in a dictionary.
    my_data={1,2,3,4,5,6}
    keys_to_check={1,2,3,4,5,6}
    exist_list=all(key in my_data for key in keys_to_check)
    if exist_list:
        print("All keys exist in the dictionary.")
    else:
        print("Not all keys exist in the dictionary.")

#Given: tuple = (23, 45, 65, 78, 98, 9, 45, 56, 43). Write a Python program to reverse this tuple.
tuple=(23, 45, 65, 78, 98, 9, 45, 56, 43)
reversed_tuple=tuple[::-1]
print(reversed_tuple)
# Write a Python program to convert a list of characters into a string.
list=["H","E","L","L","O"]
string =''.join(list)
print(string)
# 1. Given a set {1, 2, “Hello”, “Python”}. Write a Python program to iterate over the set.
set={1, 2, "Hello", "Python"}
for item in set:
    print(set)

#You were given a tuple with elements (2, 4, 5). You want to generate a total value from the
#tuple elements. Write a Python program to unpack the tuple into several variables and display
#the total value.

tuple=(2,4,5)
a,b,c=tuple
print(a)
print(b)
print(c)
total=a+b+c
print(total)


#You were given a tuple named turtle = (1, “Hello”). Write a python program to
#a. Add on item 5 using +
#b. Add on item “single” using append ().

turtle=(1,"Hello")
turtle=turtle+(5,)
print(turtle)

temp_list=list(turtle)
temp_list_list.append("single")
turtle=tuple(temp_list)
print(turtle)

#Write a Python program to determine whether the speed limit exceeds 110 km per hour. If
#the speed exceeds 110, then fine = 300, otherwise fine = 0. Display fine.

