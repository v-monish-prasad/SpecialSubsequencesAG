def findSpecialSubsequencesAG(array, length):
    if not array:
        return "Empty Array."

    A_Count = 0
    AG_Count = 0

    for i in range(length):
        if array[i] == 'A':
            A_Count += 1
        elif array[i] == 'G':
            AG_Count += A_Count

    return AG_Count


if __name__ == "__main__":
    array = input()
    length = len(array)
    print(findSpecialSubsequencesAG(array, length))
