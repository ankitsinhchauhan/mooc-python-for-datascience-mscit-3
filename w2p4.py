
# Advanced Student Performance Analytics System

import numpy as np

# ========= 1. Batch and Student Inforamtion ============

batch_name = input("Enter Batch Name: ").strip()

# Extracting department name
dept_name = batch_name.split("-")[-1].replace("_", " ")

subjects = ("Math", "Python", "Java", "DBMS", "PHP")   
students = ["Deep", "Ramesh", "Suresh", "Meet", "Ravi", "Karan", "Jeet", "Ritesh", "Mahesh", "Nilesh"]

roll_numbers = list(range(1, len(students) + 1))

print("------ Roll Numbers and Students ------")
for rollNo, name in zip(roll_numbers, students):
    print(f"Roll No: {rollNo} | Name: {name}")

# Taking marks with 0 to 100 validation
marks_list = []
print("\nEnter marks (0 to 100) for all 5 subjects:")

for rollname in students:
    print(f"\nFor {rollname}: ")
    student_marks = []
    for sub in subjects:
        while True:
            mark = float(input(f"  {sub}: "))
            if 0 <= mark <= 100:
                student_marks.append(mark)
                break
            else:
                print("Invalid input! Marks must be between 0 and 100.")
    marks_list.append(student_marks)

marks_matrix = np.array(marks_list)


# ======= 2. Academic Performance Analysis =========

total_marks = np.sum(marks_matrix, axis=1)
percentage = (total_marks / (len(subjects) * 100)) * 100

subject_avg = np.mean(marks_matrix, axis=0)

global_lowest = np.min(marks_matrix)
global_highest = np.max(marks_matrix)

top_student_index = np.argmax(total_marks)
bottom_student_index = np.argmin(total_marks)

class_avg_percentage = np.mean(percentage)

best_sub_index = np.argmax(subject_avg)
worst_sub_index = np.argmin(subject_avg)

# Slicing first 3 students and last 2 subjects
sliced_marks = marks_matrix[0:3, -2:]


# ======= 3. Student Performance Analytics ==========

print("\n---- Subject Verification Check -----\n")
search_sub = input("Enter subject name to search: ").strip()

if search_sub in subjects:
    subject_idx = subjects.index(search_sub)
    print(f" '{search_sub}' is valid. Index: {subject_idx}")
else:
    print(f" '{search_sub}' does not exist.")

# Filtering distinction and failed profiles
distinction_list = []
failed_list = []

for i in range(len(students)):
    if percentage[i] >= 85:
        distinction_list.append(students[i])

    for mark in marks_matrix[i]:
        if mark < 40:
            failed_list.append(students[i])
            break

print("\n---- Performance Filters ----")
print("Students above class average percentage: ")

for i in range(len(students)):
    if percentage[i] > class_avg_percentage:
        print(f"{students[i]} ({percentage[i]:.1f}%)")

# Sorting and reversing while preserving original list
reversed_students = list(reversed(students))
alpha_students = sorted(students)

print("\nReversed Student List (Original preserved):", reversed_students)
print("Alphabetical Student List (Original preserved):", alpha_students)

print("\nFirst 3 Students Marks in Last 2 Subjects Slicing:")
print(sliced_marks)

# ========= 4. Summary Report ===========

print("\n==================================================")
print("           ACADEMIC PERFORMANCE SUMMARY             ")
print("==================================================\n")
print(f"Batch Name                  : {batch_name}")
print(f"Department Name             : {dept_name}")
print(f"Total Number of Students    : {len(students)}")
print(f"Overall Class Average       : {class_avg_percentage:.2f}%")
print(f"Highest Scoring Student     : {students[top_student_index]} ({total_marks[top_student_index]} Marks)")
print(f"Lowest Scoring Student      : {students[bottom_student_index]} ({total_marks[bottom_student_index]} Marks)")
print(f"Subject with Highest Average: {subjects[best_sub_index]} (Avg: {subject_avg[best_sub_index]:.2f})")
print(f"Subject with Lowest Average : {subjects[worst_sub_index]} (Avg: {subject_avg[worst_sub_index]:.2f})")
print(f"Number of Distinction Holders: {len(distinction_list)}")
print(f"Number of Failed Students   : {len(failed_list)}")
print("\n==================================================\n")
