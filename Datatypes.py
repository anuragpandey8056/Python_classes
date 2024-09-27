'''
x,y,z = 10,20,30
print(x,y,z)

x=y=z=p=q=r=10
print(x,y,z,p,q)

x='neeraj'
p,q,r,a,b,c=x
print(p,q,r,a,b,c)

x=[10,20,30,40,50]
p,q,r,a,b=x
print(p,q,r,a,b)


x=(10,20,30,40,50)
p,q,r,a,b,=x

print(p,q,r,a,b)


'''
# ===============================================integer==============================================
# x=20
# y=10
# print(x/y)
# print(type(x/y))

# # ===============================================complex==============================================
# x=2+3j
# y=3+2j
# print(x*y)
# print(x/y)

# #=========================================================string in built functions =======================
# my_str="python"
# print(len(my_str))
# print(max(my_str))
# print(min(my_str))
# print(id(my_str))
# print(type(my_str))

# ==================================================list =================================
# my_list = [10,20,[5,20,30],'neeraj']
# print(my_list)
# print(id(my_list))
# print(type(my_list))

# ======================================inbuilt function of list =============================
# my_list = [10,20,[5,20,30],'neeraj']
# my_list1 = [10,20,5,20,3]
# print(sum(my_list1))
# print(len(my_list1))
# print(max(my_list1))
# print(min(my_list1))
# print(id(my_list1))
# print(type(my_list1))
# print(list(my_list))

# =========================================================methods of list ==================
# ==================================================append last me add  karata hai
# my_list = [10,20,20,'anurag','neeraj']
# my_list.append(50)
# my_list.append('hello')
# print(my_list)

# ========================================================extend===============
# my_list = [10,20,20,'anurag','neeraj']
# my_list1 = [30,40,50,60,70,80]
# my_list.extend(my_list1)
# print(my_list)

# ========================================================insert===============
# my_list = [10,20,20,'anurag','neeraj']
# my_list1 = [30,40,50,60,70,80]
# my_list.insert(3,'consume')
# my_list.insert(3,my_list1)
# print(my_list)


# # ========================================================copy===============
# my_list = [10,20,20,'anurag','neeraj']
# x= my_list.copy()
# print(x)                                        # both x and my_list location(id) are different 
# print(id(my_list))
# print(id(x))


# ========================================================clear===============
# my_list = [10,20,20,'anurag','neeraj']
# my_list.clear()
# print(my_list)   # clear ke baad bhi blank list show karega to usko dlt karne ke liye 
# print(id(my_list))
# del my_list    # to dlt my list like this []
# print(my_list)

#=============================index ke ander object pass karte hai uska index mil jata hai

# my_list =[10,20,30,40,50,60]
# print(my_list.index(40))


# ==================================frequemcy(count) count(object) ye object kitni baar aaya hai
# my_list =[10,20,30,40,50,60,40,40]
# print(my_list.count(40))


# ================================== remove(object)
# my_list =[10,20,30,40,50,60,40,40]
# my_list.remove(50)
# print(my_list)
# ====================================reverse ()
# my_list =[10,20,30,40,50,60,40,40]
# my_list.reverse()
# print(my_list)

# ===============================SORT()

# my_list =[10,20,30,40,50,60,40,40]
# my_list.sort()
# print(my_list)
# my_list.reverse()
# print(my_list)
# =====================================shortcut to do decending order
# my_list =[10,20,30,40,50,60,40,40]
# my_list.sort(reverse=True)
# print(my_list)

# ==============================================================================tuple=======================================================
# my_tuple = (10,20,30,'jail','raj')
# my_tuple1=(10,20,50,40,70)
# print(len(my_tuple))
# print(sum(my_tuple1))
# print(max(my_tuple1))
# print(min(my_tuple1))
# print(id(my_tuple))
# print(type(my_tuple))

# =============================================================inbuilt method
# my_tuple1=(10,20,50,40,40,70)

# print(my_tuple1.index(40))


# ============================dictionary=========================
# my_dict = {'x':10,'y':20,'z':30}
# print(len(my_dict))
# print(max(my_dict))
# print(min(my_dict))
# print(id(my_dict))
# print(type(my_dict))
# x= dict()
# print(x)
# print(type(x))

# =============================================================inbuilt method

# fromkeys()  to change the list tuple into dictionary
# my_list = ['a','b','c','d']
# my_dict = dict.fromkeys(my_list)
# print(my_dict)

# fromkeys()  to change the list tuple into dictionary
# my_list = ['a','b','c','d']
# my_dict = dict.fromkeys(my_list,10) #bydeafult value none rahti hai usko de dediye to value 10 dega
# print(my_dict)
# print(my_dict['a'])  # to access the value with key this  type 
# my_dict['a']=50
# print(my_dict)
# my_dict.update({'a':80,'b':69,'c:':68,'d':258})# to update the multiple value
# print(my_dict)

# my_dict['f']=5  # to add new key value pair
# print(my_dict)

# my_dict.setdefault('g',40)  # is case me agr poorana hai same key value pair overwrite nhi hogi aur agr unique hai key value to new key value create kar dega 
# print(my_dict)

# ==============================================pop()========================================
# my_dict = {'x':10,'y':20,'z':30}
# my_dict.pop('x')
# print(my_dict)

# my_dict.popitem()  # ye bydefault akhri object ko remove karta hai  iske argument me keys nhi pass kar skte hai
# print(my_dict)

# =========================================keys============================
# mydict = {'x':10,'y':20,'z':30}
# print(mydict.keys())
# print(mydict.values())
# print(mydict.items())

# ==============================================get================
# mydict = {'x':10,'y':20,'z':30}
# print(mydict.get('x'))
# print(mydict['x'])


#==========================================set===============================================================================
# my_set = {10,20,30,40,50,60}
# print(my_set)

# ===========================================inbuilt method=====================================================
# my_set = {10,20,30,40,50,60}
# my_set2 = {10,60,30,40,50,60}
# print(my_set.union(my_set2))
# print(my_set.intersection(my_set2))
# print(my_set.difference(my_set2))
# print(my_set.symmetric_difference(my_set2))


# ===========================================inbuilt method=====================================================
# my_set = {10,20,30,40,50,60}
# my_set2 = {10,60,30,40,50,60}
# my_set.clear()
# print(my_set)


# my_set = {10,20,30,40,50,60}
# my_list=[1,2,5,4]
# # str = "anurag"
# # my_set.add(800)
# # print(my_set)
# # my_set.update(str)
# # print(my_set)
# my_set.update(my_list)
# print(my_set)



# my_set = {10,20,30,40,50,60}
# my_set.pop()   #isme random object ko remove karta hai
# print(my_set)


# my_set = {10,20,30,40,50,60}
# my_set.remove(10)
# print(my_set)

# my_set = {10,20,30,40,50,60}
# my_set.discard(10)  
# print(my_set)

# my_set = {10,20,30,40,50,60}
# my_set.discard(10)   # agr koi object aisa hai jo set me nahi hai agr usko pass  kar de to isme error nhi aata hai isme wahi set show ho jata hai 
# print(my_set)


# ================================================Frozenset=================================================
my_set = {10,20,30}
my_list = [10,20,30,40]
my_tuple = (10,20,30)
x= frozenset(my_set)
y= frozenset(my_list)
z= frozenset(my_tuple)

# print(x,y,z)
# print(type(x))
# print(type(y))
# print(type(z))

print(x.union(y))
print(x.intersection(y))
print(x.difference(y))
print(x.symmetric_difference(y))

















   





























