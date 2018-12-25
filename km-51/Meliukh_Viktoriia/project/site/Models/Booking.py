class Booking():
    booking_id = str
    user_id = str
    classroom_id = str
    lesson_id = str
    bookingdate = str

    def __init__(self, bok):
        self.booking_id = bok[0]
        self.user_id = bok[1]
        self.classroom_id = bok[2]
        self.lesson_id = bok[3]
        self.bookingdate = bok[4]



