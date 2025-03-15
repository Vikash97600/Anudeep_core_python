
# 1) Python program to check number is wheather a positive , negative or zero
# def div(x,y):
#     try:
#          result=x/y
#          print("The division of a and b is:",result)
#     except ZeroDivisionError:
#         print("You cannot divide by zero")
# a=int(input("Enter the value of a:"))
# b=int(input("Enter the value of b:")) 
# div(a,b)

# 2) Python program to cube of a number
# def cube(x):
#     result=x*x*x
#     print("The cube of a is:",result)
# a=int(input("Enter the value of a:"))
# cube(a)

# 3) Pyhton program to find area of triangle whose sides are given

# import math
# def areaOfTriangle(a,b,c):
#   s=a+b+c/2
#   area=math.sqrt(s*(s-a)*(s-b)*(s-c))
#   print(area)
# a=int(input("Enter the side1 of triangle:"))
# b=int(input("Enter the side2 of triangle:"))
# c=int(input("Enter the side3 of triangle:"))
# areaOfTriangle(a,b,c)

# 4) Pyhton program to find the factorial of a number using function

# def fact(x):
#     result=1
#     for i in range(1,x+1,1):
#         result=result*i
#     print(result)
# a=int(input("Enter the value of a:"))
# fact(a)

# 5) Python program to reverse the number using function

# def reverse(num):
#     temp=num
#     rev=0
#     while num>0:
#         rem=num%10
#         rev=rev*10+rem
#         num=num//10
#     print(rev)
# a=int(input("Enter the value of a:"))
# reverse(a)

# 6) Python program to check whether a number is palindrom or not

# def palindrome(num):
#     temp=num
#     rev=0
#     while num>0:
#         rem=num%10
#         rev=rev*10+rem
#         num=num//10

#     if temp==rev:
#         print(f"The number {temp} is palindrome")
#     else:
#         print(f"The number {temp} is not palindrome")

# a=int(input("Enter the value of a:"))
# palindrome(a)

# 7) Python program to check whether a string is palindrom or not

# def palindrome(str):
#     if str==str[::-1]:
#         print(f"The string {str} is palindrome")
#     else:
#         print(f"The string {str} is not palindrome")

# a=input("Enter the string:")
# palindrome(a)


# 8) Pyrhon program to find the number is an armstrong number or not

# def armstrong(num):
#     temp=num
#     sum=0
#     while num>0:
#         rem=num%10
#         sum=sum+rem*rem*rem
#         num=num//10

#     if temp==sum:
#         print(f"The number {temp} is armstrong")
#     else:
#         print(f"The number {temp} is not armstrong")

# a=int(input("Enter the value of a:"))
# armstrong(a)
               
                #    OR


given_number = int(input("Enter a number"))

given_number=str(given_number)

string_length = len(given_number)
sum=0

for i in given_number:
    sum+=int(i)**string_length

if sum==int(given_number):
    print("Armstrong number")
else:
    print("Not armstrong no")