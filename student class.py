class Student:
    def __init__(self, name, age, roll, marks):
        self.name = name
        self.age = age
        self.roll = roll
        self.marks = []
    
    def get_total_marks(self):
        return sum(self.marks)
    
    def get_average_marks(self):
        return sum(self.marks) / len(self.marks)
    
    def get_highest_mark(self):
        return max(self.marks)
    
    def get_lowest_mark(self):
        return min(self.marks)
    
student1 = Student('Jeff', 20, 5, [])
student1.marks.append(80)
student1.marks.append(75)
student1.marks.append(81)
student1.marks.append(72)

print(student1.get_total_marks())
print(student1.get_average_marks())
print(student1.get_highest_mark())
print(student1.get_lowest_mark())