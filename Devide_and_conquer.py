# binary search

def bsearch(list, value):

    idx0 = 0
    idxn = len(list) - 1

    # find the middle most value
    while idx0 <= idxn:
        midval = (idx0 + idxn) // 2
        if list[midval] == value:
            return midval
        if list[midval] > value:
            idxn = midval - 1
        else:
            idx0 = midval + 1
    if idx0 > idxn:
        return None

list  = [2, 7, 19, 34, 53, 72]
print(bsearch(list, 72))
print(bsearch(list, 11))
