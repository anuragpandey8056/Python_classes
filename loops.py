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


    