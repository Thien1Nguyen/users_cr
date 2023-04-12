from flask import Flask, render_template, request, redirect, session

from users_model import User


app = Flask(__name__)
app.secret_key = 'ham and cheese'

@app.route("/")
def index():

    users = User.get_all()

    print(users)
    return render_template("index.html", users=users)

@app.route('/create_user', methods=["POST"])
def create_user():
    User.create(request.form)
    return redirect('/')

@app.route("/new_user")
def new_user():

    return render_template("new_user.html")

if __name__ == "__main__":
    app.run(debug=True)