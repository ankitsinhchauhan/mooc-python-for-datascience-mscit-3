# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 17:19:26 2026

@author: Ankitsinh
"""

# Student Marks Analysis



student_dict = dict();

stu_list = []
marks_list = []

for x in range(0, 10):
    
    
    # Enter Student name and marks
    
    stu_name = input("Enter student name: ")
    stu_marks = int(input("Enter student marks: "))
    
    stu_list.append(stu_name)
    marks_list.append(stu_marks)
 
    
# Student Name and Marks List
print("\n----- Student Name and Marks List ------\n")
print(stu_list)
print(marks_list)


