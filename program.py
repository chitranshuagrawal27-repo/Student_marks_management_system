import tkinter as tk
from tkinter import messagebox

subjects = ["Mathematics", "CSE", "ETC", "EVS"]

students = []

BACKGROUND = "#DCEEFF"
DARK_BLUE = "#1F4E78"
BUTTON_BLUE = "#2E75B6"
WHITE = "#FFFFFF"

root = tk.Tk()
root.title("Student Marks Management System")
root.geometry("750x680")
root.configure(bg=BACKGROUND)

title = tk.Label(
    root,
    text="STUDENT MARKS MANAGEMENT SYSTEM",
    font=("Arial", 20, "bold"),
    fg=DARK_BLUE,
    bg=BACKGROUND
)

title.pack(pady=20)

tk.Label(
    root,
    text="Student Name",
    font=("Arial", 11, "bold"),
    bg=BACKGROUND,
    fg=DARK_BLUE
).pack()

name_entry = tk.Entry(
    root,
    width=35,
    font=("Arial", 11)
)

name_entry.pack(pady=5)

tk.Label(
    root,
    text="Enter Marks",
    font=("Arial", 13, "bold"),
    bg=BACKGROUND,
    fg=DARK_BLUE
).pack(pady=15)


marks_entries = {}


for subject in subjects:

    frame = tk.Frame(
        root,
        bg=BACKGROUND
    )

    frame.pack(pady=5)

    tk.Label(
        frame,
        text=subject,
        width=15,
        font=("Arial", 10, "bold"),
        bg=BACKGROUND,
        fg=DARK_BLUE
    ).pack(side="left")

    tk.Label(
        frame,
        text="CAT 1",
        bg=BACKGROUND
    ).pack(side="left")

    cat1 = tk.Entry(
        frame,
        width=7
    )

    cat1.pack(side="left", padx=5)

    tk.Label(
        frame,
        text="CAT 2",
        bg=BACKGROUND
    ).pack(side="left")

    cat2 = tk.Entry(
        frame,
        width=7
    )

    cat2.pack(side="left", padx=5)

    tk.Label(
        frame,
        text="Term",
        bg=BACKGROUND
    ).pack(side="left")

    term = tk.Entry(
        frame,
        width=7
    )

    term.pack(side="left", padx=5)

    marks_entries[subject] = (cat1, cat2, term)

def clear_fields():

    name_entry.delete(0, tk.END)

    for subject in subjects:

        for entry in marks_entries[subject]:
            entry.delete(0, tk.END)

def add_student():

    if len(students) >= 60:

        messagebox.showerror(
            "Limit Reached",
            "Maximum 60 students can be added."
        )

        return

    name = name_entry.get()

    if name == "":

        messagebox.showerror(
            "Error",
            "Please enter student name."
        )

        return

    student = {
        "name": name,
        "marks": {}
    }

    try:

        for subject in subjects:

            cat1 = float(
                marks_entries[subject][0].get()
            )

            cat2 = float(
                marks_entries[subject][1].get()
            )

            term = float(
                marks_entries[subject][2].get()
            )

            
            if not (
                0 <= cat1 <= 100
                and 0 <= cat2 <= 100
                and 0 <= term <= 100
            ):

                messagebox.showerror(
                    "Invalid Marks",
                    "Marks should be between 0 and 100."
                )

                return

        
            final_marks = (
                cat1 + cat2 + term
            ) / 3

            student["marks"][subject] = {

                "CAT1": cat1,

                "CAT2": cat2,

                "Term": term,

                "Final": final_marks
            }

        

        total = 0
        failed = False

        for subject in subjects:

            final_marks = (
                student["marks"][subject]["Final"]
            )

            total = total + final_marks

            if final_marks < 40:
                failed = True

        student["total"] = total

        student["average"] = (
            total / len(subjects)
        )

        if failed:

            student["result"] = "FAIL"

        else:

            student["result"] = "PASS"

        

        students.append(student)

        messagebox.showinfo(
            "Success",
            "Student added successfully!"
        )

        clear_fields()

        counter_label.config(
            text="Students Added: "
            + str(len(students))
            + " / 60"
        )

    except ValueError:

        messagebox.showerror(
            "Error",
            "Please enter valid marks."
        )



