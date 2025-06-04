class RationalError(ZeroDivisionError):
    def __init__(self, message="Denominator cannot be zero"):
        super().__init__(message)

class RationalValueError(Exception):
    def __init__(self, message="Invalid value for Rational operation"):
        super().__init__(message)

