"""
Create a simple API fask app which designed to store data about students:
 1. Create class Student in a separate module. (should have fields: name, id)
 2. The main file of the app should have a list of students and next API endpoints:
 - create new student,
 - update student data by ID,
 - delete by ID.
"""

from flask import Flask, request, jsonify
from student import Student

app = Flask(__name__)
student_list = []
id_counter: int = 0

@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()
    print(data)
    global id_counter

    if not data or 'name' not in data:
        return jsonify({"error": "Name is required"}), 400

    id_counter +=1
    new_student = Student(name=data['name'], student_id=id_counter)
    student_list.append(new_student)
    print(new_student.students())
    return jsonify(new_student.students()), 201


@app.route("/students/<int:stud_id>", methods=["PUT"])
def update_student(stud_id):
    data = request.get_json()
    print(data)

    if not data or 'name' not in data:
        return jsonify({"error": "Name is required"}), 400

    student = next((s for s in student_list if s.get_id() == stud_id), None)
    if student is None:
        return jsonify({"error": "Student not found"}), 404

    student.set_name(data['name'])
    print(student.students())
    return jsonify(student.students()), 200


@app.route("/students/<int:stud_id>", methods=["DELETE"])
def delete_student(stud_id):
    student = next((s for s in student_list if s.get_id() == stud_id), None)
    if student is None:
        return jsonify({"error": "Student not found"}), 404

    student_list.remove(student)
    return jsonify({"message": "Student deleted successfully"}), 200


@app.route("/students", methods=["GET"])
def get_students():
    return jsonify([student.students() for student in student_list])


if __name__ == "__main__":
    app.run(debug=True)
