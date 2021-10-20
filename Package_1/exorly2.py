def Student(name, grade, *multiple_grades):
    if len(multiple_grades) > 0:
        average = (sum(multiple_grades)+(grade)) / (len(multiple_grades)+1)
        return name, average
    else:
        return name, grade

print(Student('ofek', 100,90,80))


