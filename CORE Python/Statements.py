# print("Python full stack development course")    #print statement

# stu_id=1002       #assignment statement
# print(stu_id)

# sub1=88
# sub2=78
# sub3=90
# sub4=77
# sub5=88

# total_marks=(sub1+sub2+sub3+sub4+sub5)     #expression statement
# print("Total marks are:",total_marks)

# student_name=input("Enter the student name:")     #Input statement
# print(student_name)

# dataMember=int(input("Enter any number:"))
# if dataMember==99:                           #conditional statements
#     print("It is greater than 99")
# else:
#     if dataMember==100:
#         print("Equal to 100")
#     else:
#         print("Less than 100")


# loop_variable = 1                      #loop statement
# while loop_variable <10:
#     if loop_variable%2==0:
#         print("Even number")
#         print(loop_variable)
#     else :
#         print("Odd number")
#         print(loop_variable)
#     loop_variable+=1

# for counter in range(1,10,1):            #for in loop
#     print(counter)


# def sumOfNumbers(first,second):         #function/method statement
#     return(first+second)
# result=sumOfNumbers(11,2)
# print("The result is:",result)

# try:                                     #Exception handling statement
#     error_log=10/0
# except ZeroDivisionError as e:
#     print("An Error occured as:",e)


for count in range(1,20,1):              #Jump statements
    if count==11:
        break
    if count==5:
        continue
    if count==9:
        pass
    print(count)