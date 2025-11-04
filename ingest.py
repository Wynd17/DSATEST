
import csv
import numpy as np

REQUIRED_COLS = [
    "student_id", "last_name", "first_name", "section",
    "quiz1", "quiz2", "quiz3", "quiz4", "quiz5",
    "midterm", "final", "attendance_percent"
]

def load_csv(filename):
    """
    Reads CSV, validates numeric ranges and missing values.
    Returns: NumPy structured array with valid rows only.
    """
    valid_rows = []
    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, start=1):
            try:
                student = {k: row.get(k, "").strip() for k in REQUIRED_COLS}

                # Clean and validate numeric fields
                for key in ["quiz1","quiz2","quiz3","quiz4","quiz5","midterm","final","attendance_percent"]:
                    val = student[key]
                    if val == "":
                        student[key] = np.nan
                    else:
                        num = float(val)
                        if not (0 <= num <= 100):
                            raise ValueError
                        student[key] = num

                valid_rows.append(tuple(student.values()))
            except Exception:
                print(f"⚠️ Skipped bad row #{i}: {row}")

    dtype = [(col, "U20") if col in ["student_id","last_name","first_name","section"] else (col, "f8")
             for col in REQUIRED_COLS]
    return np.array(valid_rows, dtype=dtype)
