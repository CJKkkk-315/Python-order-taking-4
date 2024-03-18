# siyu yin
# csce 101-002
# 2023.02.09
# ysiyu@email.sc.edu
# Lab1
test1 = int(input('input the test1 score:'))
test2 = int(input('input the test2 score:'))
lab_avg = int(input('input the lab_avg score:'))
project = int(input('input the project score:'))
quiz = int(input('input the quiz score:'))
final_grade = lab_avg * 0.5 + project * 0.05 + test1 * 0.15 + test2 * 0.15 + quiz * 0.15
if final_grade >= 90:
    letter_grade = 'A'
elif 87 <= final_grade < 90:
    letter_grade = 'B+'
elif 80 <= final_grade < 87:
    letter_grade = 'B'
elif 77 <= final_grade < 80:
    letter_grade = 'C+'
elif 70 <= final_grade < 77:
    letter_grade = 'C'
elif 67 <= final_grade < 70:
    letter_grade = 'D+'
elif 60 <= final_grade < 67:
    letter_grade = 'D'
else:
    letter_grade = 'F'
print(f'Your final grade is: {final_grade}')
print(f'Your letter grade is an {letter_grade}')
