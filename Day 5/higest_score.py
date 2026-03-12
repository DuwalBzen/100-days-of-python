student_scores = [
    78, 85, 90, 66, 92, 74, 88, 79, 95, 83,
    67, 81, 73, 89, 91, 76, 84, 69, 94, 87,
    72, 80, 77, 93, 68, 86, 82, 75, 97, 71
]

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)

print(max(student_scores))