# Student Information System

# Create variables to store student information 

print("\n=======================================")
print(f"         Student Inforamtion            ")
print("=======================================\n")


rollNo = int(input("Enter student Roll No : "))
name = input("Enter student Name :  ")
age = int(input("Enter student Age : "))


# Storing marks for three different subjects
print("\n=======================================")
print(f"        Enter Subject Marks             ")
print("=======================================\n")
    
java = eval(input("Enter Java Marks: "))
python = eval(input("Enter Python Marks: "))
dbms = eval(input("Enter DBMS marks: "))


# Arithmetic Operations

# Calculating total marks and percentage

totalMarks = java + python + dbms
percentage = (totalMarks / 300) * 100

# Logical Operations & conditions

if (java >= 40 and python >= 40 and dbms >= 40):
    result = "Passed"

elif (java < 40 or python < 40 or dbms < 40):
    result = "Failed"

else : 
    print("Invalid Marks !)")


# Formatted output

print("\n=======================================")
print(f"         Student Report Card            ")
print("=======================================\n")
print(f"Roll No      : {rollNo}")
print(f"Name         : {name}")
print(f"Age          : {age}")
print(f"Total Marks  : {totalMarks}")
print(f"Percentage   : {percentage:.2f}%")
print(f"Result Status: {result}")
print("\n=======================================")







        
        
       
        
    




