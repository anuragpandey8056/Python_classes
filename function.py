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


# 3. Default argument#=========================================================================================



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
# ============variable length argument(*args)===argument as a tuple=====================================================================================
# def add(*n):
#     print(n)
#     print(type(n))
#     sum=0
#     for i in n:
#         sum=sum+i
#     print(sum)
# add(10)
# add(10,20,30,40)
# add(50,10,2,0,40,50,30,80,700,10)
# ===========================================================
# def add(*n):
#     print(n)
#     print(type(n))
#     global sum

#     sum=0
   
#     for i in n:
#         for x in i:
#             sum=sum+x
#     print(sum)
# x=eval(input("enter any collection"))
# add(x)
# print(sum)

# ========================================keyword variable length argument================================
# def add(**n):
#     print(n)
#     print(type(n))
#     for k,v in n.items():
#         print(k,":",v)
# add(name="anurag",age=97,qualify="btech")


# ==============================================
# def add(**n):
#     print(n)
#     print(type(n))
#     for keys in n.items():
#          print(keys)

        
# add(name="anurag",age=97,qualify="btech")



# ================================================HIGHER ORDER FUNCTION==============================================
# map
# filter
# reduce
# lambda

# ===================================================map()=====================================================================

# def my_square(n):
#     count=0
#     if count>=3:
#       count=count+1
      
      
#       return n+5
#     else:
#         count=count+1
#         return n+10
    
   

   


# my_list=[1,2,3,4,5]
# x=map(my_square,my_list)
# print(tuple(x))


# def my_even(n):
#     if n%2==0:
#         return "even"
#     else:
#         return "odd"

# my_list=[1,2,3,4,5]
# x=map(my_even,my_list)
# print(list(x))


# ============================================filter==========================================

# def my_even(n):
#     if n%2==0:
#         return n

# my_list=[1,2,3,4,5]
# x=filter(my_even,my_list)
# print(list(x))


# =========================================reduce============================================================
import functools
# my_list=[1,5,4,8,6]

# def my_max(x,y):
#     if x>y:
#         return x
#     else:
#         return y

# x= functools.reduce(my_max,my_list)
# print(x)

# =========================================================================================================
# my_list=[1,5,4,8,6]

# def my_max(x,y):

#         return x+y
   

# x= functools.reduce(my_max,my_list)
# print(x)












