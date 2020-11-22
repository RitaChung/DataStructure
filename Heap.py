import heapq

H = [21,1,45,78,3,5]

# use heapify to rearange the elements
heapq.heapify(H)
print(H)

# use heappush to insert the element into heap (add into the last index)
heapq.heappush(H,8)
print(H)

# use heappop to remove the element from heap (remove the first index)
heapq.heappop(H)
print(H)

# use heapreplace to remove ths smallest element of the heap
# and insert the new incoming element at some place not fixed by any order
H = [21,1,45,78,3,5]
heapq.heapify(H)
print(H)
heapq.heapreplace(H,6)
print(H)
