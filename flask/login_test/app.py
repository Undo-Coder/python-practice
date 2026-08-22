from flask import Flask, redirect, url_for, render_template, request
import flask_login

#初期化
app = Flask(__name__)
app.secret_key = "aiueo"

login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(flask_login.UserMixin):
    def __init__(self, id):
        self.id = id

#サンプルのユーザー
users = {'test': {'password': 'HELLO365'}}

#ログイン画面
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        #入力された値を入手
        username = request.form['username']
        password = request.form['password']

        #ログイン処理
        if username in users and users[username]['password'] == password:
            user = User(username)
            flask_login.login_user(user)
            return redirect(url_for('Welcome'))
        return 'ログイン失敗'
    return render_template("login/index.html")

#メイン画面
@app.route('/Welcome')
@flask_login.login_required
def Welcome():
    return render_template("Main/index.html",current_user=flask_login.current_user.id)

#ログアウト画面
@app.route('/logout')
@flask_login.login_required
def logout():
    flask_login.logout_user()
    return render_template("logout/index.html")

#ユーザーローダー
@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        return User(user_id)
    return None

if __name__ == '__main__':
    app.run(debug=True)