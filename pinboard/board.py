from flask import Blueprint, render_template, request, redirect, url_for
from pinboard.db import get_db

bp = Blueprint("board", __name__)

import os


@bp.route("/")
def list():
    db = get_db()
    posts = db.execute("SELECT * FROM post").fetchall()
    return render_template("board/list.html", posts=posts)

@bp.route("/add", methods=("GET", "POST"))
def add():
    if request.method == "GET":
        return render_template("board/add.html")
    else:
        title = request.form["title"]
        description = request.form["description"]
        color = request.form["color"]

        db = get_db()
        db.execute(
            "INSERT INTO post (title, description, color) VALUES (?, ?, ?)",
            (title, description, color)
        )
        db.commit()

        return redirect(url_for("board.list"))

@bp.route("/likes",methods=("GET", "POST"))
def add_like():
    if request.method == "GET":
        db = get_db()
        user = str(os.getlogin())
        #Problem: Konnte die postId bzw den Loop Index nicht von jinja/html extrahieren
        #post_id = request.args.get("{{loop.index}}")
        post_id = 2

        db.execute("UPDATE post SET likes = likes + 1 WHERE id = ?",[post_id])
        db.execute("UPDATE post SET liked_by_user = ? WHERE id = ?",[user,post_id])


        db.commit()

        return redirect(url_for("board.list"))
    else:
        return render_template("board/list.html")


@bp.route('/sortnew', methods=("GET", "POST"))
def sort_new():
    db = get_db()
    posts = db.execute("SELECT * FROM post ORDER BY created DESC").fetchall()
    return redirect(url_for("board.list"))

@bp.route('/sortlikes', methods=("GET", "POST"))
def sort_like():
    db = get_db()
    posts = db.execute("SELECT * FROM post ORDER BY likes DESC").fetchall()
    return redirect(url_for("board.list"))

#Idee: die Spalte liked_by_user wird mit dem user (user = (os.getlogin()) geupdated, wenn er den Post liked,
#  daraufhin wird der Like-Button deaktiviert. Mit dem Button "new User session" soll die ganze Spalte "liked_by_user"
# wieder zurückgesetzt werden, klappt aber nicht :(
@bp.route('/new_session', methods=("GET", "POST"))
def delete_user_session():
    db = get_db()
    posts = db.execute("UPDATE post SET liked_by_user = 'test' ")
    return redirect(url_for("board.list"))




