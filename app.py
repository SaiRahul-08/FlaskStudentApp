from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("students.db")

@app.route("/")
def home():
    return "Flask Student Management Application"

@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()
    con = get_db()
    con.execute(
        "CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, department TEXT)"
    )
    con.execute(
        "INSERT INTO students (name, department) VALUES (?, ?)",
        (data["name"], data["department"])
    )
    con.commit()
    con.close()
    return jsonify({"message": "Student added successfully"})

@app.route("/students", methods=["GET"])
def get_students():
    con = get_db()
    con.execute(
        "CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, department TEXT)"
    )
    rows = con.execute("SELECT * FROM students").fetchall()
    con.close()
    return jsonify(rows)

if __name__ == "__main__":
    app.run(debug=True)
