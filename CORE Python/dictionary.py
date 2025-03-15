
#  # create dictionary 
# # employee={                                 
# #     "emp1":111,
# #     "empName":"John",
# #     "empSalary":10000
# # }

# #dictionary by constructor
# # firstDictionary=dict(empname="John",empId=111,salary=10000)

# num={1:11,2:22,3:33,4:44,5:55,6:66,7:77,8:88,9:99,10:100}
# print("Key  values")
# for key,value in num.items():
#     print(key,' : ',value)


# print("Print Keys only")
# for key in num.keys():
#     print(key)


# print("Values only")
# for value in num.values():
#     print(value)

# print("Update dictionary")
# (num.update({1:111}))
# print(num)

# print("Delete a key value from dictionary")
# del num[1]

# print("Length of dictionary")
# print(len(num))

# print("Clear dictionary")
# num.clear()
# print(num)


# newDictionary={1:11,2:22,3:33,4:44,5:55,6:66,7:77,8:88,9:99,10:100}
# print("Copy dictionary")
# secondNewDictionary=newDictionary.copy()
# print(secondNewDictionary)

# print("Convert thr dictionary to string")
# print(str(secondNewDictionary))

# print("Convert the dictionary to list")
# print(list(secondNewDictionary))

# print("Convert the dictionary to tuple")
# print(tuple(secondNewDictionary))

# print("Convert the dictionary to set")
# print(set(secondNewDictionary))

# print("remove the element from dictionary")
# secondNewDictionary.pop(2)
# print(secondNewDictionary)

# print("Remove the last element from dictionary")
# secondNewDictionary.popitem()
# print(secondNewDictionary)



# print("Python program to merge three dictionaries into a one dictionary")

# first = {1:11, 2: 88}
# second = {3:66, 4: 89}
# third = {5:90, 6:33}
# fourth= {}

# for member in (first,second,third): 
#    fourth.update(member)
# print(fourth)



#python program to print the average of values in a dictionary
# test = {"A":6, "B":9, "C":5, "D":7, "E": 4}           # dictionary
# sum=0

# for val in test.values():                             # adding values by for loop
#     sum+=val
# res = sum/len(test)                                  # res divided by length
# print("final mean/average : ", str(res))


#python program to empty the dictionary using del() function and loop
new_dict = {5: 67,6:55,7: None,8:33,9:None,1:87,2:None,3:9,4:90,5:44}
print(new_dict)

for key, value in list(new_dict.items()):
    del new_dict[key]

print("Empty dictionary",new_dict)
