# Write a Python function student_data () that will print the ID of a student (student_id). If the user passes an argument student_name or student_class the function will print the student name and class.


def student_data(student_id, **kwargs):
  print("Student ID:", student_id)

  if 'student_name' in kwargs: 
    print("Student Name:", kwargs['student_name'])

  if 'student_class' in kwargs:
    print("Student Class:", kwargs['student_class'])


# student_data(student_id="26ja")
# print()
# student_data(student_id="26ja", student_name="Jooyoung Julie Ahn")
# print()
# student_data(student_id="26ja",
#              student_name="Jooyoung Julie Ahn",
#              student_class="2026")

student_data(student_name="Jooyoung Julie Ahn", student_class="2026")