def view_students():

    if len(students) == 0:

        messagebox.showinfo(
            "Students",
            "No students have been added."
        )

        return

    window = tk.Toplevel(root)

    window.title("All Student Results")

    window.geometry("750x600")

    window.configure(bg=BACKGROUND)

    text = tk.Text(
        window,
        width=85,
        height=30,
        font=("Arial", 10)
    )

    text.pack(
        padx=10,
        pady=10
    )

    for student in students:

        text.insert(
            tk.END,
            "\nName: "
            + student["name"]
            + "\n"
        )

        for subject in subjects:

            final_marks = (
                student["marks"]
                [subject]["Final"]
            )

            text.insert(
                tk.END,
                subject
                + ": "
                + str(round(final_marks, 2))
                + "\n"
            )

        text.insert(
            tk.END,
            "Total: "
            + str(round(student["total"], 2))
            + "\n"
        )

        text.insert(
            tk.END,
            "Average: "
            + str(round(student["average"], 2))
            + "\n"
        )

        text.insert(
            tk.END,
            "Result: "
            + student["result"]
            + "\n"
        )

        text.insert(
            tk.END,
            "--------------------------------\n"
        )



def find_topper():

    if len(students) == 0:

        messagebox.showinfo(
            "Topper",
            "No students have been added."
        )

        return

    topper = None

    for student in students:

        if student["result"] == "PASS":

            if topper is None:

                topper = student

            elif (
                student["average"]
                > topper["average"]
            ):

                topper = student

    if topper is None:

        messagebox.showinfo(
            "Topper",
            "No student has passed."
        )

    else:

        messagebox.showinfo(
            "Topper",
            "Name: "
            + topper["name"]
            + "\nAverage: "
            + str(
                round(
                    topper["average"],
                    2
                )
            )
        )


def class_statistics():

    if len(students) == 0:

        messagebox.showinfo(
            "Statistics",
            "No students have been added."
        )

        return

    pass_count = 0
    fail_count = 0
    total_average = 0

    for student in students:

        total_average = (
            total_average
            + student["average"]
        )

        if student["result"] == "PASS":

            pass_count += 1

        else:

            fail_count += 1

    class_average = (
        total_average / len(students)
    )

    messagebox.showinfo(
        "Class Statistics",

        "Total Students: "
        + str(len(students))

        + "\nPassed Students: "
        + str(pass_count)

        + "\nFailed Students: "
        + str(fail_count)

        + "\nClass Average: "
        + str(round(class_average, 2))
    )



def failed_students():

    failed = []

    for student in students:

        if student["result"] == "FAIL":

            failed.append(
                student["name"]
            )

    if len(failed) == 0:

        messagebox.showinfo(
            "Failed Students",
            "No failed students."
        )

    else:

        result = "Failed Students:\n\n"

        for name in failed:

            result = result + name + "\n"

        messagebox.showinfo(
            "Failed Students",
            result
        )



button_frame = tk.Frame(
    root,
    bg=BACKGROUND
)

button_frame.pack(pady=20)


tk.Button(
    button_frame,
    text="Add Student",
    width=18,
    bg=BUTTON_BLUE,
    fg=WHITE,
    font=("Arial", 10, "bold"),
    command=add_student
).grid(
    row=0,
    column=0,
    padx=7,
    pady=7
)


tk.Button(
    button_frame,
    text="View All Students",
    width=18,
    bg=BUTTON_BLUE,
    fg=WHITE,
    font=("Arial", 10, "bold"),
    command=view_students
).grid(
    row=0,
    column=1,
    padx=7,
    pady=7
)


tk.Button(
    button_frame,
    text="Find Topper",
    width=18,
    bg=BUTTON_BLUE,
    fg=WHITE,
    font=("Arial", 10, "bold"),
    command=find_topper
).grid(
    row=1,
    column=0,
    padx=7,
    pady=7
)


tk.Button(
    button_frame,
    text="Class Statistics",
    width=18,
    bg=BUTTON_BLUE,
    fg=WHITE,
    font=("Arial", 10, "bold"),
    command=class_statistics
).grid(
    row=1,
    column=1,
    padx=7,
    pady=7
)


tk.Button(
    button_frame,
    text="Failed Students",
    width=18,
    bg=BUTTON_BLUE,
    fg=WHITE,
    font=("Arial", 10, "bold"),
    command=failed_students
).grid(
    row=2,
    column=0,
    padx=7,
    pady=7
)


tk.Button(
    button_frame,
    text="Clear",
    width=18,
    bg=BUTTON_BLUE,
    fg=WHITE,
    font=("Arial", 10, "bold"),
    command=clear_fields
).grid(
    row=2,
    column=1,
    padx=7,
    pady=7
)


counter_label = tk.Label(
    root,
    text="Students Added: 0 / 60",
    font=("Arial", 11, "bold"),
    fg=DARK_BLUE,
    bg=BACKGROUND
)

counter_label.pack(pady=10)

footer = tk.Label(
    root,
    text="Python + Tkinter Student Project",
    font=("Arial", 9),
    fg=DARK_BLUE,
    bg=BACKGROUND
)

footer.pack(
    side="bottom",
    pady=10
)

root.mainloop()
