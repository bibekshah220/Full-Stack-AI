student_grades = {
    "anit": 85,
    "Bibek": 92,
    "rishab": 78,
    "ajit": 90,
    "kundan": 88
}

if student_grades:  # check if dictionary is not empty
    total_grades = sum(student_grades.values())
    number_of_students = len(student_grades)
    average_grade = total_grades / number_of_students
    print(f"The average grade is: {average_grade:.2f}")
else:
    print("No student data available.")