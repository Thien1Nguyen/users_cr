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
    newest_id = User.get_newest_user()
    
    return redirect(f'/show_user/{newest_id}')

@app.route('/show_user/<int:id>')
def show(id):
    return render_template('show_user.html', user = User.get_one(id))

@app.route("/new_user")
def new_user():

    return render_template("new_user.html")

@app.route('/edit/<int:id>')
def edit(id):

    return render_template('/edit_user.html',user = User.get_one(id))

@app.route('/update_user', methods =["POST"])
def update():
    User.update(request.form)
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):

    User.delete_user(id)

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)