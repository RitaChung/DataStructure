# linear search
def linear_search(arr, value):
    for run in range(len(arr)):
        result = False
        if arr[run] == value:
            result = True
            break
    return result

list = [64,34,25,12,22,11,90]
print(linear_search(list, 12))
print(linear_search(list, 91))


#interpolation_search
def interpolation_search(arr, value):
    idx0 = 0
    idxn = len(arr) - 1
    while idx0 <= idxn and value >= arr[idx0] and value <= arr[idxn]:
        # find the mid point
        mid = idx0 + int((float(idxn - idx0)/(arr[idxn]-arr[idx0]))*(value- arr[idx0]))
        #compare the value at mid point with search value
        if arr[mid] == value:
            return 'found {} at index {}'.format(str(value),str(mid))
        if arr[mid] < value:
            idx0 = mid + 1
    return 'Searched element not in the list'

list = [2,6,11,19,27,31,45,121]
print(interpolation_search(list,31))
