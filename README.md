# Student Performance Data Analyzer

A Python tool that analyzes student academic records from a CSV file and generates summary statistics and visualizations using **pandas** and **matplotlib**.

## Features

- **Automatic Calculations** — computes total marks, average, and letter grade for each student
- **Class Summary Statistics** — class average, highest/lowest performer, per-subject averages
- **Grade Distribution** — counts how many students fall into each grade band (A–F)
- **Top Performers** — automatically ranks and displays the top 3 students
- **Data Visualization** — generates a bar chart of subject averages and a pie chart of grade distribution
- **Report Export** — saves a processed, sorted CSV report with all computed columns
- **Error Handling** — gracefully handles missing files, empty files, or missing columns

## Why I Built This

As someone aiming to become a data scientist, I wanted hands-on practice with the tools used daily in the field — pandas for data manipulation and matplotlib for visualization. This project simulates a real use case: turning raw academic records into meaningful insights and visuals.

## Tech Used

- **Language:** Python 3
- **Libraries:** pandas, matplotlib
- **Concepts:** Data cleaning, vectorized operations, aggregation, data visualization, CSV I/O, error handling

## How to Run

### Requirements
- Python 3 installed
- pandas and matplotlib libraries

Install the required libraries:

```bash
pip install pandas matplotlib
```

### Run the script

```bash
python student_performance_analyzer.py students.csv
```

This will:
1. Print a full class summary to the console
2. Save `subject_averages.png` (bar chart)
3. Save `grade_distribution.png` (pie chart)
4. Save `student_report.csv` (sorted report with total/average/grade columns)

## Sample Output
