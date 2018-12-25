class Lesson():
    lesson_id = str
    lessonnumber = str
    btime = str
    etime = str

    def __init__(self, l):
        self.lesson_id = l[0]
        self.lessonnumber = l[1]
        self.btime = l[2]
        self.etime = l[3]

