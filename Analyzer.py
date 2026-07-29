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

#Marks calculation:
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
average_math_mark = np.average(students[:,MATH],axis=0)
average_Python_mark = np.average(students[:,PYTHON],axis=0)
average_Dsa_mark = np.average(students[:,DSA],axis=0)
average_Oop_mark = np.average(students[:,OOP],axis=0)
average_Sd_mark = np.average(students[:,SYSTEM_DESIGN],axis=0)
median_Math_mark = np.median(students[:,MATH])
median_Python_mark = np.median(students[:,PYTHON])
median_Dsa_mark = np.median(students[:,DSA])
median_Oop_mark = np.median(students[:,OOP])
median_Sd_mark = np.median(students[:,SYSTEM_DESIGN])
deviation_Math_mark = np.std(students[:,MATH])
deviation_Python_mark = np.std(students[:,PYTHON])
deviation_Dsa_mark = np.std(students[:,DSA])
deviation_Oop_mark = np.std(students[:,OOP])
deviation_Sd_mark = np.std(students[:,SYSTEM_DESIGN])
Subject_Average_marks_of_Entire_Class = np.mean(students[:,MATH:ATTENDANCE],axis = 0)
Subject_Average_marks_of_Each_students = np.mean(students[:,MATH:ATTENDANCE],axis=1)
Average_attendence_of_class = np.mean(students[:,ATTENDANCE],axis=0)

#Subject Mark Analysis :
print("Total Students:",len(total_students))
print("Total Subjects:",len(total_subjects))
print("-"*50)
print("Subject Wise Analysis :")
print('-'*50)
print("MATH:",'\n')
print("Highest Mark:",highest_Math_mark)
print("Lowest Mark:",lowest_Math_mark)
print("Average Mark:",average_math_mark)
print("Median Mark:",median_Math_mark)
print("Math Standard Deviation Mark:",deviation_Math_mark)
print('-'*50)
print("PYTHON:",'\n')
print("Highest Mark:",highest_Python_mark)
print("Lowest Mark:",lowest_Python_mark)
print("Average Mark:",average_Python_mark)
print("Median Mark:",median_Python_mark)
print("PYTHON Standard Deviation Mark:",deviation_Python_mark)
print('-'*50)
print("DSA:",'\n')
print("Highest Mark:",highest_Dsa_mark)
print("Lowest Mark:",lowest_Dsa_mark)
print("Average Mark:",average_Dsa_mark)
print("Median Mark:",median_Dsa_mark)
print("DSA Standard Deviation Mark:",deviation_Dsa_mark)
print('-'*50)
print("OOP:",'\n')
print("Highest Mark:",highest_Oop_mark)
print("Lowest Mark:",lowest_Oop_mark)
print("Average Mark:",average_Oop_mark)
print("Median Mark:",median_Oop_mark)
print("OOP Standard Deviation Mark:",deviation_Oop_mark)
print('-'*50)
print("SYSTEM DESIGN:",'\n')
print("Highest Mark:",highest_Sd_mark)
print("Lowest Mark:",lowest_Sd_mark)
print("Average Mark:",average_Sd_mark)
print("Median Mark:",median_Sd_mark)
print("SYTEM DESIGN Standard Deviation Mark:",deviation_Sd_mark)
print('-'*50)
print("Class Mark Averages:",Subject_Average_marks_of_Entire_Class)
print("Class Average Attendance:",Average_attendence_of_class)
print('-'*50)

#Pass & Fail Count:
class_averages = Subject_Average_marks_of_Each_students
passed = class_averages[class_averages>=35]
failed = class_averages[class_averages<35]
print('-'*50)
print("Total Passed Students:",len(passed))
print("Total Failed Students:",len(failed),'\n')
print('-'*50)

#Grading:
conds = [
    class_averages >= 90,
    (class_averages >= 80) & (class_averages <= 89),
    (class_averages >= 70) & (class_averages <= 79),
    (class_averages >= 60) & (class_averages <= 69),
    (class_averages >= 50) & (class_averages <= 59),
    (class_averages >= 35) & (class_averages <= 49),
    class_averages < 35
]
choices = ['O','A','B','C','D','E','F']
grds = np.select(conds, choices, default='P')
print('-'*50)
print("Grade Report :")
print('-'*50)
grades = np.column_stack((students[:,ROLL],grds))
print('[Roll No - Grade]')
print(grades)
print('-'*50)

#scholarship Calculation:
combined_attendence_averages = np.column_stack((students[:,ROLL],students[:,ATTENDANCE],class_averages))
cond = [(combined_attendence_averages[:,1]>=65) & (combined_attendence_averages[:,-1]>=55)]
choice = ['Eligible']
res = np.select(cond, choice, default='Not Eligible')
schps = np.column_stack((students[:,ROLL],res))
print("ScholarShip Report:")
print('-'*50)
print(schps)
print('-'*50)

#Subject wise Pass/Fail Report
students_copy = students.astype(str)
result = ["P", "F"]
status = ["Promoted", "Detained"]
math_mask = students[:, MATH] > 35
python_mask = students[:, PYTHON] > 35
dsa_mask = students[:, DSA] > 35
oop_mask = students[:, OOP] > 35
sd_mask = students[:, SYSTEM_DESIGN] > 35
atdn_mask = students[:,ATTENDANCE]>65
students_copy[:, MATH] = np.where(math_mask, result[0], result[1])
students_copy[:, PYTHON] = np.where(python_mask, result[0], result[1])
students_copy[:, DSA] = np.where(dsa_mask, result[0], result[1])
students_copy[:, OOP] = np.where(oop_mask, result[0], result[1])
students_copy[:, SYSTEM_DESIGN] = np.where(sd_mask, result[0], result[1])
students_copy[:,ATTENDANCE] = np.where(atdn_mask,status[0],status[1])
print('-'*50)
print("Student Subject Wise Report:")
print('-'*50)
print(students_copy)
print('-'*50)

#Rankers List:
ranks = np.arange(1,101)
rolls = students[:,ROLL]
marks = class_averages
indices = np.argsort(marks)
ranked_averages=marks[indices][::-1]
rankers_rolls = rolls[indices[::-1]]
rankers_list = np.column_stack((ranks,rankers_rolls,ranked_averages))
print('-'*50)
print("Rankers List of Class:")
print("[Rank - Roll - Avg]")
print('-'*50)
print(rankers_list)
print('-'*50)

#<<<<<<<< ------- Project Finished on 29-07-2026 @ 23:00 ------- >>>>>>>> < Author : Srikar Yerraguntla >