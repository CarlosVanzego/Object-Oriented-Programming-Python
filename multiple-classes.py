# Using multiple Classes in OOP in Python
# Practice..

class Student:
      def __init__(self, name, age, grade):
          self.name = name
          self.age = age
          self.grade = grade 

      def get_grade(self):
          return self.grade

class Course:
    def __init__(self, name, max_students):
         self.name = name
         self.max_students = max_students
         self.students = []

    def add_student(self, student):
         if len(self.students) < self.max_students:
              self.students.append(student)
              return True
         return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
              value += student.get_grade()

        return value / len(self.students)

s1 = Student("Carlos", 28, 88) 
s2 = Student("Taylor", 26, 90) 
s3 = Student("Robert", 22, 82) 

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s3)

# This will print the name of the student.
# print(course.students[0].name)

# This will print the average grade of the students.
print(course.get_average_grade())

