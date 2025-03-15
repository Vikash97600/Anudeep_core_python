# 1) WAP to find the gratest number out of 4 numbers

# num1=int(input("Enter the value of num1:"))
# num2=int(input("Enter the value of num2:"))
# num3=int(input("Enter the value of num3:"))
# num4=int(input("Enter the value of num3:"))
# if(num1>num2) and (num1>num3) and (num1>num4):
#     greatestNum=num1
# elif(num2>num1) and (num2>num3) and (num2>num4):
#     greatestNum=num2
# elif(num3>num1) and (num3>num2) and (num3>num4):
#     greatestNum=num3
# else:
#     greatestNum=num4
# print("The greatest number is ",greatestNum)





# 2) Python program to count the occurance of each characters from the string 

# inputStr=input("Enter the string:")
# result=dict()
# for i in inputStr:
#     if i not in result:
#         result[i]=1
# for j in result:
#     count=0
#     for k in inputStr:
#         if j==k:
#             count+=1
#     print(f"The character {j} is repeated {count} times")

#     OR

# inputStr=input("Enter the string:")
# result=dict()
# for i in inputStr:
#     if i not in result:
#         result[i]=1
#     else:
#         result[i]+=1
# for word,count in result.items():
#     print(f"The character {word} is repeated {count} times")

#     OR


# def count(inputStr):
#   result=dict()
#   for i in inputStr:
#        if i not in result:
#         result[i]=1
#        else:
#         result[i]+=1
#   return dict
# Str=input("Enter the string:")
# print(count(Str))

#   OR

# a=input("Enter the string:")
# dict={}
# for i in a.lower().strip():
#     if i not in dict:
#         dict[i]=1
#     else:
#         dict[i]+=1
# for i in dict:
#     print(f"The character {i} is repeated {dict[i]} times")



# 3) Write a Python program to split a given list into two parts where the length of the first
# part of the list is given.

# originallist=input("Enter the list elements seperated by comma:").split()
# firstPartLength=int(input("Enter the length of the first part of the list:"))
# firstPartList=originallist[:firstPartLength]
# secondPartList=originallist[firstPartLength:]
# print("First part of the list is:",firstPartList)
# print("Second part of the list is:",secondPartList)


# 4)Calculate the sum of tuples in a given tuple
# demo = [(1,2),(3,5),(5,6)]
# sum=0
# for i in demo:
#     sum=sum+i[0]+i[1]
# print(sum)

# 5)Iterate the given tuple
# student=(111,"Akash",)
# for i in student:
#     print(i)

# 6)Repeat the given tuple 4 times
# example =(1,2)
# print(example*4)

#6) write a Python program to Remove items from set1 that are not common to
# both set1 and set2.
# Input:
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# Output:
# {40, 50, 30}

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# intersectionSet=set1.intersection(set2)
# print(intersectionSet)




