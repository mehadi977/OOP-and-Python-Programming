class School:
    def __init__(
        self,
        name,
        address,
    ):
        self.name = name
        self.address = address
        self.teachers = {}  # {"bangla" : teacher_object}
        self.classrooms = {}  # {"eight": classroom_object}

    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom

    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher

    def student_admission(self, student):
        classname = student.classroom.name
        self.classrooms[classname].add_student(student)

    @staticmethod
    def calculate_grade(mark):
        if mark >= 80 and mark <= 100:
            return "A+"
        elif mark >= 70 and mark < 80:
            return "A-"
        elif mark >= 60 and mark < 70:
            return "A"
        elif mark >= 50 and mark < 60:
            return "B"
        elif mark >= 40 and mark < 50:
            return "C"
        elif mark >= 33 and mark < 40:
            return "D"
        else:
            return "F"

    @staticmethod
    def grade_to_value(grade):
        grade_map = {
            "A+": 5.00,
            "A": 4.00,
            "A-": 3.50,
            "B": 3.00,
            "C": 2.00,
            "D": 1.00,
            "F": 0.00,
        }
        return grade_map[grade]

    @staticmethod
    def value_to_grade(value):
        if value >= 4.5 and value <= 5.00:
            return "A+"
        elif value >= 3.5 and value < 4.50:
            return "A"
        elif value >= 3.0 and value < 3.5:
            return "A-"
        elif value >= 2.5 and value < 3.0:
            return "B"
        elif value >= 2.0 and value < 2.5:
            return "C"
        elif value >= 1.0 and value < 2.0:
            return "D"
        else:
            return "F"

    # def __repr__(self):
    #     # All Classrooms
    #     for key in self.classrooms.keys():
    #         print(key)

    #     # All Students
    #     print("--All Students--")
    #     result = ""
    #     for Key, value in self.classrooms.items():  # prottekta class e gelam
    #         result += f"--{Key.upper()} Classroom Students\n"
    #         for student in value.studens:
    #             result += f"{student.name}"

    #     print(result)

    #     # All Subjects
    #     subject = ""
    #     for key, value in self.classrooms.items():
    #         subject += f"--{key.upper()} Classroom Subjects\n"
    #         for sub in value.subjects:
    #             subject += f"{sub.name}\n"
    #     print(subject)

    #     # All Teachers

    #     # All Student Results
    #     for key, value in self.classrooms.items():
    #         for student in value.studens:
    #             for k, i in student.marks.items():
    #                 print(student.name, k, i, student.subject_grade[k])
    #             print(student.calculate_final_grade())

    def __repr__(self):
        result = [f"School: {self.name}", f"Address: {self.address}"]

        for class_name, classroom in self.classrooms.items():
            result.append(f"\n--{class_name.upper()} Classroom Students")
            for student in classroom.studens:
                result.append(f"{student.id} - {student.name}")
                for subject, mark in student.marks.items():
                    grade = student.subject_grade[subject]
                    result.append(f"  {subject}: {mark} ({grade})")
                if student.marks:
                    result.append(f"  {student.calculate_final_grade()}")

            result.append(f"--{class_name.upper()} Classroom Subjects")
            for subject in classroom.subjects:
                result.append(subject.name)

        return "\n".join(result)
