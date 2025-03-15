#creating tuple using parenthesis
tuple1=(1,2,3,4,5,6,7,8,9,10)

#creating tuple using constructor
# tuple1 = tuple((1,2,3,4,5,6,7,8,9,10))

#creating tuple using list
# list1=[1,2,3,4,5,6,7,8,9,10]
# tuple1=tuple(list1)

# creating tuple using string
# tuple1=tuple("12345678910")

print("Given tuple is: ", tuple1)
print("Tuple size is: ", len(tuple1))
print("Type of tuple is: ", type(tuple1))

#accessing the elements of tuples using indexing methods
print(f"Accessing the Elements of tuple using indexing method are: {tuple1[0]},{tuple1[1]},{tuple1[2]},{tuple1[3]},{tuple1[4]},{tuple1[5]},{tuple1[6]},{tuple1[7]},{tuple1[8]},{tuple1[9]}")

#accessing the elements of tuples using negrative indexing methods
print(f"Accessing the Elements of tuple using negrative indexing method are: {tuple1[-1],tuple1[-2],tuple1[-3],tuple1[-4],tuple1[-5],tuple1[-6],tuple1[-7],tuple1[-8],tuple1[-9],tuple1[-10]}")

#accessing the elements of tuples using slicing methods
print(f"Accessing the Elements of tuple are: {tuple1[0:10]}")

#accessing the elements of tuples using for loop
print("Accessing the Elements of tuple using for in loop are:")
for i in tuple1:
    print(i)

#accessing the elements of tuples using range method
print("Accessing the Elements of tuple using range method are:")
for i in range(len(tuple1)):
    print(tuple1[i])


#accessing the elements of tuples using while loop
print("Accessing the Elements of tuple using while loop are:")
i=0
while i<len(tuple1):
    print(tuple1[i])
    i+=1


# Demonstrations of different methods of tuples
print("Demonstrations of different methods of tuples")

demoTuple=(1,2,3,4,5,6,7,8,9,10,1)
print(f"The given tuple is : {demoTuple}")

print("The type of tuple is: ", type(demoTuple))

print("The Length of tuple is: ", len(tuple1))

print("The Maximum value of tuple is: ", max(demoTuple))

print("The Minimum value of tuple is: ", min(demoTuple))

print("The Sum of tuple is: ", sum(demoTuple))

print("The Sorted form of tuple is: ", tuple(sorted(demoTuple)))

print("The reversed form of tuple is: ", tuple[::-1])

print("The list form of tuple is: ", list(demoTuple))

print("The string form of tuple is: ", str(demoTuple))

print("The tuple form of list is: ", tuple([1,2,3,4,5,6,7,8,9,10]))

print("The tuple form of string is: ", tuple("12345678910"))
print(demoTuple)

print("Counting the occurance of a specific element (1):",demoTuple.count(1))

del demoTuple
print("Tuple with name ''demoTuple' is deleted")


