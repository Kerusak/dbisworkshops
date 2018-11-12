from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/server/api/<action>', methods=['GET'])
def get(action):
    if action == 'classroom':
        return render_template('classroom.html', room=classroom_dictionary)
    elif action == 'user':
        return render_template('user.html', user=user_dictionary)
    elif action == 'all':

        all_dict = dict(user=user_dictionary, classroom=classroom_dictionary)

        return render_template('all.html', result=all_dict)
    else:
        return render_template('404.html')


@app.route('/server/api/<action>', methods=['POST'])
def post(action):
    if action == "classroom":
        classroom_dictionary["classroomId"] = request.form["classroomId"]
        classroom_dictionary["classroomNumber"] = request.form["classroomNumber"]
        classroom_dictionary["housingNumber"] = request.form["housingNumber"]
        classroom_dictionary["numberOfSeats"] = request.form["numberOfSeats"]
        classroom_dictionary["multimedia"] = request.form["multimedia"]
        classroom_dictionary["status"] = request.form["status"]
        return redirect(url_for('get', action='all'))

    elif action == "user_update":
        user_dictionary["userId"] = request.form["userId"]
        user_dictionary["fName"] = request.form["fName"]
        user_dictionary["mName"] = request.form["mName"]
        user_dictionary["lName"] = request.form["lName"]
        user_dictionary["email"] = request.form["email"]
        user_dictionary["password"] = request.form["password"]
        user_dictionary["emailChecked"] = request.form["emailChecked"]

        return redirect(url_for('get', action='all'))
    else:
        return render_template('404.html')


if __name__ == "__main__":
    user_dictionary = dict(userId='61BA3C8B63CD450BA180196D67AF8BA9',
                           fName='Иванов', mName='Иван', lName='Иванович',
                           email='ivan@mail.com', password='4198329807', emailChecked=1)

    classroom_dictionary = dict(classroomId='79EE4A3E61D44F5CB44ED7C18F304694', classroomNumber=95, housingNumber=15,
                                numberOfSeats=20, multimedia=1, status=0)
    app.run(debug=True, port=5001)
