import tkinter as tk
from tkinter import messagebox
from statistics import mode, StatisticsError, stdev


class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Examination Results")

        self.students = []

        # Name label and entry
        tk.Label(root, text="Name:").grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        # Marks labels and entries
        tk.Label(root, text="Math marks:").grid(row=1, column=0)
        self.math_entry = tk.Entry(root)
        self.math_entry.grid(row=1, column=1)

        tk.Label(root, text="English marks:").grid(row=2, column=0)
        self.english_entry = tk.Entry(root)
        self.english_entry.grid(row=2, column=1)

        tk.Label(root, text="Computer marks:").grid(row=3, column=0)
        self.comp_entry = tk.Entry(root)
        self.comp_entry.grid(row=3, column=1)

        # Buttons
        tk.Button(root, text="Next", command=self.add_student).grid(row=4, column=0)
        tk.Button(root, text="Close", command=root.quit).grid(row=4, column=1)
        tk.Button(root, text="Highest total", command=self.display_highest_total).grid(row=0, column=3)
        tk.Button(root, text="Least total", command=self.display_least_total).grid(row=1, column=3)
        tk.Button(root, text="Print pass", command=self.display_pass_students).grid(row=2, column=3)
        tk.Button(root, text="Print fail", command=self.display_fail_students).grid(row=3, column=3)

    def add_student(self):
        name = self.name_entry.get()
        math_marks = int(self.math_entry.get())
        english_marks = int(self.english_entry.get())
        comp_marks = int(self.comp_entry.get())
        total_marks = math_marks + english_marks + comp_marks
        self.students.append({
            "name": name,
            "math_marks": math_marks,
            "english_marks": english_marks,
            "comp_marks": comp_marks,
            "total_marks": total_marks
        })
        # Clear the entry boxes
        self.name_entry.delete(0, tk.END)
        self.math_entry.delete(0, tk.END)
        self.english_entry.delete(0, tk.END)
        self.comp_entry.delete(0, tk.END)
        messagebox.showinfo("Info", f"Record added for {name}")

    def display_highest_total(self):
        if self.students:
            highest = max(self.students, key=lambda x: x["total_marks"])
            messagebox.showinfo("Highest Total",
                                f"Highest total marks: {highest['total_marks']} (Student: {highest['name']})")
        else:
            messagebox.showwarning("Warning", "No student records available.")

    def display_least_total(self):
        if self.students:
            least = min(self.students, key=lambda x: x["total_marks"])
            messagebox.showinfo("Least Total", f"Least total marks: {least['total_marks']} (Student: {least['name']})")
        else:
            messagebox.showwarning("Warning", "No student records available.")

    def display_pass_students(self):
        pass_students = [s for s in self.students if (s["total_marks"] / 3) >= 50]
        if pass_students:
            result = "\n".join([f"Name: {s['name']}, Total Marks: {s['total_marks']}" for s in pass_students])
            messagebox.showinfo("Pass Students", f"Students with average marks >= 50 (Pass):\n{result}")
        else:
            messagebox.showinfo("Pass Students", "No students with average marks >= 50.")

    def display_fail_students(self):
        fail_students = [s for s in self.students if (s["total_marks"] / 3) < 50]
        if fail_students:
            result = "\n".join([f"Name: {s['name']}, Total Marks: {s['total_marks']}" for s in fail_students])
            messagebox.showinfo("Fail Students", f"Students with average marks < 50 (Fail):\n{result}")
        else:
            messagebox.showinfo("Fail Students", "No students with average marks < 50.")


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()
