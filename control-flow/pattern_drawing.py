#!/bin/python3
size = abs(int(input("Enter the size of the pattern: ")))

index = size
while index:
    for i in range(size):
        print("*", end="")
    print("")
    index -= 1
