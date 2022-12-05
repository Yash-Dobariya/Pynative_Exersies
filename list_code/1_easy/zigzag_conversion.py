str1="PAYPALISHIRING"
# str2="PAYPALISHIRING"
depth = int(input("Enter your number : "))

convert_list=list(str1)
zigzag=[]
# for i in range(depth):

app_list1=convert_list[::depth]
zigzag.extend(app_list1)

# app_list2=convert_list[::1-depth]
# zigzag.extend(app_list2)

# app_list3=convert_list[::2-depth]
# zigzag.extend(app_list3)
    
    



print("".join(zigzag))

    
    
    
# elif convert_list1 > lenth1:
   
    # app_list1=convert_list[::4]
    # list1.extend(app_list1)
    # app_list2=convert_list[1::2]
    # list2.extend(app_list2)
    # app_list3=convert_list[2::4]
    # list3.extend(app_list3)
    # app_list4=convert_list[2::4]
    # list3.extend(app_list4)

    # c=list1+list2+list3
#     print("".join(c))

# else :
#     print("unsatisfying")