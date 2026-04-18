def calculate_grades(scores_dict):
    grades = {}
    for student in scores_dict:
        score = scores_dict[student] 
        if score >= 91:
            grades[student] = "Outstanding"
        elif score >= 81:
            grades[student] = "Exceeds Expectations"
        elif score >= 71:
            grades[student] = "Acceptable"
        else:
            grades[student] = "Fail"
    return grades

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades = calculate_grades(student_scores)
print(student_grades)