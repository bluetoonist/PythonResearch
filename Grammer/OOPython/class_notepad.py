"""
instance method

static method

class method

"""

class study_method:
    class_var = 0

    def __init__(self):
        self.init_value = 1

    def this_instance_method_(self):
        return self.init_value

    @staticmethod
    def this_static_method():
        study_method.class_var += 4
        return study_method.class_var

    @classmethod
    def this_class_method(cls):
        return cls.class_var


obj = study_method()


print(study_method.this_static_method())