# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 16:15:51 2026

@author: Ankitsinh
"""


# Student Information System

rollNo = int(input("Enter student Roll No : "))
name = input("Enter student Name :  ")
age = int(input("Enter student Age : "))

#------- Student Subject Marks ------------

java = eval(input("Enter Java Marks : "))
python = eval(input("Enter Python Marks : "))
dbms = eval(input("Enter DBMS marks : "))

# --------- Student Marks Calculation

if (java < 40 or python < 40 or dbms < 40):
    print("Studetn Fail")

elif (java > 40 or python > 40 or dbms > 40):
    
    total = java + python + dbms
    print("Total Marks : ", total)
    
    percentage = (total / 3) * 100
    print("percentage is : ",percentage)
    
    print("Studetn pass")
else :
    print("invlaid marks")
        
print("Student RollNo: ", rollNo)
print("Student Name: ", name)
print("Studetn Age: ", age)




        
        
       
        
    




