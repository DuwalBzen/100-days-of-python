"""
Day 16 Python Challenge
Student Score Analyzer Program

You are building a small school analysis program that helps a teacher understand student performance.

You are given a dataset of students and their exam scores.

Your program must analyze this data and print useful information.
"""

from prettytable import PrettyTable

students = [
    {"name": "Alex", "score": 85},
    {"name": "Maya", "score": 92},
    {"name": "Ken", "score": 76},
    {"name": "Sara", "score": 88},
    {"name": "John", "score": 67},
    {"name": "Emma", "score": 95},
    {"name": "Liam", "score": 72},
    {"name": "Olivia", "score": 81}
]

# Task 1 — Print All Students
def get_result(students):
    for student in students:
        print(f"{student["name"]} scored {student["score"]}")


# Task 2 — Find the Top Student
# Output example: Top student: Emma with score 95

def get_highest_score(students):
    score = 0
    student_name = ""
    for student in students:
        if student["score"] > score:
            score = student["score"]
            student_name = student["name"]
    print(f"Top student: {student_name} with score {score}")



#Task 3 — Calculate Average Score
# Formula:
# average = total_score / number_of_students
#Output example:
# Average score: 82.0

def calculate_average(students):
    total_score  = 0
    for student in students:
        total_score += student["score"]
    average = total_score / len(students)
    print(f"Average score: {average}")


"""
Task 4 — Count Passing Students
Passing score = 70
Your program should count how many students passed.
Example output:
Number of students who passed: 7
"""

def count_passed(students):
    count = 0
    for student in students:
        if student["score"] >= 70:
            count += 1
    print(f"Number of students who passed: {count}")


"""
Task 5 — Assign Grades

Create a grade system based on score.
Score	Grade
90 – 100	A
80 – 89	B
70 – 79	C
60 – 69	D
Below 60	F

Output example:
Alex : B
Maya : A
Ken : C
Sara : B
John : D
Emma : A
Liam : C
Olivia : B
"""

def calculate_grades(students):

    table = PrettyTable()
    table.field_names = ["Student", "Grade"]

    for student in students:

        score = student["score"]

        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "FAILED"

        table.add_row([student["name"], grade])

    print(table)


display_grade = PrettyTable()
get_result(students)
get_highest_score(students)
calculate_average(students)
count_passed(students)
calculate_grades(students)
