student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
#for total score
total_score = sum(student_scores)
print(f"Total score by using function: {total_score}")

total = 0
for stu_score in student_scores:
    total += stu_score
print(f"With loop total score is : {total}")

#for finding max number
max_score = max(student_scores)
print(max_score)

maximum = 0
for max_scr in student_scores:
    if max_scr > maximum:
        maximum = max_scr
print(maximum)