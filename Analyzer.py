# Student Mark Analysis:
import numpy as np

def show_data(x):
    print("---- Student Data ----")
    print(x['index'])
    print(x['data'])

x = np.load('StudentData.npz')

print("DataSet:")
show_data(x)

#data set cols index:
ROLL = 0
MATH = 1
PYTHON = 2
DSA = 3
OOP = 4
SYSTEM_DESIGN = 5
ATTENDANCE = 6

headers = x['index']
students = x['data']

total_students = students[:,ROLL]
total_subjects = headers[MATH:ATTENDANCE]
highest_Math_mark = np.amax(students[:,MATH])
highest_Python_mark = np.amax(students[:,PYTHON])
highest_Dsa_mark = np.amax(students[:,DSA])
highest_Oop_mark = np.amax(students[:,OOP])
highest_Sd_mark = np.amax(students[:,SYSTEM_DESIGN])
lowest_Math_mark = np.amin(students[:,MATH])
lowest_Python_mark = np.amin(students[:,PYTHON])
lowest_Dsa_mark = np.amin(students[:,DSA])
lowest_Oop_mark = np.amin(students[:,OOP])
lowest_Sd_mark = np.amin(students[:,SYSTEM_DESIGN])
Subject_Average_marks_of_Entire_Class = np.mean(students[:,MATH:ATTENDANCE],axis = 0)
Subject_Average_marks_of_Each_students = np.mean(students[:,MATH:ATTENDANCE],axis=1)
Average_attendence_of_class = np.mean(students[:,ATTENDANCE],axis=0)

print("Total Students:",len(total_students),'\n')
print("Total Subjects:",len(total_subjects),'\n')
print("Math Highest Mark:",highest_Math_mark,'\n')
print("Math Lowest Mark:",lowest_Math_mark,'\n')
print("Python Highest Mark:",highest_Python_mark,'\n')
print("Python Lowest Mark:",lowest_Python_mark,'\n')
print("DSA Highest Mark:",highest_Dsa_mark,'\n')
print("DSA Lowest Mark:",lowest_Dsa_mark,'\n')
print("OOP Highest Mark:",highest_Oop_mark,'\n')
print("OOP Lowest Mark:",lowest_Oop_mark,'\n')
print("SYSTEM DESIGN Highest Mark:",highest_Sd_mark,'\n')
print("SYSTEM DESIGN LOWEST Mark:",lowest_Sd_mark,'\n')
print("Class Mark Averages:",Subject_Average_marks_of_Entire_Class,'\n')
print("Student Mark Averages:",Subject_Average_marks_of_Each_students,'\n')
print("Class Average Attendance:",Average_attendence_of_class,'\n')

#<<<<<<<< ------- completed on 27-07-2026 @ 23:45 ------- >>>>>>>> < Author : Srikar Yerraguntla >