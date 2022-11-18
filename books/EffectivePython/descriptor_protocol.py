# descriptor protocol
class Grade(object):
    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        pass


class Exam(object):
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()


exam = Exam()

# Exam.__dict__['writing_grade'].__set__(exam,40)
exam.writing_grade = 40

# Exam.__dict__['writing_grade']__get__(exam,Exam))
print(exam.writing_grade)