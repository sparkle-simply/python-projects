import sys
from maths_calculator import add, subtract, multiply, divide
from scientific_calculator import sine, cosine, tangent, logarithm, exponential
from ascii_calculator import char_to_ascii, ascii_to_char
from roman_calculator import int_to_roman


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

def ascii_calculator():
    print("\nHi, ASCII Calculator")
    print("ASCII (Hello) =", char_to_ascii('Hello'))
    print("ASCII (Have a nice day!) =", char_to_ascii('Have a nice day!'))
    print("ASCII (Thank you) =", char_to_ascii('Thank you'))
    print("!! Thank You ASCII Calculator !!")

def roman_calculator():
    print("\nHi, Roman Calculator")
    int_to_roman()
    print("!! Thank You Roman Calculator !!")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        mode = sys.argv[1]
        match mode:
            case 'maths':
                maths_calculator()
            case 'scientific':
                scientific_calculator()
            case 'ascii':
                ascii_calculator()
            case 'roman':
                roman_calculator()
            case _:
                print('Calculator Mode Not Implemented !!')
    else:
        print('Please provide calculator mode')