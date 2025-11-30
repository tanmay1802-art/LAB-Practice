# 2. Write a Python program to find element in setA but not in setB.
setA={1,2,3,4,5,6}
setB={3,4,6}
difference=setA-setB
print(difference)

#3. Write a Python program to convert string to set, set to list and set to tuple.
my_string = "Hello"

string_to_set = set(my_string)
print( string_to_set)


set_to_list = list(string_to_set)
print( set_to_list)


set_to_tuple = tuple(string_to_set)
print( set_to_tuple)


#4. Using set, write a Python program to count number of vowels from given strings
#Programming with Python”.


text = "Programming with Python"

vowels = {'a', 'e', 'i', 'o', 'u'}

text_lower = text.lower()

vowel_count = sum(1 for char in text_lower if char in vowels)

print( vowel_count)


#5. Write a Python program to add an item (state: Kedah) into the dictionary. Given a
#dictionary {name: “Amira”, “age”: 35}

dict={"name":"Amira","age":35}
dict["state"] = "Kedah"
print(dict)

dict={"name":"Tanmay","age":21}
dict["Area"]="BukitJalil"
print(dict)



#6. From question 5 above, write a Python program to display all items in the dictionary
#using loops.

dict = {"name": "Amira", "age": 35, "state": "Kedah"}

for key, value in dict.items():
    print(f"{key}: {value}")


#7. Given a values numbers = {145, 100, 65, 79}, write a Python program to sum all the
#values in the dictionary.

numbers={145,100,65,79}
total = sum(numbers)
print(total)


#8. Given a dictionary keys and items myData = { 1:"hello",2:22,2:22,3:"hello",3:33}, write
#a Python program to check if multiple keys exist in a dictionary.

myData =  { 1:"hello",2:22,2:22,3:"hello",3:33}

keys_to_check = [1, 2, 4]

all_exist = all(key in myData for key in keys_to_check)

if all_exist:
    print("All keys exist in the dictionary.")
else:
    print("Not all keys exist in the dictionary.")
#########


mydata={1:"hello",2:22,3:"hello",3:33}
keycheck={1,3,5}
existense=all ( key in mydata for key in keycheck)
if existense:
   print("All data exist")
else:
  print("Al data is not exist")


