str1 = "Hello World 2345"
sum_num = 0
for x in str1:
    if x.isdigit() == True:
        sum_num = sum_num + int(x)
print(sum_num)