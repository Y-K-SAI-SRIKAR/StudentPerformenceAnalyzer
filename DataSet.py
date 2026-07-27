# Numpy Mini Project:
# Data Set Creating :
import numpy as np

#data set cols:
headers = np.array([
    "RollNo",
    "Math",
    "Python",
    "DSA",
    "OOP",
    "SystemDesign",
    "Attendance"
])

np.random.seed(42)

#data set rows:
roll_no = np.arange(1,101)
math_marks = np.random.randint(20,101,100)
python_marks = np.random.randint(20,101,100)
dsa_marks = np.random.randint(20,101,100)
oop_marks = np.random.randint(20,101,100)
system_design_marks = np.random.randint(15,101,100)
attendance = np.random.randint(60,101,100)

#Combined Data Set:
StudentsDataSet = np.column_stack((roll_no,
                                   math_marks,
                                   python_marks,
                                   dsa_marks,
                                   oop_marks,
                                   system_design_marks,
                                   attendance))

#saving Data as npy file:
np.save('StudentData.npy',StudentsDataSet)
print(".Npy file Created Successfully")

#saving as a zip file:
np.savez('StudentData.npz',index=headers,data=StudentsDataSet)
print(".Npz file Created Successfully")

#<<<<<<<< ------- created on 26-07-2026 @ 23:00 ------- >>>>>>>> < Author : Srikar Yerraguntla >