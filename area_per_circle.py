#!/usr/bin/env python3

# Created by: Ina Tolo
# Created on: Nov. 25, 2021
# This program calculates and displays the area and circumference of a
# circle with radius 12mm.

import math
a_float = 452.3893421169302
a_float2 = 12.566370614359172
formatted_float = "{:.2f}".format(a_float)
formatted_float2 = "{:.2f}".format(a_float2)


def main():
    print("For a circle with a radius of 12mm:")
    print("")
    print("Area")
    print("= π * r^2")
    print("= π * (12)^2")
    print("= {}". format(math.pi*12**2))
    print(f"≈ {formatted_float} mm")
    print("")
    print("Circumference")
    print("= 2 * π * r")
    print("= 2 * π * (12)")
    print("= {}". format(2*math.pi*2))
    print(f"≈ {formatted_float2} mm")


if __name__ == "__main__":
    main()
