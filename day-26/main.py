#list = [i*2 for i in range(1,5)]
#print(list)
import random
#names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

#long_names = [name.upper() for name in names if len(name) > 5]
#print(long_names)

#students_scores = {student:random.randint(1, 100) for student in names}
#print(students_scores)

#passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
#print(passed_students)

import pandas

student_dict = {
    "student": ["Angela", "Dash", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# loop through a data frame
#for (key, value) in student_data_frame.items():
#    print(value)

# loop through rows of data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Dash":
        print(row.score) #print(row) #print(row.student)