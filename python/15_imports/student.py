class Student:
    def __init__(self, name: str, student_id: int):
        self.name = name
        self.id = student_id

    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def students(self):
        return {"name": self.name, "student_id": self.id}