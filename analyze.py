# src/analyze.py
import numpy as np

QUIZ_WEIGHT = 0.20
MIDTERM_WEIGHT = 0.30
FINAL_WEIGHT = 0.40
ATTEND_WEIGHT = 0.10

def compute_weighted_grades(data):
    """Compute weighted grade per student."""
    quiz_avg = np.nanmean([data["quiz1"], data["quiz2"], data["quiz3"], data["quiz4"], data["quiz5"]], axis=0)
    weighted = (
        quiz_avg * QUIZ_WEIGHT +
        data["midterm"] * MIDTERM_WEIGHT +
        data["final"] * FINAL_WEIGHT +
        data["attendance_percent"] * ATTEND_WEIGHT
    )
    return append_column(data, "weighted_grade", weighted)

def grade_distribution(data):
    """Print basic distribution metrics."""
    grades = data["weighted_grade"]
    print("\n📊 Grade Distribution")
    print(f"Mean: {np.nanmean(grades):.2f}")
    print(f"Median: {np.nanmedian(grades):.2f}")
    print(f"Std Dev: {np.nanstd(grades):.2f}")

def find_outliers(data):
    """Detect outliers using IQR."""
    grades = data["weighted_grade"]
    q1, q3 = np.nanpercentile(grades, [25, 75])
    iqr = q3 - q1
    lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    outliers = data[(grades < lower) | (grades > upper)]
    print(f"\n🚨 Found {len(outliers)} outlier(s).")
    if len(outliers):
        print(outliers[["student_id","weighted_grade"]])

def track_improvements(data):
    """Compare midterm vs final for improvement."""
    improved = data[data["final"] > data["midterm"]]
    print(f"\n📈 {len(improved)} students improved in the final exam.")
    if len(improved):
        print(improved[["student_id","midterm","final"]])

def append_column(data, name, values):
    """Add a new column to a structured NumPy array."""
    new_dtype = data.dtype.descr + [(name, "f8")]
    new_data = np.empty(data.shape, dtype=new_dtype)
    for field in data.dtype.names:
        new_data[field] = data[field]
    new_data[name] = values
    return new_data
