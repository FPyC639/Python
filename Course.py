class Course:
    def __init__(self, courseName):
        self.__courseName = courseName
        self.__students = []
    def getCourseName(self):
        return self.__courseName
    def addStudent(self, student):
        self.__students.append(student)
    def dropStudent(self, student):
        self.__students.remove(student)
    def getStudents(self):
         for i in self.__students:
             print(i, end= " ")
    def getNumberofStudents(self):
        return len(self.__students)

cps2232 = Course("Data Structures")
cps2232.addStudent("Jose M. Serra Jr.")
cps2232.addStudent("Yarelis Serra")
cps2232.addStudent("Angel Serra")
print("The course that is being offered is {}".format(cps2232.getCourseName()))
print("The current number of students in the course is {}".format(cps2232.getNumberofStudents()))
print("The students in the course are: ")
cps2232.getStudents()
cps2232.dropStudent("Yarelis Serra")
print("Oh no some students dropped the course now the number of students is {}".format(cps2232.getNumberofStudents()))
print("The current students in the course are: ")
cps2232.getStudents()
