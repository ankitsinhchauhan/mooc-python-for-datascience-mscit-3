# Student Performance Analytics System

print("\n==== Student Performance Analytics System ====\n")


rollNo_list = []
name_list = []

java_list = []
dbms_list = []
html_list = []
python_list = []
math_list = []

total_marks_list = []
percentage_list = []
grade_list = []

grade_dict = {'A': [], 'B': [], 'C': [], 'D': [], 'F': []}

students = int(input("Enter Number of Student: "))

for x in range(students):
    
    print("----- Enter Student Details -----\n")
    roll_no = int(input("Enter student roll No: "))
    name = input("Enter student name: ")
    print("\n----- Enter Subjects Marks -----\n")
    java = int(input("Enter java marks: "))
    dbms = int(input("Enter dbms marks: "))
    html = int(input("Enter html marks: "))
    python=int(input("Enter python marks: "))
    math = int(input("Enter math marks: "))
    
    rollNo_list.append(roll_no)
    name_list.append(name)
   
    java_list.append(java)
    dbms_list.append(dbms)
    html_list.append(html)
    python_list.append(python)
    math_list.append(math)
 
    total = java + dbms + html + python + math
    percentage = total / 5
    
    if percentage >= 85:
        grade = 'A'
    elif percentage >= 65:
        grade = 'B'
    elif percentage >= 45: 
        grade = 'C'
    elif percentage >= 35:
        grade = 'D'
    else : 
        grade = 'F'

    total_marks_list.append(total)
    percentage_list.append(percentage)

    grade_dict[grade].append(name)

# Class average percentage

total_class_percentage = 0
for p in percentage_list:
    total_class_percentage += p
class_percentage_avg =  total_class_percentage / len(percentage_list)

# Highest and Lowest Score

highest_marks = total_marks_list[0]
lowest_marks = total_marks_list[0]

for t in total_marks_list:
    if t > highest_marks:
        highest_marks = t
    if t < lowest_marks:
        lowest_marks = t

highest_score = []
lowest_score = []

for i in range(len(total_marks_list)):
    if total_marks_list[i] == highest_marks:
        highest_score.append(name_list[i])
    if total_marks_list[i] == lowest_marks:
        lowest_score.append(name_list[i])


# Students scoring above the class average

above_avg_students = []
for i in range(len(percentage_list)):
    if percentage_list[i] > class_percentage_avg:
        above_avg_students.append(name_list[i])


# Students who failed in one or more subjects

fail_students = []
for i in range(len(name_list)):
    if java_list[i] < 35 or dbms_list[i] < 35 or html_list[i] < 35 or python_list[i] < 35 or math_list[i] < 35:
        fail_students.append(name_list[i])

# Create a dictionary where: key  = Grade , value = List of student belonging  to that grade

print("\n------ Grade wise student list -------\n")
print(grade_dict)

# Display the names of students in alphabetical order without modifying the original records.

alphabetical_order = sorted(name_list)
print("\n---- Alphabetical Order of Students ----\n")
print(alphabetical_order)


# Find the second-highest scorer without sorting the entire dataset.

highest = total_marks_list[0]
second_highest = -1
for i in range(len(total_marks_list)):
    if total_marks_list[i] > highest:
        second_highest = highest
        highest = total_marks_list[i]
    elif total_marks_list[i] > second_highest and total_marks_list[i] != highest:
        second_highest = total_marks_list[i]


# Display the subject in which the class has obtained the highest average marks.

java_avg = sum(java_list) / len(java_list)
dbms_avg = sum(dbms_list) / len(dbms_list)
html_avg = sum(html_list) / len(html_list)
python_avg = sum(python_list) / len(python_list)
math_avg = sum(math_list) / len(math_list)

subject_avg_dict = {
    'Java': java_avg,
    'DBMS': dbms_avg,
    'HTML': html_avg,
    'Python': python_avg,
    'Math': math_avg
}

highest_avg_subject = max(subject_avg_dict, key=subject_avg_dict.get)

print("\n--- Highest Average Subject ---")
print(f"Subject with Highest Average: {highest_avg_subject} ({subject_avg_dict[highest_avg_subject]:.2f})")


# Remove duplicate student names (if any) and report the duplicate entries

duplicate_names = []
unique_names = []

for name in name_list:
    if name not in unique_names:
        unique_names.append(name)
    else:
        duplicate_names.append(name)

print("\n---- Duplicate Student Names ----\n")
print(f"Duplicate Names: {duplicate_names}")

print("\n---- Unique Student Names ----\n")
print(f"Unique Names: {unique_names}")
