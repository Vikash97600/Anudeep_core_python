# first_list=[11,12,13,14,15,16,17]
# print("Original list is:",first_list)
# for i in first_list:
#     print(i)

# # create a sublist form the first list
# sub_list=first_list[2:5]
# print("Sub list is:",sub_list)

# #find length of the first list
# lengthList=len(first_list)
# print("Length of the list is:",lengthList)

# # adding an element at the end of the first list
# first_list.append(200)
# print("Appended list is:",first_list)

# # adding an elements at the end of the first list
# first_list.extend([18,19,20])
# print("Extended list is:",first_list)

# # adding an element between the first list at a specific index(2) member(200)
# first_list.insert(2,100)
# print("Inserted list is:",first_list)

# # removing an element from the first list
# first_list.remove(100)
# print("After rmoving the element, list is:",first_list)

# #removing the element from the first list according to index
# first_list.pop(0)
# print("After removing the first element, list is:",first_list)

# # removing the last element from the first list
# first_list.pop()
# print("After removing the last element, list is:",first_list)

# # sorting the list items
# first_list.sort()
# print("Sorted list is:",first_list)

# # sorting the list items in reverse order
# first_list.sort(reverse=True)  # or first_list.reverse()
# print("Reverse sorted list is:",first_list)

# #copy the list to another list
# another_list=first_list.copy()
# print("Copied list is:",another_list)

# #count the occurrence of an element in the 
# count=first_list.count(11)
# print("Count of 11 is:",count)

# #get the minimum numbers from the list
# minumum=min(first_list)
# print("Minimum number is:",minumum)

# # print the maximum number from the list
# maximum=max(first_list)
# print("Maximum number is:",maximum)

# #clear the list
# first_list.clear()
# print("Cleared list is:",first_list)


# PDF QUESTIONS
# 1.Take 10 integers from the keyboard using a while loop and print their average value on the screen without exception handling.

sum=0
count=0
while count<10:
    num=int(input("Enter the number:"))
    sum=sum+num
    count=count+1
average=sum/10
print("The average is:",average)

total = 0  
count = 0  

