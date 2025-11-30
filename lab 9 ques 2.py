#You were given a tuple named turtle = (1, “Hello”). Write a python program to
#a. Add on item 5 using +
#b. Add on item “single” using append ().

turtle=(1,"Hello")
turtle = turtle + (5,)
print(turtle)


turtle_list = list(turtle)
turtle_list.append("single")
turtle = tuple(turtle_list)
print(turtle)


