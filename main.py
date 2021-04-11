def creation(array, numbers, filename):
    array.clear()
    numbers.clear()
    fin = open(filename)
    size = int(fin.readline())

    string = fin.readline().split()

    for i in range(size):
        array.append(int(string[i]))

    for lines in fin:
        numbers.append(int(lines))

    numbers.pop(0)


def binary_search(array, value):
    mid = len(array) // 2
    left = 0
    right = len(array) - 1

    while array[mid] != value and left <= right:
        if value > array[mid]:
            left = mid + 1
        else:
            right = mid - 1
        mid = (left + right) // 2

    if left > right:
        return -1
    else:
        return mid


def binary_search_with_checking(array, numbers, filename):
    fout = open(filename)

    result_array = []
    for elem in numbers:
        result_array.append(binary_search(array, elem))

    i = 0
    for lines in fout:
        if int(lines) != result_array[i]:
            return False
        else:
            i = i + 1

    return True


if __name__ == '__main__':

    array = []
    numbers = []

    for i in range(5):
        filein = "sourses/" + str(i+1) + ".in"
        fileout = "sourses/" + str(i+1) + ".out"
        
        creation(array, numbers, filein)
        print(binary_search_with_checking(array, numbers, fileout))





