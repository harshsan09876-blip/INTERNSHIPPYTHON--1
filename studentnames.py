# Day 9 - Student Record Program
# Veda Technology Python Internship

# Store student names and marks in lists
student_names = ["Harsh", "Aman", "Riya", "Priya", "Rahul"]
student_marks = [85, 72, 91, 68, 78]

print("===== STUDENT RECORD SYSTEM =====")

# Display student records
print("\nStudent Records:")

for i in range(len(student_names)):
    print(student_names[i], ":", student_marks[i])

# Search for a student
search_name = input("\nEnter student name to search: ")

if search_name in student_names:
    index = student_names.index(search_name)
    print(search_name, "scored", student_marks[index], "marks.")
else:
    print("Student not found.")

# Find highest score
highest_score = max(student_marks)
highest_index = student_marks.index(highest_score)

print("\nHighest Score:")
print(student_names[highest_index], ":", highest_score)

# Find lowest score
lowest_score = min(student_marks)
lowest_index = student_marks.index(lowest_score)

print("\nLowest Score:")
print(student_names[lowest_index], ":", lowest_score)

# Sort students according to marks
sorted_records = sorted(
    zip(student_names, student_marks),
    key=lambda student: student[1],
    reverse=True
)

print("\nStudents Sorted by Marks (Highest to Lowest):")

for name, marks in sorted_records:
    print(name, ":", marks)