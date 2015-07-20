# Uses divide & conquer to sort array in O(n log n).
def merge_sort(array):
    # Base case - an array of length 1 is always a sorted array.
    if len(array) > 1:
        mid = len(array)/2
        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)

        x = 0
        y = 0
        z = 0

        while x < len(left) and y < len(right):
            if left[x] < right[y]:
                array[z] = left[x]
                x += 1
            else:
                array[z] = right[y]
                y += 1
            z += 1

        while x < len(left):
            array[z] = left[x]
            x += 1
            z += 1

        while y < len(right):
            array[z] = right[y]
            y += 1
            z += 1

    return array

# Tests accuracy of sorting function.
def test_sort(function, starting_position):
    for pos, num in enumerate(function, starting_position):
        if pos != num:
            print(pos, num)
    else:
        return 'OK!'
