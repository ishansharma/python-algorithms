import math


def binary_search(arr, search):
    size = len(arr)

    left = 0
    right = size - 1

    if left > right:
        return False

    while left < right:
        mid = math.floor((right - left) / 2)
        if search == arr[mid]:
            return mid
        elif search < arr[mid]:
            right = mid
            mid = math.floor((left - right) / 2)
        elif search > arr[mid]:
            left = mid
            mid = math.floor((left - right) / 2)

    return False


def test_1_small():
    arr = [1, 2, 3, 4, 5, 6]
    print("Array is", arr)
    print("Expected result is 2")
    print("Result is", binary_search(arr, 3))


def test_2_small():
    arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
    print("Array is", arr)
    print("Expected result is 15")
    print("Result is ", binary_search(arr, 30))


test_1_small()
test_2_small()
