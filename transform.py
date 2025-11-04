# src/transform.py
import numpy as np

def select_rows(data, condition):
    """Filter rows based on a Python expression (e.g. section=='A')."""
    try:
        mask = np.array([eval(condition, {}, dict(zip(data.dtype.names, row))) for row in data])
        return data[mask]
    except Exception:
        print("❌ Invalid condition.")
        return data

def project_columns(data, columns):
    """Display specific columns."""
    valid_cols = [c for c in columns if c in data.dtype.names]
    print(data[valid_cols])

def sort_data(data, column):
    """Sort by a given column."""
    if column not in data.dtype.names:
        print("❌ Invalid column.")
        return data
    return np.sort(data, order=column)

def insert_row(data):
    """Insert a new row manually."""
    values = []
    for name in data.dtype.names:
        val = input(f"Enter {name}: ")
        if data[name].dtype.kind == "f":
            val = float(val) if val else np.nan
        values.append(val)
    return np.append(data, np.array([tuple(values)], dtype=data.dtype))

def delete_row(data, student_id):
    """Delete row with matching student_id."""
    mask = data["student_id"] != student_id
    if np.all(mask):
        print("❌ ID not found.")
    return data[mask]
