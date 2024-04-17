

from flask import Flask, jsonify, request
from student import Student

app = Flask(__name__)

students = []

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify({'students': [student.__dict__ for student in students]})

@app.route('/students', methods=['POST'])
def create_student():
    data = request.json
    student = Student(data['name'], data['student_id'])
    students.append(student)
    return jsonify({'message': 'Student created successfully'}), 201

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.json
    for student in students:
        if student.student_id == student_id:
            student.name = data['name']
            return jsonify({'message': 'Student updated successfully'})
    return jsonify({'message': 'Student not found'}), 404

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    for i, student in enumerate(students):
        if student.student_id == student_id:
            del students[i]
            return jsonify({'message': 'Student deleted successfully'})
    return jsonify({'message': 'Student not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
