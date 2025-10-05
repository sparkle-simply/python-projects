def char_to_ascii(s = 'a'):
    if not isinstance(s, str):
        raise ValueError("Input must be string")
    return [ord(char) for char in s]

def ascii_to_char(ascii_values = [97]):
    if isinstance(ascii_values, int):
        ascii_values = [ascii_values]
    if not all(0 <= val <= 127 for val in ascii_values):
        raise ValueError("ASCII values should be within 0 and 127")
    return ''.join(chr(val) for val in ascii_values)