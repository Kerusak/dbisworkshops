from flask import Flask, render_template, request, flash, make_response, redirect, url_for
from workshop3.source.wtf.forms.login import LoginForm

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    u_login = request.form.get('email')
    if request.method == 'POST':
        if not form.validate():
            flash('Some fields are empty')
        elif u_login in fake_data:
            user_dict_for_render['email'] = request.form['email']
            resp = make_response(render_template('personal_page.html', user=user_dict_for_render))
            resp.set_cookie('userID', user_dict_for_render['email'])
            return resp
            # return render_template('personal_page.html')
    user_name = request.cookies.get('userID')
    if user_name is None:
        return render_template('login.html', form=form)
    else:
        user_dict_for_render['email'] = request.cookies.get('userID')
        return render_template('personal_page.html', user=user_dict_for_render)


@app.route('/logout', methods=['GET'])
def logout():
    resp = make_response(redirect(url_for('index')))
    resp.set_cookie('userID', '', expires=0)
    return resp


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = LoginForm(request.form)
    if request.method == 'POST':
        if not form.validate():
            flash('Some fields are empty')
        fake_data.append(request.form['email'])
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


if __name__ == '__main__':
    user_dict_for_render = dict()
    fake_data = list()
    app.run(debug=True)
