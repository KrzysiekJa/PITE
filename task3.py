import matrix as mtx


def main():
    matrix_1 = mtx.Matrix([4,5,61,7,2,5,24,-33,1])
    matrix_2 = mtx.Matrix([2,5,-2,1,4,-13,2,7,9])
    print(matrix_1)
    
    matrix_3 = matrix_1 + 2
    print(matrix_3)
    
    matrix_4 = 2 + matrix_3
    print(matrix_4)
    
    print(matrix_2)
    
    matrix_5  = mtx.Matrix([0 for i in range(9)])
    matrix_2 -= 2
    print(matrix_2)
    matrix_5 += matrix_2
    print(matrix_5)
    
    matrix_6  = mtx.Matrix([1 for i in range(9)])
    matrix_2 += 3
    print(matrix_2)
    matrix_6 -= matrix_2
    print(matrix_6)
    
    matrix_7 = matrix_2 * matrix_3
    print(matrix_7)
    
    matrix_8 = matrix_5 @ matrix_3
    print(matrix_8)
    
    matrix_9 = mtx.Matrix([16,-10,6,7,43,5,0,0,-4,34,1,0,12,1,-5,-2])
    print(matrix_9)
    
    matrix_10 = mtx.Matrix([16,-10,6,7,5,0,0,-4,34,1,0,12,1,-5,-2])


if __name__=='__main__':
    main()