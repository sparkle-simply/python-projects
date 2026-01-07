import math

class Scientific_Calculator:
    def sine(angle):
        return math.sin(math.radians(angle))

    def cosine(angle):
        return math.cos(math.radians(angle))

    def tangent(angle):
        return math.tan(math.radians(angle))

    def logarithm(value, base = 10):
        return math.log(value, base)

    def exponential(value):
        return math.exp(value)