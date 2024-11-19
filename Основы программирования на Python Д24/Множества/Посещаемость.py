lessons = [[input() for _ in range(int(input()))] for _ in range(int(input()))]
students = {}
for lesson in lessons:
    for student in lesson:
        if student in students:
            students[student] += 1
        else:
            students[student] = 1

for i in students.keys():
    if students[i] == len(lessons):
        print(i)
