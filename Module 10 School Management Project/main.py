from school import School
from person import Student, Teacher
from subject import Subject
from classroom import ClassRoom

school = School("ABC", "Dhaka")

# Adding Classroom
eight = ClassRoom("Eight")
nine = ClassRoom("Nine")
ten = ClassRoom("Ten")

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

# Adding Student
rahim = Student("Rahim", eight)
sakib = Student("Sakib", nine)
rakib = Student("Rakib", ten)
khalid = Student("Khalid", eight)
ridoy = Student("Ridoy", eight)

school.student_admission(rahim)
school.student_admission(sakib)
school.student_admission(rakib)
school.student_admission(khalid)
school.student_admission(ridoy)

# Adding Teachers
halim = Teacher("Halim")
lokman = Teacher("Lokman")
forid = Teacher("Forid")
any = Teacher("Any")

# Adding Subject
bangla = Subject("Bangla", forid)
biology = Subject("Biology", lokman)
english = Subject("English", halim)
math = Subject("Math", any)
physics = Subject("Physics", any)


eight.add_subject(bangla)
eight.add_subject(english)
eight.add_subject(math)

nine.add_subject(bangla)
nine.add_subject(english)
nine.add_subject(math)
nine.add_subject(physics)

ten.add_subject(bangla)
ten.add_subject(english)
ten.add_subject(math)
ten.add_subject(physics)
ten.add_subject(biology)

eight.take_semester_finel_exam()
nine.take_semester_finel_exam()
ten.take_semester_finel_exam()
print(school)
