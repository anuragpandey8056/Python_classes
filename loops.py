# code repetation in sequence we use loop 
# it supprt two loop
# for()   finite time
# while() infinite

# syntax
# print 1 to 10 no 
# x=1
# while x<=10:
#     if x<10:

#         print(x,end=',')                # to print in same line
#     else:
#         print(x)

#     x=x+1

# y=0
# x=1
# while x<=10:
#     y=y+x
#     if x<10:
#         print(x,end='+')                # to print in same line
#     else:
#         print(x,end="=")

#     x=x+1
# print(y)
# ====================upto=====================================================================
# y=int(input("enter a no"))
# x=1

# while y>=x:
#     if y%2==0:                 #to check value given even or odd
#         if x%2==0:             # to find even no
#             if x<y:            # for output
#                  print(x,end=',')  # to get 
#             else:
#                 print(x)

#     else:
#         if x%2==0:
#             if x<y-1:
#                 print(x,end=(","))
#             else:
#                 print(x)
#     x=x+1

# ========================sum of upto even no================================================
# y=int(input("enter a no"))
# x=1
# z=0


# while y>=x:

#     if y%2==0:                 #to check value given even or odd
#         if x%2==0:
#             z=z+x             # to find even no
#             if x<y:            # for output
#                  print(x,end='+')  # to get 
#             else:
#                 print(x,end='=')
#                 print(z)

                

#     else:
#         if x%2==0:
#             z=z+x             # to find even no

#             if x<y-1:
#                 print(x,end=("+"))
#             else:
#                 print(x,end='=')
#                 print(z)
#     x=x+1

# ===================n even no==================================================
# y=int(input("enter a no"))
# x=1


# while y*2>=x:
#     if x%2==0:
#         z=z+x
#         if x<y*2-1:
#             print(x,end='+')
#         else:
#             print(x)

        
#     x=x+1

# ===========================sum of n even no=====================================
# y=int(input("enter a no"))
# x=1
# z=0

# while y*2>=x:
#     if x%2==0:
#         z=z+x
#         if x<y*2-1:
#             print(x,end='+')
#         else:
#             print(x,end='=')
#             print(z)

        
#     x=x+1


# ===================================== generate upto odd no===================================
# y=int(input("enter a no"))
# x=1

# while y>=x:
#     if y%2==0:                 #to check value given even or odd
#         if x%2!=0:             # to find even no
#             if x<y-1:            # for output
#                  print(x,end=',')  # to get 
#             else:
#                 print(x)

#     else:
#         if x%2!=0:
#             if x<y-1:
#                 print(x,end=(","))
#             else:
#                 print(x)
#     x=x+1

# ===========================sum of upto odd  no==============================================
# y=int(input("enter a no"))
# x=1
# z=0

# while y>=x:
#     if y%2==0:                 #to check value given even or odd
#         if x%2!=0:
#             z=z+x             # to find even no
#             if x<y-1:            # for output
#                  print(x,end=',')  # to get 
#             else:
#                 print(x,end='=')
#                 print(z)

#     else:
#         if x%2!=0:
#             z=z+x
#             if x<y-1:
#                 print(x,end=(","))
#             else:
#                 print(x,end='=')
#                 print(z)
#     x=x+1


# ===================n odd no==================================================
# y=int(input("enter a no"))
# x=1


# while y*2>=x:
#     if x%2!=0:
#         if x<y*2-1:
#             print(x,end='+')
#         else:
#             print(x)

        
#     x=x+1

# =================== sum n odd no==================================================
# y=int(input("enter a no"))
# x=1
# z=0


# while y*2>=x:
#     if x%2!=0:
#         z=z+x
#         if x<y*2-1:
#             print(x,end='+')
#         else:
#             print(x,end='=')
#             print(z)

        
#     x=x+1


# =================================================================FOR LOOP========================================================
# x=int(input("enter a no"))
# for i in range(1,x+1):
#     if(i<x):
#         print(i,end=(','))
#     else:
#         print(i)
# even no upto====================================================
# x=int(input("enter a no"))
# for i in range(1,x+1):
#     if i%2==0:
#         if i<x-1:
#           print(i,end=(','))
#         else:
#           print(i)
# =====================================odd upto=====================
# x=int(input("enter a no"))
# for i in range(1,x+1):
#     if i%2!=0:
#         if i<x-1:
#           print(i,end=(','))
#         else:
#           print(i)

# ==============================n even no
# x=int(input("enter a no"))
# for i in range(1,(x*2)+1):
#     if i%2==0:
#         if i<(x*2)-1:
#           print(i,end=(','))
#         else:
#           print(i)

# ==============================n odd no==================================

# x=int(input("enter a no"))
# sum=0
# for i in range(1,(x*2)+1):
#     if i%2!=0:
#         sum=sum+i
#         if i<(x*2)-1:
#           print(i,end=('+'))
#         else:
#           print(i,end="=")
#           print(sum)

# my_str=input("enter a name")
# for i in  my_str:
    
# ====================== to check volwel consonent ==============================================================================
# x=input("enter a name")
# vol=cons=0
# for i in x:
#     if i in ('a','e','i','o','u','A','E','I','O','U'):
#         vol=vol+1
#     else:
#         cons=cons+1
# print(vol,cons)

# ================================ to count the what we type count=============================================================
x=input("enter a anything")
alphabet=special=no=0
for i in x:
    y=ord(i)
    if y>=65 and y<=90 or y>=97 and y<=122:
        alphabet=alphabet+1
    elif y>=48 and y<=57:
        no=no+1
    elif y>=32 and y<=47 or y>=58 and y<=64 or y>=91 and y<=96 or y>=123 and y<=126:
        special=special+1
print(alphabet,no,special)
        



   
       
    
    