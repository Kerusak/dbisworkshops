class User():
    user_id = str
    fname = str
    mname = str
    lname = str
    email = str
    emailischecked = str

    def __init__(self, user):
        self.user_id = user[0]
        self.fname = user[1]
        self.mname = user[2]
        self.lname = user[3]
        self.email = user[4]
        self.emailischecked = user[5]

