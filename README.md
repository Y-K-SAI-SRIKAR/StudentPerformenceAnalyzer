# Student Performance Analyzer

## Overview

The Student Performance Analyzer is a Python-based mini project developed using the NumPy library. The project analyzes the academic performance of a class by processing student marks and attendance stored in a NumPy dataset.

It demonstrates how NumPy can be used to perform statistical analysis, data manipulation, sorting, filtering, and conditional operations on structured data.

This project was developed as part of my NumPy learning journey to apply theoretical concepts in a practical scenario.

---

## Features

- Generates and loads student datasets using NumPy.
- Displays complete student records.
- Calculates subject-wise statistics:
  - Highest Marks
  - Lowest Marks
  - Average Marks
  - Median
  - Standard Deviation
- Calculates overall class average for each subject.
- Calculates average attendance of the class.
- Generates pass/fail reports.
- Assigns grades based on average marks.
- Determines scholarship eligibility using attendance and academic performance.
- Generates subject-wise pass/fail status.
- Generates attendance status.
- Produces a complete class ranking based on average marks.

---

## Technologies Used

- Python 3
- NumPy

---

## NumPy Concepts Used

The project makes use of several important NumPy operations, including:

- Array Creation
- Array Indexing and Slicing
- Boolean Masking
- Statistical Functions
  - `np.mean()`
  - `np.average()`
  - `np.median()`
  - `np.std()`
  - `np.amax()`
  - `np.amin()`
- Conditional Operations
  - `np.where()`
  - `np.select()`
- Sorting
  - `np.argsort()`
- Array Combination
  - `np.column_stack()`
- Dataset Storage
  - `np.save()`
  - `np.savez()`

---

## Project Structure

```
Student-Performance-Analyzer/
│
├── DataSet.py
├── Analyzer.py
├── StudentData.npy
├── StudentData.npz
└── README.md
```

---

## Dataset

The dataset contains information for 100 students.

Each record consists of:

- Roll Number
- Mathematics Marks
- Python Marks
- Data Structures Marks
- Object-Oriented Programming Marks
- System Design Marks
- Attendance Percentage

The dataset is generated using NumPy and stored in both `.npy` and `.npz` formats.

---

## Analysis Performed

The analyzer performs the following operations:

- Subject-wise statistical analysis
- Overall class statistics
- Student average calculation
- Grade generation
- Pass/Fail analysis
- Scholarship eligibility analysis
- Subject-wise result generation
- Attendance analysis
- Complete class ranking

---

## How to Run

1. Clone the repository.

```
git clone https://github.com/Y-K-SAI-SRIKAR/StudentPerformenceAnalyzer
```

2. Navigate to the project folder.

```
cd Student-Performance-Analyzer
```

3. Install NumPy.

```
pip install numpy
```

4. Generate the dataset (if required).

```
python DataSet.py
```

5. Run the analyzer.

```
python Analyzer.py
```

---

## Learning Outcomes

Through this project, I gained practical experience with:

- Working with multidimensional NumPy arrays.
- Applying statistical functions on real datasets.
- Using boolean indexing for filtering data.
- Performing conditional operations with NumPy.
- Sorting and ranking records using `np.argsort()`.
- Organizing and analyzing structured datasets.
- Building a complete mini project using NumPy.

---

## Future Improvements

Possible future enhancements include:

- Exporting reports to CSV or Excel.
- Generating visualizations using Matplotlib.
- Searching student records by roll number.
- Interactive menu-driven interface.
- Semester-wise comparison of student performance.
- Graphical dashboard for analysis.

---

## Author

**Srikar Yerraguntla**

This project was developed as a personal learning project to strengthen my understanding of NumPy by applying its concepts to a practical student performance analysis system.
