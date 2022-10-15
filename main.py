# username and password validation
# user_name=["athul","ajay","jithin"]
# pass_word=["a123","b123","c123"]
# x=input("enter your username:")
# if x in user_name:
#     pswd=input("enter your password:")
#     ind = user_name.index(x)
#     if pswd in pass_word and ind==pass_word.index(pswd):
#         print("logged in")
#     else:
#         print("incorrect password")
# else:
#     print("incorrect username")

# --------------------------------------------
# adding 5 names to  list
# name=[]
# for i in range(1,6):
#     x=input("enter your name:")
#     name.append(x)
# age=[]
# for j in range(6):
#     y=int(input("enter your age:"))
#     age.append(y)
# print(name)
# print(age)

# -------------------------------------------------

# pgm to count vowels in a string
# x=input("enter a sentence:")
# count=0
# for i in x:
#     if i in ["a","e","i","o","u"]:
#         count+=1
# print(count)
# ----------------------------------------------

# a=input("enter a word:")
# if a[0]=="p":
#     print("welcome")
# else:
#     print("no entry")
# --------------------------------------------------

# palindrome
# a=input("enter a word:")
# n=len(a)
# flag=0
# for i in a:
#     if i != a[n]:
#         flag=1
#         break
#     n=n-1
#
# if flag==1:
#     print("not a palindrome")
# else:
#     print("it is a palindrome")

# a=input("enter a word")
# rev=a[::-1]
# print(rev)
# if a==rev:
#     print("palindrome")
# else:
#     print("not a palindrome")

# -----------------------------------------

# dict={"abay":23,"aju":21,"arun":22,"akash":20,"anju":22}
# print(dict["arun"])
# print(dict.__getitem__("arun"))
# dict.__setitem__("achu",24)
# print(dict)
# dict.popitem()
# print(dict)
# dict.pop("aju")
# print(dict)
# print(dict.keys())

# -----------------------------------------------
#addinf 5 names and ages to a dictionary

# dict={}
# for i in range(1,6):
#     name=input("enter your name:")
#     age=int(input("enter your age:"))
#     dict.__setitem__(name,age)
# print(dict)

# ------------------------------------------------

# dict={10:"sunday",8:"monday",100:"tuesday",4:"wednesday",5:"thursday",6:"friday",7:"saturday"}
# a=int(input("enter a number"))
# if a in dict.keys():
#     print(dict.__getitem__(a))
# else:
#     print("not found")

# ------------------------------------------------

# a="1234"
# print(a.isnumeric())
# b="abcd"
# print(b.isnumeric())
# a="welcome to python class"
# print(a.startswith("w"))
# print(a.upper())
# print(a.lower())
# print(a.count("o"))
# print(a.find("l"))
# print(a.replace("python","java"))
# print(a.split("to"))

# ------------------------------------------------------
'''
define a function which can generate a list where the values are square of numbers between 1 and 20 (bothincluded).
Then the function needs to print the last 5 elements in the list
'''

# def square():
#     list = []
#     for i in range(1, 21):
#         list.append(i * i)
#     print(list[-5:])
#
# square()

'''
with a given tuple(1,2,3,4,5,6,7,8,9,10),write a program to print the first half values in one line and last
 half values in another line
'''
# tuple=(1,2,3,4,5,6,7,8,9,10)
# print(tuple[:5])
# print(tuple[5:])

'''
write a program which accept a string as input to print "yes" if the string is "yes" or "YES" or "Yes" ,otherwise print"No"
'''
# s=input()
# if s="yes" or s="YES" or s="Yes":
#     print("yes")
# else:
#     print("No")

'''
write a program which can filter even numbers in a list by using filter function.The list is:[1,2,3,4,5,6,7,8,9,10].
'''

# list1=[1,2,3,4,5,6,7,8,10]
# even=filter(lambda x:x%2==0,list1)
# print(list(even))

'''
please write a program to generate all sentences where subject is in ["I","YOU"] and verb is in ["Play","Love"]
 and the object is in ["Hockey","Football"].
'''
# for x in ["I","YOU"]:
#     for y in ["Play","Love"]:
#         for z in ["Hockey","Football"]:
#             print(x,y,z)

