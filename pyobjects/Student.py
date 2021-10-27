class Student:
    def __init__(self, id, name):

        self.id=id
        self.name=name
        self.subject_grade= {}

    def add_grade(self, subname, grade):
        self.subject_grade[subname] = grade

    def __str__(self):
        return f"id: {self.id}, name: {self.name}, subject and grade: {self.subject_grade}"

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, subject and grade: {self.subject_grade}"

    def calc_factor(self, subject, fac_percent):
        if subject in self.subject_grade:
            new_grade=((fac_percent/100)+1)*self.subject_grade[subject]
            if new_grade > 100:
                new_grade=100
            self.subject_grade[subject] = new_grade

    def average(self):
        return (sum(self.subject_grade.values))/len(self.subject_grade)

