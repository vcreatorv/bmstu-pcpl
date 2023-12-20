from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Users.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class ToDo(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column(db.String(150), unique=True, nullable=False)
    is_complete = db.Column(db.Boolean)
    current_id = db.Column(db.Integer)


@app.get("/")
@app.get("/home")
def home():
    todo_list = ToDo.query.all()
    return render_template("index.html", todo_list=todo_list, title=f"Главная страница")


@app.post("/add")
def add():
    title = request.form.get("title")
    new_todo = ToDo(title=title, is_complete=False)

    try:
        db.session.add(new_todo)
        db.session.commit()
        new_todo.current_id = new_todo.id
        db.session.commit()
    except IntegrityError:
        print("exc")

    return redirect(url_for("home"))


@app.get("/update/<int:todo_id>")
def update(todo_id):
    todo = ToDo.query.filter_by(id=todo_id).first()
    todo.is_complete = not todo.is_complete

    db.session.commit()
    return redirect(url_for("home"))


@app.get("/delete/<int:todo_id>")
def delete(todo_id):
    todo = ToDo.query.filter_by(id=todo_id).first()

    todo_list = ToDo.query.all()
    for i in range(todo.current_id, len(todo_list)):
        todo_list[i].current_id -= 1

    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
