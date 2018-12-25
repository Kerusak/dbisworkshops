class Classroom():
    classroom_id = str
    classroomnum = str
    housingnumber = str
    multimedia = str
    numberofseats = int

    def __init__(self, classroom):
        self.classroom_id = classroom[0]
        self.classroomnum = classroom[1]
        self.housingnumber = classroom[2]
        self.multimedia = classroom[3]
        self.numberofseats = classroom[4]
