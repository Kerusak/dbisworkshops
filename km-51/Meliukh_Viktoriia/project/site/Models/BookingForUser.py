class BookingForUser():
    CLASSROOMNUM = str
    HOUSINGNUMBER = str
    NUMBEROFSEATS = str
    BTIME = str
    ETIME = str
    LESSONNUMBER = str
    MULTIMEDIA = str
    CLASSROOM_ID = str

    def __init__(self, b):
        self.CLASSROOMNUM = b[0]
        self.HOUSINGNUMBER = b[1]
        self.NUMBEROFSEATS = b[2]
        self.BTIME = b[3]
        self.ETIME = b[4]
        self.LESSONNUMBER = b[5]
        self.MULTIMEDIA = b[6]
        self.CLASSROOM_ID = b[7]

