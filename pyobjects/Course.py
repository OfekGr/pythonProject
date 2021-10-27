from pyobjects.Student import Student
class Course:

    def __init__(self, courseID, course_name, max_students):
        self.courseID=courseID
        self.course_name=course_name
        self.max_students=max_students
        self.subjects_teachers={}
        self.students=[]

    def __str__(self):
        return f"courseID: {self.courseID}, course name: {self.course_name}, max students in course: {self.max_students},subject teachers: {self.subjects_teachers} students: {self.students},"

    def add_student(self,student):
        if len(self.students)<self.max_students:
            self.students.append(student)
            return True
        else:
            return False

    def add_factor(self, subject, fac_percent):
        for i in self.students:
            i.calc_factor(subject, fac_percent)

    def del_student(self, studentID):
        print("inside del", self.students)
        for i in self.students:
            if studentID == i.id:
                del self.students.i[1]



course=Course(123, "economics", 10)
student1=Student(1,"aaaa")
print(course)
print(student1)
course.add_student(student1)
print(course)
course.del_student(1)
print("after delete", course)







   # def eligible_student(self, student):
  #      for i in subject_grade
  #          if student = <> and
 #               return True
    #        else:
   #             return False





