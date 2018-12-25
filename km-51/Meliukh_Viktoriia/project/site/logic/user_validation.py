import cx_Oracle, hashlib


def get_user_by_id(user_name):
    con = cx_Oracle.connect('system/Mumeqybysghbdtn1024@127.0.0.1/orcldb')
    cur = con.cursor()
    cur.execute(f"SELECT * FROM users WHERE USER_ID = '{user_name[0]}'")
    res = cur.fetchone()
    cur.close()
    con.close()
    return res

def get_user_by_name(user_name):
    con = cx_Oracle.connect('system/Mumeqybysghbdtn1024@127.0.0.1/orcldb')
    cur = con.cursor()
    cur.execute(f"SELECT * FROM users WHERE EMAIL = '{user_name}'")
    res = cur.fetchone()
    cur.close()
    con.close()
    return res


def validate(user, passwrd):
    if validate_pass(user[5], passwrd):
        return True
    else:
        return False


def validate_pass(db_pass, user_pass):
    return db_pass == hashlib.sha256(user_pass.encode()).hexdigest()


def user_exist(email):
    con = cx_Oracle.connect('system/Mumeqybysghbdtn1024@127.0.0.1/orcldb')
    cur = con.cursor()
    cur.execute(f"SELECT * FROM users WHERE EMAIL = '{email}'")
    res = cur.fetchone()
    cur.close()
    con.close()
    return not not res


def validate_registration(form_data):
    return not user_exist(form_data['email'])


def create_user(user):
    con = cx_Oracle.connect('system/Mumeqybysghbdtn1024@127.0.0.1/orcldb')
    cur = con.cursor()
    # cur.execute(f"INSERT INTO users VALUES (sys_guid(),'{user['fname']}', '{user['mname']}','{user['lname']}', '{user['email']}', '{hashlib.sha256(user['password'].encode()).hexdigest()}' , '0')")
    cur.callproc("users_pack.add_users",
                 [user['fname'], user['mname'], user['lname'], user['email'], hashlib.sha256(user['password'].encode()).hexdigest(), 0])
    con.commit()
    cur.close()
    con.close()
    return


def get_bookings_byuser_id(id):
    con = cx_Oracle.connect('system/Mumeqybysghbdtn1024@127.0.0.1/orcldb')
    cur = con.cursor()
    cur.execute(f"SELECT  c.CLASSROOMNUM, c.HOUSINGNUMBER, c.NUMBEROFSEATS, l.BTIME, l.ETIME, l.LESSONNUMBER,"
                f" c.MULTIMEDIA, b.BOOKING_ID FROM BOOKING b JOIN CLASSROOM c ON b.CLASSROOM_ID = c.CLASSROOM_ID "
                f"JOIN LESSON l "
                f"ON b.LESSON_ID = l.LESSON_ID  WHERE b.USER_ID = '{id[0]}'")
    # cur.execute(f"SELECT * FROM BOOKING WHERE USER_ID = '{id[0]}'")
    res = cur.fetchall()
    cur.close()
    con.close()
    return res


def find_classrooms(criteria):
    con = cx_Oracle.connect('system/Mumeqybysghbdtn1024@127.0.0.1/orcldb')
    cur = con.cursor()
    cur.execute(f"SELECT c.classroom_id, c.classroomnum, c.housingnumber, c.multimedia, c.numberofseats "
                f"FROM CLASSROOM c WHERE c.housingnumber = '{criteria['h_num']}'"
                f" AND c.numberofseats >= '{criteria['seats']}' AND c.multimedia = '{criteria['mult']}' "
                f"AND NOT EXISTS (SELECT * FROM BOOKING b JOIN LESSON l ON b.LESSON_ID = l.LESSON_ID "
                f"WHERE to_char(b.BOOKINGDATE) = to_char(DATE '{criteria['date']}')"
                f" AND l.LESSONNUMBER = '{criteria['l_num']}')")
    res = cur.fetchall()
    cur.close()
    con.close()
    return res


def get_all_users_info():
    con = cx_Oracle.connect('system/Mumeqybysghbdtn1024@127.0.0.1/orcldb')
    cur = con.cursor()
    cur.execute(f"SELECT u.USER_ID, u.FNAME, u.MNAME, u.LNAME, u.EMAIL, u.EMAILISCHECKED  FROM USERS u")
    res = cur.fetchall()
    cur.close()
    con.close()
    return res


def get_all_unch_users():
    con = cx_Oracle.connect('system/Mumeqybysghbdtn1024@127.0.0.1/orcldb')
    cur = con.cursor()
    cur.execute(f"SELECT u.USER_ID, u.FNAME, u.MNAME, u.LNAME, u.EMAIL FROM Users u WHERE u.EMAILISCHECKED = 0")
    res = cur.fetchall()
    cur.close()
    con.close()
    return res


def delete_user_bookings(params):
    con = cx_Oracle.connect('system/Mumeqybysghbdtn1024@127.0.0.1/orcldb')
    cur = con.cursor()
    cur.callproc("booking_pack.delete_class_booking", [params])
    con.commit()
    cur.close()
    con.close()
    return


