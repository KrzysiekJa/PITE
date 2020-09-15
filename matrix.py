import math
from itertools import starmap
from operator  import mul

class Matrix:
    def __init__(self, list):
        if math.sqrt(len(list)) != int(math.sqrt(len(list))):
            raise ValueError("It's not right size of NxN matrix.")
        else:
            self.list   = [i for i in list]
            self.length = int(math.sqrt(len(list)))
    
    def __str__(self):
        string = ""
        for i, elem in enumerate(self.list):
           string += str(elem) + " "
           if (i % self.length == self.length - 1):
               string += '\n'
        return string
    
    def __radd__(self, other):
        return Matrix([i + other for i in self.list])
    
    def __add__(self, other): 
        return Matrix([i + other for i in self.list])
        
    def __iadd__(self, other):
        if type(other) == int:
            self.list = [i + other for i in self.list]
            return self
        elif type(other) == Matrix:
            self.list = [elem + other.list[i] for i, elem in enumerate(self.list)]
            return self
        else:
            raise TypeError("Type not excepted.")
    
    def __isub__(self, other):
        if type(other) == int:
            self.list = [i - other for i in self.list]
            return self
        elif type(other) == Matrix:
            self.list = [elem - other.list[i] for i, elem in enumerate(self.list)]
            return self
        else:
            raise TypeError("Type not excepted.")
    
    def __mul__(self, other):
        return Matrix([elem * other.list[i] for i, elem in enumerate(self.list)])
    
    def __matmul__(self, other):
        our_list   = []
        tmp        = []
        other_list = [[] for i in range(other.length)]
        
        append = our_list.append
        for i, elem in enumerate(self.list):
            tmp.append(elem)
            if (i % self.length == self.length - 1):
                append(tmp)
                tmp = []
                
        for i, elem in enumerate(other.list):
            other_list[i % self.length].append(elem)
        
        return Matrix([sum(starmap(mul, zip(row, col))) for row in our_list for col in other_list])
    
    def add(self, new_one):
        if self.length == new_one.length:
            result = [x + y for x, y in zip(self.list, new_one.list)]
            return result
        else:
            raise ValueError("Matrices are not similar.")
