""" Homework """
""" exam : attend_to_exam get_mark """
class Exam:
    Subject="Python"
    
    def __init__(self):
        self.name=''
        self.roll=0
        self.mark=0
    def attend_to_exam(self,name,roll,mark):
        self.name=name
        self.roll=roll
        self.mark=mark
        
    def get_mark(self):
        print(f'Total Mark: {self.mark}')
        
me=Exam()
me.attend_to_exam('Mehadi',5,83)
khalid=Exam()
khalid.attend_to_exam('Khalid',6,90)
me.get_mark()
khalid.get_mark()