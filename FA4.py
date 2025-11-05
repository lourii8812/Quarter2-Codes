student = int(input('Enter the number of students: '))
subj = int(input('Enter the number of subjects: '))
stu_fin = 0
tot_avg=0
tot_clavg=0
while stu_fin < student:
    stu_fin += 1
    subj_fin = 0
    stu_avg = 0
    tot_scr = 0
    print('Student', stu_fin)
    while subj_fin < subj:
        subj_fin += 1
        score = float(input(f'Enter score {subj_fin}: '))
        tot_scr += score
    stu_avg = tot_scr / subj
    tot_clavg += stu_avg
    print(f'Average for Student {stu_fin} = {stu_avg}.')
fin_clavg = tot_clavg / student
print(f'Class average = {fin_clavg}')
