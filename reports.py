# src/reports.py
import csv
import numpy as np

def print_summary(data):
    """Print basic summary by section."""
    print("\n📋 Summary by Section")
    sections = np.unique(data["section"])
    for sec in sections:
        sec_rows = data[data["section"] == sec]
        avg = np.nanmean(sec_rows["weighted_grade"])
        print(f"Section {sec}: {len(sec_rows)} students, Avg Grade = {avg:.2f}")

def export_per_section(data):
    """Export each section’s data to its own CSV."""
    for sec in np.unique(data["section"]):
        subset = data[data["section"] == sec]
        filename = f"section_{sec}.csv"
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(subset.dtype.names)
            writer.writerows(subset.tolist())
        print(f"💾 Exported {filename}")

def generate_at_risk_list(data, threshold=75.0):
    """Generate list of at-risk students below threshold."""
    at_risk = data[data["weighted_grade"] < threshold]
    print(f"\n⚠️ {len(at_risk)} student(s) are at risk (grade < {threshold}).")
    if len(at_risk):
        for r in at_risk:
            print(f"{r['student_id']} - {r['weighted_grade']:.2f}")
