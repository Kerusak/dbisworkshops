from flask import Flask, render_template, request, make_response, redirect, url_for, flash

from Booking import Booking
from Classroom import Classroom
from User import User
from Lesson import Lesson
from Housing import Housing
from Seat import Seat
from BookingForUser import  BookingForUser
from logic.user_validation import get_user_by_id, validate, user_exist, validate_registration, create_user, \
    get_bookings_byuser_id, find_classrooms, get_all_users_info, get_all_unch_users, delete_user_bookings, \
    edit_user_bookings, check_user_email, create_booking, validate_book_creation, delete_user_func, create_classroom, \
    edit_classroom, delete_classroom, get_lessons_data, get_housing_numbers_data, get_number_of_seats_data, \
    get_user_id_data, get_lesson_id_by_number, get_user_by_name
from form.register_form import RegisterForm
import json

app = Flask(__name__)
app.secret_key = 'development key'


@app.route('/')
def index():
    user_login = request.cookies.get('userID')
    if user_login:
        return render_template('search_page.html')
    else:
        return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    user_login = request.form['login']
    user_pass = request.form['pass']
    if user_login == 'admin':
        if user_pass == '123':
            return redirect(url_for('get_all_user_datas'))
    # user validation here
    user = get_user_by_name(user_login)

    if not user:
        return render_template('index.html')
    if user[6] == 0:
        flash('Your account is not verified yet')
        return redirect(url_for('index'))
    if validate(user, user_pass):
        resp = make_response(render_template('search_page.html'))
        resp.set_cookie('userID', user_login)
        return resp

    return render_template('index.html')


@app.route('/logout')
def logout():
    resp = make_response(redirect(url_for('index')))
    resp.set_cookie('userID', '', expires=0)
    return resp


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'GET':
        return render_template('register.html', form=form)
    else:
        if not form.validate():
            flash('incorrect data input')
            return render_template('register.html', form=form)
        form_data = request.form
        if validate_registration(form_data):
            create_user(form_data)
            return render_template('check_page.html')
        else:
            flash('User with dis email already exist')
            return render_template('register.html', form=form)


@app.route('/search')
def search_page():
    return render_template('search_form_page.html')


# @app.route('/editbookings')
# def edit_personal_bookings():
#     return render_template('edit_personal_bookings.html')


@app.route('/bookingconfirm')
def booking_confirmation():
    user_login = request.cookies.get('userID')
    if not user_login:
        render_template('index.html')
    user_id = get_user_id_data(user_login)
    user = get_user_by_id(user_id)

    booking = request.args
    res = [[], []]
    res[0] = user
    res[1] = booking
    return render_template('booking_confirm.html', res=res)


@app.route('/confirmsuccess')
def confirm_success():
    return render_template('confirm_success.html')


@app.route('/bookingdeleted')
def booking_deleted():
    return render_template('booking_deleted.html')
# ---------------------------------------------------------- 'api'

# ----------------------- user booking crud


@app.route('/bookingsbyuser')
def allbookings():
    user_login = request.cookies.get('userID')
    if not user_login:
        render_template('index.html')
    user_id = get_user_id_data(user_login)
    res = get_bookings_byuser_id(user_id)
    result_list = []
    for r in res:
        result_list.append(BookingForUser(r).__dict__)
    return render_template('edit_personal_bookings.html', res=result_list)


@app.route('/deletebooking')
def delete_user_booking():
    params = request.args['id']
    delete_user_bookings(params)
    return json.dumps('OK')


@app.route('/editbooking')
def edit_user_booking():
    params = request.args
    edit_user_bookings(params)
    return json.dumps('OK')


@app.route('/book')
def booking():
    user_login = request.cookies.get('userID')
    if not user_login:
        render_template('index.html')
    user_id = get_user_id_data(user_login)

    bok = request.args

    lesson_id = get_lesson_id_by_number(bok['l_num'])
    t = validate_book_creation(bok, lesson_id)
    if t:
        create_booking(bok, user_id, lesson_id)
        return json.dumps('OK')
    else:
        return json.dumps('ALREADY EXISTS')


@app.route('/findclassrooms')
def find():
    criterias = request.args
    classrooms = find_classrooms(criterias)
    res = []
    for r in classrooms:
        res.append(Classroom(r).__dict__)
    return json.dumps(res, default=str)


# @app.route('/bookingconfirm')
# def booking_confirm():


@app.route('/displaysearchresult')
def display_search():
    criterias = request.args
    classrooms = find_classrooms(criterias)
    res = [[], []]
    res[1] = criterias
    for r in classrooms:
        res[0].append(Classroom(r).__dict__)
    return render_template('display_search.html', res=res)


@app.route('/lessonsdata')
def lessons_data():
    les = get_lessons_data()
    res = []
    for l in les:
        res.append(Lesson(l).__dict__)
    return json.dumps(res)


@app.route('/gethousingnumbers')
def get_housing_numbers():
    housing = get_housing_numbers_data()
    res = []
    for h in housing:
        res.append(Housing(h).__dict__)
    return json.dumps(res)


@app.route('/getnumberofseats')
def get_number_of_seats():
    seats = get_number_of_seats_data()
    res = []
    for s in seats:
        res.append(Seat(s).__dict__)
    return json.dumps(res)
# ----------------------------- admin users crud


@app.route('/getalluserdata')
def get_all_user_datas():
    users_data = get_all_users_info()
    res = []
    for u in users_data:
        res.append(User(u).__dict__)
    return render_template('admin_page.html',  res=res)


@app.route('/getalluncheckedusers')
def get_all_unchecked():
    data = get_all_unch_users()
    res = []
    for u in data:
        res.append(User(u).__dict__)
    return json.dumps(res)


@app.route('/checkuser')
def check_user():
    user_id = request.args['id']
    check_user_email(user_id)
    return json.dumps('OK')
# delete user


@app.route('/deleteuser')
def delete_user():
    user_id = request.args['id']
    delete_user_func(user_id)
    return json.dumps('deleted')
# create classroom


@app.route('/createclassroom')
def create_class_room():
    classroom = request.args
    create_classroom(classroom)
    return json.dumps('CREATED')

# edit classroom


@app.route('/editclassroom')
def edit_class_room():
    classroom = request.args
    edit_classroom(classroom)
    return json.dumps('OK')


# delete classroom
@app.route('/deleteclassroom')
def delete_class_room():
    c_id = request.args['id']
    delete_classroom(c_id)
    return json.dumps('deleted')


if __name__ == '__main__':
    app.run(debug=True)
