import sys
from maths_calculator import add, subtract, multiply, divide, Maths_Calculator
from scientific_calculator import sine, cosine, tangent, logarithm, exponential, Scientific_Calculator
from ascii_calculator import char_to_ascii, ascii_to_char, ASCII_Calculator
from roman_calculator import int_to_roman


def maths_calculator():
    print("\nHi, Maths Calculator")
    print("Addition: 3 + 4 =", add(3, 4))
    print("Subtraction: 10 - 5 =", subtract(10, 5))
    print("Multiplication: 3 * 4 =", multiply(3, 4))
    print("Division: 10 / 2 =", divide(10, 2))
    print("!! Thank You Maths Calculator !!")

    print("\nHi, Maths Calculator Class Impl")
    maths_util = Maths_Calculator()

    try:
        print("Addition: 6 + 7 =", maths_util.add(6, 7))
        print("Subtraction: 14 - 6 =", maths_util.subtract(14, 6))
        print("Multiplication: 212 * 13 =", maths_util.multiply(212, 13))
        print("Division: 144 / 12 =", maths_util.divide(144, 12))

    except ValueError as e:
        print(f"Error: {e}")

    print("!! Thank You Maths Calculator Class Impl !!")

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

    print("\nHi, Scientific Calculator Class Impl")
    scientific_util = Scientific_Calculator()

    try:
        print("sin(0) =", scientific_util.sine(0))
        print("sin(90) = ", scientific_util.sine(90))
        print("cos(0) =", scientific_util.cosine(0))
        print("cos(90) = ", scientific_util.cosine(90))
        print("tan(0) =", scientific_util.tangent(0))
        print("tan(90) =", scientific_util.tangent(90))
        print("log 100 base 10 =", scientific_util.logarithm(100, 10))
        print("log 8 base 2 =", scientific_util.logarithm(8, 2))
        print("exp 1 =", scientific_util.exponential(1))
        print("exp 0 =", scientific_util.exponential(0))

    except ValueError as e:
        print(f"Error: {e}")

    print("!! Thank You Scientific Calculator Class Impl !!")

def ascii_calculator():
    print("\nHi, ASCII Calculator")
    print("ASCII (Hello) =", char_to_ascii('Hello'))
    print("ASCII (Have a nice day!) =", char_to_ascii('Have a nice day!'))
    print("ASCII (Thank you) =", char_to_ascii('Thank you'))
    print("!! Thank You ASCII Calculator !!")

    print("\nHi, ASCII Calculator Class Impl")
    ascii_util = ASCII_Calculator()

    try:
        word = "Welcome"
        ascii_vals = ascii_util.char_to_ascii(word)
        print(f"'{word}' converted to ASCII: {ascii_vals}")

        back_to_text = ascii_util.ascii_to_char(ascii_vals)
        print(f"{ascii_vals} converted back: '{back_to_text}'")

    except ValueError as e:
        print(f"Error: {e}")

    print("!! Thank You ASCII Calculator Class Impl !!")

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