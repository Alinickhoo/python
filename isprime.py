x = int(input("enter your number:"))
flag = True
for i in range(2, x):
    if x % i == 0:
        flag = False
        break
if flag == True:
    print("yes")
elif flag == False:
    print("no")
