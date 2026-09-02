# ============================================================
# Day 10 - Python Lists: Student Records & Logic Building
# Internship: Veda Technology
# ============================================================

# Step 1: Create a list to store student names.
students = ["Harsh", "Mohini", "Kratika", "Chirag", "Deepender"]

# Step 2: Create a second list to store Chemistry marks.
# The index of each mark corresponds to the same student's index.
subject_chemistry = [76, 89, 90, 89, 96]


# Step 3: Display both lists.
print("Students:", students)
print("Chemistry Marks:", subject_chemistry)


# ============================================================
# Step 4: Find the student with the highest marks
# ============================================================

# Logic:
# Start by assuming the first mark is the highest.
# Then compare every mark with the current highest mark.
# If a higher mark is found, update the highest mark
# and store the student at the same index.

highest = subject_chemistry[0]
highest_student = students[0]

for i in range(len(students)):
    if subject_chemistry[i] > highest:
        highest = subject_chemistry[i]
        highest_student = students[i]

print("Highest Marks:", highest)
print("Highest Scoring Student:", highest_student)


# ============================================================
# Step 5: Find the lowest marks
# ============================================================

# Logic:
# Start with the first mark as the lowest.
# Check every mark in the list.
# If the current mark is smaller, update the lowest value.

lowest = subject_chemistry[0]

for mark in subject_chemistry:
    if mark < lowest:
        lowest = mark

print("Lowest Marks:", lowest)


# ============================================================
# Step 6: Count students scoring more than 90
# ============================================================

# Logic:
# Start the counter from 0.
# Check each mark one by one.
# If the mark is greater than 90, increase the counter by 1.

count = 0

for mark in subject_chemistry:
    if mark > 90:
        count = count + 1

print("Students scoring more than 90:", count)


# ============================================================
# Step 7: Display students scoring more than 90
# ============================================================

# Logic:
# Use the same index for both lists.
# Check whether the Chemistry mark is greater than 90.
# If true, print the student name and corresponding marks.

print("Students scoring more than 90:")

for i in range(len(students)):
    if subject_chemistry[i] > 90:
        print(students[i], "-", subject_chemistry[i])


# ============================================================
# Step 8: Search for a student
# ============================================================

# Logic:
# Take the student's name as input.
# Start with found = False.
# Loop through the students list.
# If the entered name matches a student:
#     Set found = True.
#     Display the student's marks.
#     Stop the loop using break.
# If found is still False after the loop,
# display "Student not found".

student = input("Enter student name: ")

found = False

for i in range(len(students)):
    if student == students[i]:
        found = True
        print("Student is found")
        print("Chemistry Marks:", subject_chemistry[i])
        break

if found == False:
    print("Student not found")


# ============================================================
# Step 9: Add a new student using append()
# ============================================================

# Logic:
# append() adds a new element to the end of the list.

students.append("Vikas")

print("After adding Vikas:", students)


# ============================================================
# Step 10: Remove a student using remove()
# ============================================================

# Logic:
# remove() deletes the specified value from the list.

students.remove("Vikas")

print("After removing Vikas:", students)


# ============================================================
# Key Logic Learned
# ============================================================
# 1. Lists store multiple values.
# 2. Index connects related data between two lists.
# 3. for loop checks/processes each element.
# 4. if condition makes decisions.
# 5. A variable such as 'found' can remember a result.
# 6. break stops the loop after finding the required item.
# 7. count = count + 1 is used for counting.
# 8. append() adds an item.
# 9. remove() removes an item.
# 10. Manual comparison improves logic-building skills.