class Student:
    def __init__(self, name, age, roll, marks):
        self.name = name
        self.age = age
        self.roll = roll
        self.marks = {}
        
    def add_mark(self, subject, mark):
        self.marks[subject] = mark
        
    def get_total_marks(self):
        return sum(self.marks.values())
    
    def get_average_marks(self):
        return sum(self.marks.values()) / len(self.marks)
    
    def get_highest_mark(self):
        return max(self.marks.values())
    
    def get_lowest_mark(self):
        return min(self.marks.values())
    
# Create a student instance
student1 = Student("John", 20, "A001", {})

# Add marks for different subjects
student1.add_mark("Math", 85)
student1.add_mark("Science", 78)
student1.add_mark("English", 92)

# Get total marks
total_marks = student1.get_total_marks()
print("Total marks:", total_marks)

# Get average marks
average_marks = student1.get_average_marks()
print("Average marks:", average_marks)

# Get highest mark
highest_mark = student1.get_highest_mark()
print("Highest mark:", highest_mark)

# Get lowest mark
lowest_mark = student1.get_lowest_mark()
print("Lowest mark:", lowest_mark)    