# 1)Python program to print the frequency of uppercase,lowercase,digits,symbols in a string
# str = "Application Development Using Python !! 2025"
# print("My string is:",str)

# upr,lwr,num,spl=0,0,0,0
# for i in range(len(str)):
#     if str[i]>='A' and str[i]<='Z':
#         upr+=1
#     elif sstr[i]>='a' and str[i]<='z':
#         lwr+=1
#     elif str[i]>='0' and str[i]<='9':
#         num+=1
#     else:
#         spl+=1

# print("Uppercase letters : ",upr)
# print("Lowercase letters : ",lwr)
# print("Numbers : ",num)
# print("Special chacters ",spl)



# 2)Python program to find number of vowles and consonants in a string

# demoStr=input("Enter any string to find out Vowels/Consonants: ")
# countVowels=0
# countConsonants=0
# for i in demoStr:
#     if(i=='A' or i=='a' or i=='E' or i=='e' or i=='I' or i=='i' or i=='O' or i=='o' or i=='U' or i=='u'):
#         countVowels+=1
#     else:
#         countConsonants+=1
# print(f"Total vowels in a string {demoStr} is {countVowels}")
# print(f"Total consonants in a string {demoStr} is {countConsonants}")

# 3)Python program to find repetition of a character from the string










# 4) Pyhton program to remove the duplicate character from string and print the new string

input_string = "string and string functions"

result_str=""

print("Original String  is :",input_string)

for char in input_string.split(' '):
    if char not in result_str:
        result_str+=' '+char

print("Resultant string when duplicates are removed : ",result_str)



