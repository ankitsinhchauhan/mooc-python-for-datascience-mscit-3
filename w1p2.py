# Student Marks Analysis

print("\n========== Student Marks Analysis ===========\n")

stu_list = ["Ramesh", "Suresh", "Deep", "Meet", "Ravi", "Kiran", "Nilesh", "Rohit", "Sunil", "Rakesh"]
marks_list = [65, 76, 99, 24, 76, 34, 77, 88, 76, 90]
    
# Student Name and Marks List
print("\n----- Student Name and Marks List ------\n")
print(stu_list)
print(marks_list)

 # convert list to tuple

print("\n ------- Convert List To Tuple -------\n")
convert_tuple = tuple(zip(stu_list, marks_list))
print(type(convert_tuple))

# Store Student Name and Marks in Dictionary
print("\n-------- Store Student Name and Marks in Dictionary --------\n")
dict_student = dict(student=stu_list, marks=marks_list)
print(dict_student)

# Find the student highest, lowest and average marks
print("\n----- Find the student highest, lowest and average marks ------\n")

highest_marks = max(marks_list)
lowest_marks = min(marks_list)
average_marks = sum(marks_list) / len(marks_list)

print(f"Highest Marks: {highest_marks}")
print(f"Lowest Marks: {lowest_marks}")
print(f"Average Marks: {average_marks:.2f}%")

# Display students above average marks
print("\n----- Display students above average marks ------\n")

for i in range(len(marks_list)):
    if marks_list[i] > average_marks:
        print(f"{stu_list[i]} : {marks_list[i]}")


# Remove duplicate marks using set

print("\n----- Remove duplicate marks using set ------\n")
unique_marks = set(marks_list)
print(unique_marks)
