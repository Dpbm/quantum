import numpy

class Operations:
    def __init__(self):
        self.operator = numpy
        self.float32 = numpy.float32

    def dot(self, first_vector, second_vector):
        return self.operator.dot(first_vector, second_vector)
    
    def create_vector(self, initial_value):
        return self.operator.array(initial_value, dtype=self.float32)

    def square_root(self, number):
        return self.operator.sqrt(number)