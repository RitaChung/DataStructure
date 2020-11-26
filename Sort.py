# bubble sort - comparison-based algorithm
def bubble_sort(list):
    # two for loop is for pair comparison, which will list all the pair combination
    for iter in range(len(list)-1,0,-1): # from end to beginning
        for idx in range(iter): # list all the element before current iter
            if list[idx] > list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp

list = [19,2,31,45,6,11,121,27]
bubble_sort(list)
print(list)

#merge sort
def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list

    #find the middle point and devide it
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return merge(left_list, right_list)


def merge(left_half, right_half):
    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res

list = [64,34,25,12,22,11,90]
print(merge_sort(list))


# insert sort
def insertion_sort(list):
    for i in range(1, len(list)):
        j = i-1
        next_element = list[i]
        while (list[j] > next_element) and (j >= 0):
            list[j+1] = list[j]
            j = j-1
        list[j+1] = next_element


list = [19,2,31,45,30,11,121,27]
insertion_sort(list)
print(list)

#shell sort
def shell_sort(list):
    gap = len(list) // 2
    while gap > 0:
        for i in range(gap, len(list)):
            temp = list[i]
            j = i

            while j >= gap and list[j - gap] > temp:
                list[j] = list[j - gap]
                j = j - gap
            list[j] = temp
        gap = gap // 2


list = [19,2,31,45,30,11,121,27]
shell_sort(list)
print(list)


#selection sort
def selection_sort(list):
    for idx in range(len(list)):
        min_dix = idx
        for j in range(idx+1, len(list)):
            if list[min_dix] > list[j]:
                min_dix = j
        list[idx], list[min_dix] = list[min_dix], list[idx]

list = [19,2,31,45,30,11,121,27]
selection_sort(list)
print(list)
