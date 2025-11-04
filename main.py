# src/main.py
import numpy as np
from ingest import load_csv
from transform import select_rows, project_columns, sort_data, insert_row, delete_row
from analyze import compute_weighted_grades, grade_distribution, find_outliers, track_improvements
from reports import print_summary, export_per_section, generate_at_risk_list


def main_menu():
    data = None

    while True:
        print("\n=== STUDENT GRADE MANAGEMENT MENU ===")
        print("1. Load & Validate CSV")
        print("2. View / Select / Sort Data")
        print("3. Compute Analytics (Grades, Distributions, Outliers)")
        print("4. Generate Reports (Summaries & At-Risk Lists)")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            path = input("Enter CSV file path: ").strip()
            data = load_csv(path)
            if data is not None:
                print(f"✅ Loaded {len(data)} valid rows.")
        elif choice == "2":
            if data is None:
                print("⚠️ Load data first.")
                continue
            print("\na) Select rows")
            print("b) Project columns")
            print("c) Sort data")
            print("d) Insert row")
            print("e) Delete row")
            sub = input("Choose operation: ").lower().strip()
            if sub == "a":
                cond = input("Enter condition (e.g. section=='A'): ")
                data = select_rows(data, cond)
            elif sub == "b":
                cols = input("Enter columns (comma-separated): ").split(",")
                project_columns(data, [c.strip() for c in cols])
            elif sub == "c":
                col = input("Sort by column: ")
                data = sort_data(data, col)
            elif sub == "d":
                insert_row(data)
            elif sub == "e":
                sid = input("Enter student_id to delete: ")
                data = delete_row(data, sid)
        elif choice == "3":
            if data is None:
                print("⚠️ Load data first.")
                continue
            weighted = compute_weighted_grades(data)
            grade_distribution(weighted)
            find_outliers(weighted)
            track_improvements(weighted)
            data = weighted
        elif choice == "4":
            if data is None:
                print("⚠️ Load data first.")
                continue
            print_summary(data)
            export_per_section(data)
            generate_at_risk_list(data)
        elif choice == "5":
            print("👋 Exiting program.")
            break
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main_menu()
