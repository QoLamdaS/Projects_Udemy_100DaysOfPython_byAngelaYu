
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
for key in student_scores:
    if student_scores[key] >= 91:
        student_scores[key] = "Outstanding"
    elif student_scores[key] >= 81:
        student_scores[key] = "Exceeds Expectations"
    elif student_scores[key] >= 71:
        student_scores[key] = "Acceptable"
    else:
        student_scores[key] = "Fail"

#student_grades = student_scores
#print(student_grades)
print(student_scores) #* Better this than actually, as it is more efficiently.
