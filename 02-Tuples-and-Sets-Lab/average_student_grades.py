def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())
    return lines

n = int(input())

student_grades_lines = input_to_list(n)

def avg(g):
    return sum(g) / len(g)

student_grades = {}

for line in student_grades_lines:
    student, grade = line.split(' ')
    if student not in student_grades:
        student_grades[student] = []
    student_grades[student].append(float(grade))

for student, grades in student_grades.items():
    grade_str = ' '.join(map(lambda grade: f'{float(grade):.2f}', grades))
    avg_grade = avg(grades)
    print(f"{student} -> {grade_str} (avg: {avg_grade:.2f})")
