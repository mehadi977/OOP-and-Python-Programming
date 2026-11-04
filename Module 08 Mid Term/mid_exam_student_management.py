# https://github.com/mehadi977/Student-Management-system
# 1. Create the StudentDatabase class-->
class StudentDatabase:
    student_list = []

    def __init__(self):
        pass

    @classmethod
    def add_student(self, student):
        self.student_list.append(student)


# 2. Create the Student class-->
class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled
        # stdnt={self.__student_id,self.__name,self.__department,self.__is_enrolled}
        # 3. Initialize Student Object
        StudentDatabase.add_student(self)

    # 4. Implement enroll_student() method
    def enrol_student(self):
        if self.__is_enrolled == True:
            print(f"Student {self.__student_id} is already enroled!")
        else:
            self.__is_enrolled = True
            print(f"{self.__student_id} Student enrolled successfully")

    # 5. Implement drop_student() method
    def drop_student(self):
        if self.__is_enrolled == True:
            self.__is_enrolled = False
            print(f"{self.__student_id} has dorpped!")
        else:
            print(f"{self.__student_id} is not enrolled before")

    # 6. Implement view_student_info() method
    def view_student_info(self):
        print(
            f"Id: {self.__student_id}, Name: {self.__name}, Department: {self.__department}, Enrollment Status: {self.__is_enrolled} "
        )

    def get_student_id(self):
        return self.__student_id


# 7. Menu System
def menu():
    while True:
        print("\n--- Student Management Menu---")
        print("1. View All Students")
        print("2. Enroll Student")
        print("3. Drop Student")
        print("4. Exit")
        choice = input("Enter your choice (1-4)")
        if choice == "1":
            s: Student
            for s in StudentDatabase.student_list:
                s.view_student_info()

        elif choice == "2":
            try:
                st_id = int(input("Entar student ID: "))
            except:
                print("Please enter valid ID(0-9)")
                continue

            student: Student
            for student in StudentDatabase.student_list:
                if student.get_student_id() == st_id:
                    student.enrol_student()
                    break
            else:
                print("Invalid student ID")

        elif choice == "3":
            try:
                st_id = int(input("Entar student ID: "))
            except:
                print("Please enter valid ID(0-9)")
                continue

            for student in StudentDatabase.student_list:
                if student.get_student_id() == st_id:
                    student.drop_student()
                    break
            else:
                print("Invalid student ID")

        elif choice == "4":
            print("Thank you!")
            break
        else:
            print("invalid choise")


Student(101, "Raicha", "BBA", True)
Student(102, "Mehadi", "CSE", True)
Student(105, "Khalid", "EEE", False)
Student(106, "Rakib", "CSE", False)

menu()
