#!/usr/bin/env python3
import sys
import os

def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        y = arr[mid]
        if y == x:
            return mid
        elif y < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 binary_search.py \"list_of_numbers\" \"target_value\"")
        sys.exit(1)
    list_str = sys.argv[1]
    target_str = sys.argv[2]
    
    try:
        data = [int(x.strip()) for x in list_str.split(',')]
        target = int(target_str)
        
        index = binary_search(data, target)
        
        if index != -1:
            print(f"Target {target} found at index {index}")
        else:
            print(f"Target {target} not found in the list.")
    except ValueError:
        print("Invalid input. Please provide a comma-separated list of numbers and a single target value.")
