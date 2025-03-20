def quick_sort(sequence):
    if len(sequence) <= 1:
        return sequence
    lowest_list = []
    greatest_list = []
    pivot = sequence.pop()
    for item in sequence:
        if item < pivot:
            lowest_list.append(item)
        else:
            greatest_list.append(item)
    return quick_sort(lowest_list) + [pivot] + quick_sort(greatest_list)

print(quick_sort([3, 4, 2, 1, 0, 8]))