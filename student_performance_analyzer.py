"""
Student Performance Data Analyzer
----------------------------------
Reads student marks from a CSV file and produces summary statistics
and visualizations using pandas and matplotlib.

Intermediate concepts demonstrated:
    - Reading/cleaning tabular data with pandas
    - Computing derived columns (total, average, grade)
    - Aggregation and groupby operations
    - Data visualization (bar chart + pie chart)
    - Basic error handling and functions
    - Exporting a processed report back to CSV

Usage:
    python student_performance_analyzer.py students.csv
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt

SUBJECT_COLUMNS = ["math", "physics", "chemistry", "english", "computer_science"]


def load_data(filepath: str) -> pd.DataFrame:
    """Load student data from a CSV file, with basic error handling."""
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        print(f"Error: file '{filepath}' not found.")
        sys.exit(1)
    except pd.errors.EmptyDataError:
        print(f"Error: file '{filepath}' is empty.")
        sys.exit(1)

    missing_cols = [c for c in SUBJECT_COLUMNS if c not in df.columns]
    if missing_cols:
        print(f"Error: missing expected columns: {missing_cols}")
        sys.exit(1)

    return df


def compute_results(df: pd.DataFrame) -> pd.DataFrame:
    """Add total, average, and letter-grade columns to the dataframe."""
    df = df.copy()
    df["total"] = df[SUBJECT_COLUMNS].sum(axis=1)
    df["average"] = df[SUBJECT_COLUMNS].mean(axis=1)
    df["grade"] = df["average"].apply(assign_grade)
    return df


def assign_grade(average: float) -> str:
    """Convert a numeric average into a letter grade."""
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def print_summary(df: pd.DataFrame) -> None:
    """Print class-wide and per-subject summary statistics."""
    print("\n===== Class Summary =====")
    print(f"Number of students : {len(df)}")
    print(f"Class average      : {df['average'].mean():.2f}")
    print(f"Highest average    : {df['average'].max():.2f} "
          f"({df.loc[df['average'].idxmax(), 'name']})")
    print(f"Lowest average     : {df['average'].min():.2f} "
          f"({df.loc[df['average'].idxmin(), 'name']})")

    print("\n----- Per-Subject Averages -----")
    for subject in SUBJECT_COLUMNS:
        print(f"{subject.title():<18}: {df[subject].mean():.2f}")

    print("\n----- Grade Distribution -----")
    grade_counts = df["grade"].value_counts().sort_index()
    for grade, count in grade_counts.items():
        print(f"{grade}: {count} student(s)")

    print("\n----- Top 3 Performers -----")
    top3 = df.sort_values("average", ascending=False).head(3)
    for _, row in top3.iterrows():
        print(f"{row['name']} — avg {row['average']:.2f} ({row['grade']})")


def plot_subject_averages(df: pd.DataFrame, output_path: str = "subject_averages.png") -> None:
    """Bar chart comparing average marks across subjects."""
    averages = df[SUBJECT_COLUMNS].mean()

    plt.figure(figsize=(8, 5))
    averages.plot(kind="bar", color="#4C72B0")
    plt.title("Average Marks by Subject")
    plt.ylabel("Average Mark")
    plt.xlabel("Subject")
    plt.xticks(rotation=30, ha="right")
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f"\nSaved chart: {output_path}")


def plot_grade_distribution(df: pd.DataFrame, output_path: str = "grade_distribution.png") -> None:
    """Pie chart showing the distribution of letter grades."""
    grade_counts = df["grade"].value_counts().sort_index()

    plt.figure(figsize=(6, 6))
    plt.pie(
        grade_counts.values,
        labels=grade_counts.index,
        autopct="%1.1f%%",
        startangle=90,
        colors=["#55A868", "#4C72B0", "#DD8452", "#C44E52", "#8172B2"],
    )
    plt.title("Grade Distribution")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f"Saved chart: {output_path}")


def export_report(df: pd.DataFrame, output_path: str = "student_report.csv") -> None:
    """Save the processed dataframe (with total/average/grade) to a new CSV."""
    df_sorted = df.sort_values("average", ascending=False)
    df_sorted.to_csv(output_path, index=False)
    print(f"Saved processed report: {output_path}")


def main():
    filepath = sys.argv[1] if len(sys.argv) > 1 else "students.csv"

    df = load_data(filepath)
    df = compute_results(df)

    print_summary(df)
    plot_subject_averages(df)
    plot_grade_distribution(df)
    export_report(df)


if __name__ == "__main__":
    main()