import sys
from maths_calculator import add, subtract, multiply, divide
from scientific_calculator import sine, cosine, tangent, logarithm, exponential


def maths_calculator():
    print("\nHi, Maths Calculator")
    print("Addition: 3 + 4 =", add(3, 4))
    print("Subtraction: 10 - 5 =", subtract(10, 5))
    print("Multiplication: 3 * 4 =", multiply(3, 4))
    print("Division: 10 / 2 =", divide(10, 2))
    print("!! Thank You Maths Calculator !!")

def scientific_calculator():
    print("\nHi, Scientific Calculator")
    print("sin(0) =", sine(0))
    print("sin(90) = ", sine(90))
    print("cos(0) =", cosine(0))
    print("cos(90) = ", cosine(90))
    print("tan(0) =", tangent(0))
    print("tan(90) =", tangent(90))
    print("log 100 base 10 =", logarithm(100, 10))
    print("log 8 base 2 =", logarithm(8, 2))
    print("exp 1 =", exponential(1))
    print("exp 0 =", exponential(0))
    print("!! Thank You Scientific Calculator !!")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        mode = sys.argv[1]
        match mode:
            case 'maths':
                maths_calculator()
            case 'scientific':
                scientific_calculator()
            case _:
                print('Calculator Mode Not Implemented !!')
    else:
        print('Please provide calculator mode')