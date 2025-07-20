from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["students_db"]
collection = db["Chapter6_students"]

@app.route("/")
def index():
    students = list(collection.find())
    return render_template("Index.html", students=students)

@app.route("/exercise1")
def exercise1():
    return render_template("Exercise1.html")

@app.route("/exercise2", methods=["GET", "POST"])
def exercise2():
    if request.method == "POST":
        collection.insert_one({
            "name": request.form["name"],
            "age": int(request.form["age"]),
            "gender": request.form["gender"],
            "major": request.form["major"]
        })
        return redirect(url_for("index"))
    return render_template("Exercise2.html")

@app.route("/exercise3")
def exercise3():
    students = list(collection.find())
    return render_template("Exercise3.html", students=students)

@app.route("/Exercise4/edit/<id>", methods=["GET", "POST"])
def exercise4_edit(id):
    student = collection.find_one({"_id": ObjectId(id)})
    if request.method == "POST":
        collection.update_one({"_id": ObjectId(id)}, {"$set": {
            "name": request.form["name"],
            "age": int(request.form["age"]),
            "gender": request.form["gender"],
            "major": request.form["major"]
        }})
        return redirect(url_for("Exercise3"))
    return render_template("Exercise4.html", student=student)

@app.route("/Exercise5/delete/<id>", methods=["GET", "POST"])
def exercise5_delete(id):
    student = collection.find_one({"_id": ObjectId(id)})
    if request.method == "POST":
        collection.delete_one({"_id": ObjectId(id)})
        return redirect(url_for("Exercise3"))
    return render_template("Exercise5.html", student=student)

@app.route("/exercise6", methods=["GET"])
def exercise6():
    name = request.args.get("name", "")
    if name:
        students = list(collection.find({"name": name}))
    else:
        students = []
    return render_template("Exercise6.html", students=students)

@app.route("/exercise7", methods=["GET"])
def exercise7():
    name = request.args.get("name", "")
    if name:
        students = list(collection.find({"name": {"$regex": name, "$options": "i"}}))
    else:
        students = []
    return render_template("Exercise7.html", students=students)

@app.route("/exercise8", methods=["GET"])
def exercise8():
    major = request.args.get("major", "")
    if major:
        students = list(collection.find({"major": major}))
    else:
        students = []
    return render_template("Exercise8.html", students=students)

@app.route("/exercise9")
def exercise9():
    results = list(collection.aggregate([
        {"$group": {"_id": "$major", "count": {"$sum": 1}}}
    ]))
    return render_template("Exercise9.html", results=results)

@app.route("/exercise10", methods=["GET", "POST"])
def exercise10():
    if request.method == "POST":
        name = request.form["name"]
        math = float(request.form["math"])
        literature = float(request.form["literature"])
        english = float(request.form["english"])

        # Find the student by name (only the first match)
        student = collection.find_one({"name": name})
        if student:
            collection.update_one(
                {"_id": student["_id"]},
                {"$set": {
                    "scores": {
                        "math": math,
                        "literature": literature,
                        "english": english
                    }
                }}
            )
        return redirect(url_for("index"))
    return render_template("Exercise10.html")

@app.route("/exercise11")
def exercise11():
    students = list(collection.find())
    for s in students:
        scores = s.get("scores", {})
        if scores:
            gpa = round((scores.get("math", 0) + scores.get("literature", 0) + scores.get("english", 0)) / 3, 2)
        else:
            gpa = 0
        s["gpa"] = gpa
        collection.update_one({"_id": s["_id"]}, {"$set": {"gpa": gpa}})
    return render_template("Exercise11.html", students=students)

@app.route("/exercise12")
def exercise12():
    students = list(collection.find())
    for s in students:
        gpa = s.get("gpa", 0)
        if gpa >= 8:
            rank = "Excellent"
        elif gpa >= 6.5:
            rank = "Good"
        else:
            rank = "Average"
        s["rank"] = rank
        collection.update_one({"_id": s["_id"]}, {"$set": {"rank": rank}})
    return render_template("Exercise12.html", students=students)

@app.route("/exercise13")
def exercise13():
    students = list(collection.find({"gpa": {"$gte": 8}}))
    return render_template("Exercise13.html", students=students)

@app.route("/exercise14")
def exercise14():
    student = collection.find_one(sort=[("gpa", -1)])
    return render_template("Exercise14.html", student=student)

@app.route("/exercise15", methods=["GET"])
def exercise15():
    min_age = request.args.get("min_age", type=int)
    max_age = request.args.get("max_age", type=int)
    query = {}
    if min_age is not None and max_age is not None:
        query["age"] = {"$gte": min_age, "$lte": max_age}
    students = list(collection.find(query))
    return render_template("Exercise15.html", students=students)

@app.route("/exercise16", methods=["GET"])
def exercise16():
    gender = request.args.get("gender", "")
    query = {"gender": gender} if gender else {}
    students = list(collection.find(query))
    return render_template("Exercise16.html", students=students)

if __name__ == "__main__":
    app.run(debug=True)
