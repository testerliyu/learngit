import math

def quadratic(a, b, c):
    delta = b * b - 4 * a * c
    if a == 0:
        if b == 0:
            if c == 0:
                print('方程恒成立，无穷解')
            else:
                return None
        else:
            return -c/b
    else:
        if delta == 0:
            return -b / (2*a)
        elif delta < 0:
            return None
        else:
            return (-b+math.sqrt(delta))/(2*a), (-b-math.sqrt(delta))/(2*a)

# some particular test cases
print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))
print(quadratic(0, 3, -4))
print(quadratic(0, 0, 0))
print(quadratic(0, 0, 1))
print(quadratic(0, 2, 1))
