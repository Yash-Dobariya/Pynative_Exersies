number=int(input("Enter palindrom number : "))
orignal_num=number
res1=0
while number>0:
    res= number % 10
    res1= (res1 * 10)+ res
    number=number // 10

if orignal_num == res1 :
    print("This is Pelindrom number ")
else :
    print("This is not Pelindrom number ")



