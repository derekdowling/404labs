class Student:

    def __init__(self, name, family):
        self.name = name
        self.family = family
        self.results = {}

    def addCourseMark(self, course, mark):
        self.results[course] = mark

    def getName(self):
        return self.name + self.family

    def average(self):
        courses = len(self.results)
        grade_points = 0.0
        for course, mark in self.results.iteritems():
            grade_points += mark
        return grade_points / courses

if __name__ == "__main__":

    student = Student("Jimmy", "Bobby")
    student.addCourseMark("CMPUT101", 4.0)
    student.addCourseMark("CMPUT114", 3.0)
    student.addCourseMark("CMPUT115", 3.3)
    student.addCourseMark("CMPUT201", 3.0)

    avg = student.average()
    print(student.getName() + "'s GPA: " + str(avg))
