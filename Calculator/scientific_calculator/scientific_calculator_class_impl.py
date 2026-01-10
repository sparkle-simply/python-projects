import math

class Scientific_Calculator:
    @staticmethod
    def sine(angle):
        return math.sin(math.radians(angle))

    @staticmethod
    def cosine(angle):
        return math.cos(math.radians(angle))

    @staticmethod
    def tangent(angle):
        return math.tan(math.radians(angle))

    @staticmethod
    def logarithm(value, base = 10):
        return math.log(value, base)

    @staticmethod
    def exponential(value):
        return math.exp(value)