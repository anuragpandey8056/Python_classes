# write once and call multiple code reusebility block of code baar repeate ho rha ho 
# two types of function
# Ibuilt function => print(),type(),str(),etc.......
# userdefine function=>
# without name function is called lamda function
# c python interpreter hai jaha inbuilt function likhe hai 
# def add(x,y):
#     print(x+y) 
#     return x+y
# x=int(input("enter a one")) 
# y=int(input("enter a twoe")) 
# d=add(x,y)
# print(d)

# ======================return=========================================
# def add(x,y): 
#     p=x+y
#     q=x*y
#     r=x//y
#     s=x%y
#     return p,q,r,s

# x=int(input("enter a one")) 
# y=int(input("enter a twoe")) 
# a,s,m,d,=add(x,y)
# print(a,s,m,d)

# ===================================================================================
# evail run time pe data type pahechan leta hai 
#  mathmatical calculation karwane ke liye 

# collection = eval(input("enter a collection"))
# print(collection)
# print(type(collection))
# count = 0
# for i in collection:
#     count=count+1
# print(count)


# ==========================================================================================
# def mylen(collection):
#     count=0
#     for i in collection:
#         count=count+1
#     return count

# collection = eval(input("enter any collection"))
# mylen1=mylen(collection)
# print("len=",mylen1)


# ==========================================type of argument ==============================================
# 1. positional argument
# 2. keyword argument

# def mylen(x,y):
#     print(x,y)
   
#     return x+y

# a = int(input("enter any no"))
# b= int(input("enter any no"))

# mylen1=mylen(x=a,y=b)
# print("len=",mylen1)


# 3. Default argument
# def mylen(x=0,y=0):
#     print(x,y)
   
#     return x+y

# a = int(input("enter any no"))
# b= int(input("enter any no"))

# mylen1=mylen()
# mylen2=mylen(a)
# mylen3=mylen(y=b)

# print("len1=",mylen1)
# print("len2=",mylen2)
# print("len3=",mylen3)











