# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 16:15:51 2026

@author: Ankitsinh
"""


    # Student Information System



def stu_information():
    
    print("\n======= Enter Student Inforamtion ======")
    
    rollNo = int(input("Enter student Roll No : "))
    name = input("Enter student Name :  ")
    age = int(input("Enter student Age : "))

    #------- Student Subject Marks ------------
    print("\n===== Enter Subject Marks ======\n")
    
    java = eval(input("Enter Java Marks : "))
    python = eval(input("Enter Python Marks : "))
    dbms = eval(input("Enter DBMS marks : "))

    # --------- Student Marks Calculation

    if (java < 40 or python < 40 or dbms < 40):
        print("\n Student Fail \n")

    elif (java > 40 or python > 40 or dbms > 40):
        
        total = java + python + dbms
        
        percentage = (total / 3) * 100
        
        print("\n ----- Student Result -----\n")
        print("Total Marks : ", total)
        print("percentage is : ",percentage)
        print("Student Pass.")
    else :
        print("invlaid marks !")
            
    print("------ Student Information --------")
    print("Student RollNo: ", rollNo)
    print("Student Name: ", name)
    print("Studetn Age: ", age)

stu_information()




        
        
       
        
    




