''' 
File access modes:
r - read only mode
w - write only mode
a - append only mode
rb - read only in binary mode
wb - write only in binary mode
ab - append only in binary mode
r+ - read and write mode
w+ - write and read mode
a+ - append and read mode

File formates: 
.txt files, .csv files, .json files,.xml files(it is a tag based language),
.html files, .log files, .zip files, .doc files

File methods:
1) file = open(file_name or file_path,access_mode)
2) file.close() : closes the open file
3) file.read() : reads all the content of the file
4) file.write(content) : writes the content in the file
5) file.readline() : reads one line of the file
6) file.readlines() : reads all the lines of the file in a list

'''
# 1) WAP to read the studentDemo.txt file and print it
# def readStudentDemo():
#     file=open("studentDemo.txt","r")
#     for line in file:
#         print(line)
#     file.close()

# readStudentDemo()

# # 2) WAP to write the studentDemo.txt file and print it
# def writeStudentDemo():
#     file=open("studentDemo.txt","w")
#     file.write("Hello World")
#     file.close()

# writeStudentDemo()

# 3) WAP to count the words of a file

# def countWords():
#     file=open("studentDemo.txt","r")
#     count=0
#     for line in file:
#         words=line.split()
#         count+=len(words)
#     file.close()

#     return count
# print("The total number of words in the file is:",countWords())

                    #   OR

# def countWords():
#     file=open("studentDemo.txt","r")
#     count=0
#     data=file.read()
#     words=data.split()
#     for word in words:
#         count+=1
#     file.close()
#     return count
# print("The total number of words in the file is:",countWords())

# 4)WAP to count the lines of a file

# def countLines():
#     file=open("studentDemo.txt","r")
#     count=0
#     for line in file:
#         count+=1
#     file.close()
#     return count

# print("The total number of lines in the file is:",countLines())

# 5) WAP to count the characters of a file
# def countCharacters():
#     file=open("studentDemo.txt","r")
#     count=0
#     data=file.read()
#     words=data.split()
#     for line in words:
#         count+=len(line)
#     file.close()
#     return count
# print("The total number of characters in the file is:",countCharacters())

# 6) WAP to count the uppercase and lowercase characters of a file
# def countCharactersUpperLowercase():
#     file=open("studentDemo.txt","r")
#     data=file.read()
#     uCount=0
#     lCount=0
#     for char in data:
#         if char.isupper():
#             uCount+=1
#         else:
#             if char.islower():
#                 lCount+=1
#     print("The total number of lowercase characters in the file is:",lCount)
#     print("The total number of uppercase characters in the file is:",uCount)
#     file.close()
# countCharactersUpperLowercase()

# 7) WAP which takes file name as input and the content of the file as input and overwrites it in a new file
# def overwrite(filename,content):
#     file=open(filename,"w")
#     file.write(content)
#     file.close()
# filename=input("Enter the file name:")
# content=input(f"Enter the content of the file {filename}:")
# overwrite(filename,content)

# 8) WAP which takes file name as input and the content of the file as input and appends it in a new file
def appendFile(filename,content):
    file=open(filename,"a+")
    file.write(content)
    file.close()
filename=input("Enter the file name:")
content=input(f"Enter the content of the file {filename}:")
appendFile(filename,content)