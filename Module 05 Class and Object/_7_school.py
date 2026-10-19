class Student:
    def __init__(self,name,curent_class,id):
        self.name=name
        self.id=id
        self.curent_class=curent_class
    # print korar jonno
    def __repr__(self):
        return f'Student with name: {self.name}, class: {self.curent_class}, id: {self.id}'
    
class Teacher:
    def __init__(self,name,subject,id):
        self.name=name
        self.subject=subject
        self.id=id
        
    def __repr__(self):
        return f'Teacher name: {self.name}, subject: {self.subject}, id: {self.id}'
    
class School:
        def __init__(self,name):
            self.name=name
            self.techers=[]
            self.students=[]
            
        def add_teacher(self,name,subject):
            id=len(self.techers)+101
            techer=Teacher(name,subject,id)
            self.techers.append(techer)
            
        def enroll(self,name,fee):
            if(fee<6500):
                return "no enugh fee"
            else:
                id=len(self.students)+1
                student= Student(name,'C',id)
                self.students.append(student)
                return f'{name} is enrolled with id: {id}, extra money {fee-6500}'
            
        def __repr__(self):
            result=f'welcome to {self.name} \n'
            result+=f'------Our Techers-------\n'
            for tecr in self.techers:
                # print(tecr)
                result+=str(tecr)+'\n'
                
            result+="-----Our Students------\n"
            for stdnt in self.students:
                # print(stdnt)
                result+=str(stdnt)+'\n'
            return result
                

        
alia=Student('Alia',9,1)
print(alia)

pias=Teacher("Mahmud Pias","DSA",110)
print(pias)
phitron = School('Phitron')
phitron.enroll('khalid',6000)
phitron.enroll('mehedi',6500)
phitron.enroll('omuk',33333)

phitron.add_teacher('Rifat','XPSC')
phitron.add_teacher('Hridoy','CP')
phitron.add_teacher('Toufik','DS')
# phitron.add_teacher(pias)

print(phitron)