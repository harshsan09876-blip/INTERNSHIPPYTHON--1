#Logic I will build first 
# a = str(input ("Enter the student name"))
# marks = int(input ("Enter the number:"))
# do try except: 
#Catch ("don't enter negative marks)
# if(marks => 90 || 100):
#Print ("grade A++") 
# elif(marks => 80): 
#Print (grade A) 
# elif(marks => 70): 
#Print (grade B+)
#elif(marks = > 60): 
#Print (grade B) 
#Elif (marks => 50): 
#Print (grade C+) 
#Elif(marks => 40):
#Print (grade C) 
#Elif(marks=> 30):
#Print (grade D) 
#Elif (marks => 20):
#print(grade E) 
#else : 
#Print (grade F) 

# Student Grade Calculator

student_name = input("Enter student name: ")

try:
    subjects = int(input("Enter number of subjects: "))

    if subjects <= 0:
        print("Number of subjects must be greater than 0.")
    else:
        total_marks = 0

        for i in range(subjects):
            while True:
                try:
                    marks = float(input(f"Enter marks for Subject {i + 1} (0-100): "))

                    if marks < 0 or marks > 100:
                        print("Invalid marks! Enter marks between 0 and 100.")
                    else:
                        total_marks += marks
                        break

                except ValueError:
                    print("Invalid input! Please enter a number.")

        percentage = total_marks / subjects

        if percentage >= 90:
            grade = "A++"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B+"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C+"
        elif percentage >= 40:
            grade = "C"
        elif percentage >= 30:
            grade = "D"
        elif percentage >= 20:
            grade = "E"
        else:
            grade = "F"

        print("\n----- Student Result -----")
        print(f"Student Name : {student_name}")
        print(f"Total Marks  : {total_marks:.2f} / {subjects * 100}")
        print(f"Percentage   : {percentage:.2f}%")
        print(f"Grade        : {grade}")

except ValueError:
    print("Invalid input! Please enter a valid number.")