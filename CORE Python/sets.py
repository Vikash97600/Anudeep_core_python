#creating a set using curly braces
set1={1,2,3,4,5}
print("set1 is:",set1)

#creating a set using constructor
# set1 = set((1,2,3,4,5,6,7,8,9,10,1,2))
# print("set1 is:",set1)

#creating a set using list
# list1=[1,2,3,4,5,6,7,8,9,10]
# set1=set(list1)
# print("set1 is:",set1)

#creating a set using string
# set1=set("pythonprogramming")
# print("set1 is:",set1)

#creating a set using tuple
# tuple1=(1,2,3,4,5,6,7,8,9,10)
# set1=set(tuple1)
# print("set1 is:",set1)

#creating a set using range
# set1=set(range(1,11))
# print("set1 is:",set1)

#creating a set using dictionary
# dict1={1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10}
# set1=set(dict1)
# print("set1 is:",set1)

#creating empty set using curly parenthesis
# set1={}
# print("set1 is:",set1)

#creating an empty set using constructor
# set1=set()
# print("set1 is:",set1)

#creating an empty set using list
# list1=[]
# set1=set(list1)
# print("set1 is:",set1)



#accessing the elements of sets using for loop
# set1={1,2,3,4,5,6,7,8,9,10}
# for i in set1:
#     print(i)


print("Length of the set1 is :",len(set1))

print("Type of the set1 is :",type(set1))

set2={6,7,8,9,2,3}
set2.add(10)
print("After Adding the element into the set2:",set2)

set2.remove(10)      #if we are removing the element that is not present in set, it will  give any error
print("After Removing the 10 from set2 :",set2)

set3=set2
print("set3 is the copy of set2",set3)

set2.discard(10)  #if we are removing the element that is not present in set, it will not give any error
print(set2)

set2.pop()
print("After Removing the random elemnt from set2 :",set2)

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

unionSet=set1.union(set2) or set1|set2
print("Union of set1 and set2 is (set1|set2):",unionSet)

interscetionResult=set1.intersection(set2) or set&set2
print("Elements common to both set1 and set2  are (set1$set2):",interscetionResult)

differenceResult=set1.difference(set2) or set1-set2    
print("Elements in set1 but not in set2 are (set1-set2):",differenceResult)

symmDiffResult=set1.symmetric_difference(set2) or set1^set2
print("Elements in set1 or set2 but not in both are (set1^set2):",symmDiffResult)

subsetResult=set1.issubset(set2) or set1<=set2
print("set1 is subset of set2 (set1<=set2):",subsetResult)

supersetResult=set1.issuperset(set2) or set1>=set2
print("set1 is superset of set2 (set1>=set2):",supersetResult)

properSubsetResult=set1<set2
print("set1 is proper subset of set2 (set1<set2):",properSubsetResult)

frozenSet=frozenset(set1)
print("Frozen set of set1 is :",frozenSet)


