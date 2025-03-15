# 1)Python program to check number is wheather a positive , negative or zero

num1=float(input("Enter a number:"))
if(num1>0):
    print("The number you have entered is a Positive number.")
elif (num1==0):
    print("The number you have entered is a Zero.")
else:
    print("The number you have entered is a Negative number.")


# num1=int(input("Enter the value of num1:"))
# num2=int(input("Enter the value of num2:"))
# num3=int(input("Enter the value of num3:"))

# if(num1>num2) and (num1>num3):
#     greatest=num1
# elif(num2>num1) and (num2>num3):
#     greatest=num2
# else:
#     greatest=num3
# print("The gratest number is : ", greatest )

                #OR
# if(num1>num2):
#     if(num1>num3):
#         print("Greatest no: ", num1)
#     else:
#         print("Greatest no:",num3)
# else:
#     if(num2>num3):
#         print("Greatest no: ", num2)
#     else:
#         print("Greatest no:",num3)

# 3)Python program to calculate electricity bill(Self study)

# typeOfUser = input("Enter the type of user (Household or Small Business or Industrial): ").strip().lower()
# consumption = int(input("Enter the consumption in a month in units: "))

# if typeOfUser == "household":
#     rate = 2
# elif typeOfUser == "small business":
#     rate = 5
# elif typeOfUser == "industrial":
#     rate = 10
# else:
#     print("You are a Invalid user. Please enter Household or Small Business or Industrial.")

# total_bill = consumption * rate
# print(f"Your total electricity bill is: Rs {total_bill} ")



# 4)Python program to calculate a year is a leap year or not

# year=int(input("Enter the year:"))
# if(year<0):
#     print("Year should be in positive")
# elif(year%4==0) and (year%100!=0):
#     print("Year is a leap year")
# else:
#     print("Year is not a leap year")




                            # CONDITIONAL CONSTRUCT PDF LAST QUESTIONS
# 5) A company decided to give a bonus of 5% to an employee if his/her year of
# service is more than 5 years .Ask users for their salary and year of service and
# print the net bonus amount.

# userSalary=int(input("Enter the salary of user:"))
# userServiceYear=int(input("Enter the year of service"))

# if userServiceYear>5:
#     userSalary1=((userSalary)+(5/100*userSalary))
#     bonusOfUser=(userSalary1-userSalary)
#     print(f"Bouns of the user is {bonusOfUser}")
# else:
#     print("You are not applicable for bonus")


# 6) Write a program that prompts the user to enter the quantity of items they want to purchase. Each unit costs $100. If the total cost exceeds $1000, a 10%
# discount will be applied. The program should then calculate and display the final total cost after considering any discount.

# qtyOfItemPurchase=int(input("Enter the quantity of item that you want to purchase:"))
# unitCostOfItemPurchase= 100
# totalCost=(qtyOfItemPurchase*unitCostOfItemPurchase)
# if(totalCost>1000):
#     finalCost=(totalCost-10/100*totalCost)
# else:
#     print("Sorry,your total cost is not greater than $1000 .So you are not applicable to get 10% discount ")

# print(f"The final total cost after considering discount is {finalCost}")