def edit_user_bookings(booking):
    con = cx_Oracle.connect('system/Mumeqybysghbdtn1024@127.0.0.1/orcldb')
    cur = con.cursor()
    cur.callproc("booking_pack.editing_booking", [booking['id'], booking['class_room_id'], booking['userid'],
                                                  booking['lessonid'],
                                                  booking['bdate']])
    cur.close()
    con.close()
    return


def check_user_email(user_id):
    con = cx_Oracle.connect('system/Mumeqybysghbdtn1024@127.0.0.1/orcldb')
    cur = con.cursor()
    cur.execute(f"UPDATE USERS u SET u.emailischecked = 1 WHERE USER_ID = '{user_id}'")
    con.commit()
    cur.close()
    con.close()
    return


def create_booking(book, user_id, l_id):
    con = cx_Oracle.connect('system/Mumeqybysghbdtn1024@127.0.0.1/orcldb')
    cur = con.cursor()
    cur.execute(f" INSERT INTO booking VALUES (sys_guid() , '{user_id[0]}' , '{l_id[0]}' , '{book['c_id']}' , DATE '{book['b_date']}')")
    #'{book['b_date']}') ")
    # cur.callproc("booking_pack.create_application", [user_id[0], l_id[0], book['c_id'], book['b_date']])
    con.commit()
    cur.close()
    con.close()
    return


def validate_book_creation(bok, l_id):
    con = cx_Oracle.connect('system/Mumeqybysghbdtn1024@127.0.0.1/orcldb')
    cur = con.cursor()
    cur.execute(f"SELECT * FROM BOOKING b WHERE b.LESSON_ID = '{l_id[0]}' AND b.CLASSROOM_ID = '{bok['c_id']}' "
                f"AND to_char(b.BOOKINGDATE) = to_char(DATE '{bok['b_date']}')")
    res = cur.fetchall()
    if res:
        return False
    else:
        return True


def delete_user_func(user_id):
    con = cx_Oracle.connect('system/Mumeqybysghbdtn1024@127.0.0.1/orcldb')
    cur = con.cursor()
    cur.execute(f"DELETE BOOKING b WHERE b.USER_ID = '{user_id}'")
    cur.execute(f"DELETE USERS u WHERE u.USER_ID = '{user_id}'")
    con.commit()
    cur.close()
    con.close()
    return


def create_classroom(cl):
    con = cx_Oracle.connect('system/Mumeqybysghbdtn1024@127.0.0.1/orcldb')
    cur = con.cursor()
    cur.callproc("classroom_pack.create_class", [cl['c_num'], cl['h_num'], cl['n_set'], cl['mult']])
    con.commit()
    cur.close()
    con.close()
    return


def edit_classroom(cl):
    con = cx_Oracle.connect('system/Mumeqybysghbdtn1024@127.0.0.1/orcldb')
    cur = con.cursor()
    cur.callproc("classroom_pack.editing_classroom", [cl['c_id'], cl['c_num'], cl['h_num'], cl['n_set'],
                                                      cl['mult'], cl['c_st']])
    con.commit()
    cur.close()
    con.close()
    return


def delete_classroom(c_id):
    con = cx_Oracle.connect('system/Mumeqybysghbdtn1024@127.0.0.1/orcldb')
    cur = con.cursor()
    cur.callproc("classroom_pack.delete_class", [c_id])
    con.commit()
    cur.close()
    con.close()
    return


def get_lessons_data():
    con = cx_Oracle.connect('system/Mumeqybysghbdtn1024@127.0.0.1/orcldb')
    cur = con.cursor()
    cur.execute("SELECT * FROM LESSON")
    res = cur.fetchall()
    cur.close()
    con.close()
    return res


def get_housing_numbers_data():
    con = cx_Oracle.connect('system/Mumeqybysghbdtn1024@127.0.0.1/orcldb')
    cur = con.cursor()
    cur.execute("SELECT DISTINCT HOUSINGNUMBER FROM CLASSROOM")
    res = cur.fetchall()
    cur.close()
    con.close()
    return res


def get_number_of_seats_data():
    con = cx_Oracle.connect('system/Mumeqybysghbdtn1024@127.0.0.1/orcldb')
    cur = con.cursor()
    cur.execute("SELECT DISTINCT NUMBEROFSEATS FROM CLASSROOM ORDER BY NUMBEROFSEATS")
    res = cur.fetchall()
    cur.close()
    con.close()
    return res


def get_user_id_data(user_name):
    con = cx_Oracle.connect('system/Mumeqybysghbdtn1024@127.0.0.1/orcldb')
    cur = con.cursor()
    cur.execute(f"SELECT USER_ID FROM USERS WHERE EMAIL = '{user_name}'")
    res = cur.fetchone()
    cur.close()
    con.close()
    return res


def get_lesson_id_by_number(n):
    con = cx_Oracle.connect('system/Mumeqybysghbdtn1024@127.0.0.1/orcldb')
    cur = con.cursor()
    cur.execute(f"SELECT LESSON_ID FROM LESSON WHERE LESSONNUMBER = '{n}'")
    res = cur.fetchone()
    cur.close()
    con.close()
    return res

