def int_to_roman_conversion(num):
    if not (0 < num < 4000):
        raise ValueError("Input must be between 1 and 3999")

    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num

def int_to_roman():
    try:
        num = int(input("Enter a number to convert to Roman numeral: "))
        print(f"Roman numeral: {int_to_roman_conversion(num)}")
    except ValueError as ve:
        print(f"Error: {ve}")