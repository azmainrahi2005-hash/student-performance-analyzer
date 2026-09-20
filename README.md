Student Performance Data Analyzer

A Python tool that analyzes student academic records from a CSV file and generates summary statistics and visualizations using pandas and matplotlib.

Features
Automatic Calculations — computes total marks, average, and letter grade for each student
Class Summary Statistics — class average, highest/lowest performer, per-subject averages
Grade Distribution — counts how many students fall into each grade band (A–F)
Top Performers — automatically ranks and displays the top 3 students
Data Visualization — generates a bar chart of subject averages and a pie chart of grade distribution
Report Export — saves a processed, sorted CSV report with all computed columns
Error Handling — gracefully handles missing files, empty files, or missing columns
Why I Built This

As someone aiming to become a data scientist, I wanted hands-on practice with the tools used daily in the field — pandas for data manipulation and matplotlib for visualization. This project simulates a real use case: turning raw academic records into meaningful insights and visuals.

Tech Used
Language: Python 3
Libraries: pandas, matplotlib
Concepts: Data cleaning, vectorized operations, aggregation, data visualization, CSV I/O, error handling
How to Run
Requirements
Python 3 installed
pandas and matplotlib libraries

Install the required libraries:

pip install pandas matplotlib

Run the script:

python student_performance_analyzer.py students.csv

This will:

Print a full class summary to the console
Save subject_averages.png (bar chart)
Save grade_distribution.png (pie chart)
Save student_report.csv (sorted report with total/average/grade columns)
Sample Output
===== Class Summary =====
Number of students : 10
Class average      : 78.46
Highest average    : 91.40 (Ahmed Khan)
Lowest average     : 58.00 (Carlos Ruiz)

----- Per-Subject Averages -----
Math              : 77.40
Physics           : 78.60
Chemistry         : 75.20
English           : 80.70
Computer_Science  : 80.40

----- Grade Distribution -----
A: 5 student(s)
B: 2 student(s)
C: 2 student(s)
D: 1 student(s)

----- Top 3 Performers -----
Ahmed Khan — avg 91.40 (A)
Aisha Rahman — avg 91.00 (A)
Wei Chen — avg 89.80 (A)
Sample Data Format

The input CSV should have these columns:

id,name,math,physics,chemistry,english,computer_science
101,John Doe,85,90,78,88,92
Possible Future Improvements
Add command-line flags for custom subject lists
Support multiple classes/terms for trend analysis over time
Build an interactive dashboard (e.g., using Streamlit)
Add unit tests for grade calculation logic
Author
MD RAHI CHOWDHURY
