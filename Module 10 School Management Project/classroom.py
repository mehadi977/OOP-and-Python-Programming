class ClassRoom:
    def __init__(self, name):
        self.name = name
        self.studens = []  # list of student objects
        self.subjects = []  # list of subject objects

    def add_student(self, student):  # rahim, eight e vorti hobe.
        roll_no = f"{self.name} - {len(self.studens)+1}"
        student.id = roll_no
        self.studens.append(student)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def take_semester_finel_exam(self):
        for subject in self.subjects:
            subject.exam(self.studens)

        for student in self.studens:
            student.calculate_final_grade()
