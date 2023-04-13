from flask import render_template, request, redirect

from flask_app.models.users_model import User

from flask_app import app

@app.route("/")
def index():

    users = User.get_all()

    print(users)
    return render_template("index.html", users=users)

@app.route('/create_user', methods=["POST"])
def create_user():
    User.create(request.form)
    newest_id = User.get_newest_user()['id']
    
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