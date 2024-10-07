# ==================================================pattern========================================
# n=int(input("enter no of rows\n"))
# for i in range(n):       # only last value show karega
#     print("*"*n)

# ============================================================
# n=int(input("enter no of row\n"))

# for i in range(1,n+1):                  
#     print("*"*i)
# ==========================================================
# n=int(input("enter no of row\n"))

# for i in range(1,n+1):
#     print(' '*(n-i)+"*"*i)
# ===========================================================
# n=int(input("enter no of row\n"))

# for i in range(1,n+1):
#     print(' '*(n-i)+" *"*i)

# ===============================================================
# n=int(input("enter no of row\n"))
# for i in range(n,0,-1):
#     print('*'*i)

# ============================================================
# n=int(input("enter no of \n"))
# for i in range(n,0,-1):
#     print(" "*(n-i)+'*'*i)

# =======================================================
# n=int(input("enter no of row\n"))

# for i in range(n,0,-1):
#     print(' '*(n-i)+" *"*i)
# =======================================================================
# n=int(input("enter no of row\n"))
# for i in range(1,n+1):                  
#     print("*"*i)
# for i in range(n-1,0,-1):
#     print('*'*i)

# ==================================================================
# n=int(input("enter no of row\n"))
# for i in range(1,n+1):
#     print(' '*(n-i)+"*"*i)
# for i in range(n-1,0,-1):
#     print(" "*(n-i)+'*'*i)


# # ===============================================
# n= int(input("enter a no of rows"))
# for i in range(1,n+1):
#     print("*"*i)
# for i in range(n-1,0,-1):
#     print(" "*(n-i)+"*"*i)


# ===============================================
# n= int(input("enter a no of rows"))
# for i in range(1,n+1):
#     if i==n:
#         print("*"*i,end="")
#     else:
#         print("*"*i)
# for i in range(n,0,-1):
#     if i==n:
#         print(" "*(n-i)+"*"*i)
#     else:
#        print(" "*n+" "*(n-i)+"*"*i)

# ===============================Armstrong NO==========================
# n=int(input("enter a no"))
# m=x=n
# sum=0
# digit=0
# i=0
# while i<n:
#     n=n//10
#     digit=digit+1
# while i<m:
#     last_digit=m%10
#     sum=sum+last_digit**digit
#     m=m//10
# if x==sum:
#     print("it is Armstrong")
# else:
#     print("not a Armstrong")


# =====================================Palindrome========================================================================
# n= input("enter any value")
# x=n[::-1]
# if n==x:
#     print("it is palindrome")
# else:
#     print("it is not a palindrome")

# ====================================================================
# n= int(input("enter a digit"))
# y=n
# i=0
# digit=0
# while i<n:
#     rev= n%10
#     digit=digit*10+rev
#     n=n//10
# print("reverse digit ",digit)
# if y==digit:
#     print("it is palindrome")
# else:
#     print("not palindrome")


# ========================palindrom without using function=============================================
# n= input("enter any value")
# rev = ""
# for i in  n:
#     rev = i+rev
# print(rev)
# if n==rev:
#     print("it is palindrome")
# else:
#     print("it is not a palindrome")

# ====================================fibonaccie =====================================================================
n= int(input("enter a n no to generate digit"))
a=0
b=1
i=1
print(a,end=',')
print(b,end=',')
while i<=(n-2):

    c=a+b
    a=b
    b=c
    if i<n-2:
     print(c,end=',')
    else:
     print(c)
    i=i+1



