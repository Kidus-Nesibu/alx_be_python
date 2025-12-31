#!/bin/python3
def safe_divide(numerator, denominator):
    try:
        return float(numerator) / float(denominator)
    except (ValueError, ZeroDivisionError) as e:
        print(e)

