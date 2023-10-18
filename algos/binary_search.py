from typing import List


## Input: ordered list, element
## Output: index of element in list, or -1
def bin_search(l: List[int], el: int) -> int:
    i, j = 0, len(l) - 1
    if l[j] == el:
        return j
    while j > i:
        k = (i + j) // 2
        mid = l[k]
        if mid == el:
            return k
        if j - i == 1:
            return -1
        elif el < mid:
            i, j = i, k
        else:
            i, j = k, j
    return -1


l1 = [1, 3, 5, 9, 11, 13, 15, 17]
l2 = [1, 2, 3, 5, 9, 11, 13, 15, 17]
print(bin_search(l1, 5))
print(bin_search(l1, 17))
print(bin_search(l1, 1))
print(bin_search(l1, 2))
print(bin_search(l1, 18))
print(bin_search(l1, 11))

print(bin_search(l2, 5))
print(bin_search(l2, 17))
print(bin_search(l2, 1))
print(bin_search(l2, 2))
print(bin_search(l2, 18))
print(bin_search(l2, 11))
