class Student:
    def __init__ (self):
        self.first_name = []
        self.second_name = []
        self.couse = []
        self.student_id = []
        print("class successfully created!")
    def add_firstname (self, name):
        self.first_name = name
        print(f"Here is the result {self.first_name}")
        if len(self.first_name) >= 1:
            return True
        return False
    def add_second_name(self, name):
        self.second_name = name
        print(f"Here is your another result {self.second_name}")
        if len(self.second_name) >= 1:
            return True
        return False
student = Student()
student.add_firstname("Oleg")




