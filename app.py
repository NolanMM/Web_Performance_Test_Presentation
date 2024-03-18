from flask import Flask, request, make_response, render_template
import secrets, string

from Services.Authorized_Process import AuthorizedProcess

app = Flask(__name__)


def generate_session_id(length=40):
    characters = string.ascii_letters + string.digits
    session_id = ''.join(secrets.choice(characters) for i in range(length))
    return session_id


@app.route('/', methods=['GET'])
def index():
    session_id = request.cookies.get('session_id')
    if session_id is None:
        session_id = generate_session_id()
        response = make_response(render_template('LoginPage.html'))
        response.set_cookie('session_id', session_id)
        return response
    else:
        response = make_response(render_template('LoginPage.html'))
        response.set_cookie('session_id', session_id)
        return response


@app.route('/', methods=['POST'])
def index_post():
    session_id = request.cookies.get('session_id')
    if session_id is None:
        session_id = generate_session_id()
        response = make_response(render_template('LoginPage.html'))
        response.set_cookie('session_id', session_id)
        return response
    else:
        username = request.form['usernameInput']
        password = request.form['passwordInput']
        remember_me = request.form.get('RememberMe_checkbox', False)
        remember_me = True if remember_me == 'on' else False

        authorized_process = AuthorizedProcess()
        is_valid = authorized_process.login(username, password)
        if is_valid:
            response = make_response(render_template('HomePage.html'))
            response.set_cookie('session_id', session_id)
            return response
        else:
            response = make_response(render_template('LoginPage.html'))
            response.set_cookie('session_id', session_id)
            return response


@app.route('/Register', methods=['GET'])
def register():
    session_id = request.cookies.get('session_id')
    if session_id is None:
        session_id = generate_session_id()
        response = make_response(render_template('RegisterPage.html'))
        response.set_cookie('session_id', session_id)
        return response
    else:
        response = make_response(render_template('RegisterPage.html'))
        response.set_cookie('session_id', session_id)
        return response


@app.route('/Register', methods=['POST'])
def register_post():
    session_id = request.cookies.get('session_id')
    if session_id is None:
        session_id = generate_session_id()
        response = make_response(render_template('RegisterPage.html'))
        response.set_cookie('session_id', session_id)
        return response
    else:
        username = request.form['usernameInput']
        password = request.form['passwordInput']
        email = request.form['emailInput']
        authorized_process = AuthorizedProcess()
        is_registered = authorized_process.register(username, password, email)
        if is_registered:
            response = make_response(render_template('LoginPage.html'))
            response.set_cookie('session_id', session_id)
            return response
        else:
            response = make_response(render_template('RegisterPage.html'))
            response.set_cookie('session_id', session_id)
            return response


@app.route('/Logout', methods=['POST', 'GET'])
def logout():
    session_id = request.cookies.get('session_id')
    if session_id is None:
        session_id = generate_session_id()
        response = make_response(render_template('LoginPage.html'))
        response.set_cookie('session_id', session_id)
        return response
    else:
        authorized_process = AuthorizedProcess()
        authorized_process.logout(session_id)
        response = make_response(render_template('LoginPage.html'))
        session_id = generate_session_id()
        response.set_cookie('session_id', session_id)
        return response


def main():
    app.run(debug=True, port=25000)


if __name__ == "__main__":
    main()
