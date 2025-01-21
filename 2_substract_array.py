# def two_substract_array(arr,target):
#     s1 = set()
#     s2 = set()
#
#     for i in arr:
#         if i-target in s1:
#             s2.add((i,i-target))
#         if i+target in s1:
#             s2.add((i,i+target))
#         s1.add(i)
#     return list(s2)
#
# a1 = [3,2,4,5,6,7,1,2,9]
# re = two_substract_array(a1,6)
# print(re)

def find_pairs_with_difference_two_pointers(arr, target):
    arr.sort()
    i, j = 0, 1
    pairs = []

    while j < len(arr):
        diff = arr[j] - arr[i]

        if diff == target:
            pairs.append((arr[j], arr[i]))
            i += 1
            j += 1
        elif diff < target:
            j += 1
        else:
            i += 1

        if i == j:  # Ensure pointers don't overlap
            j += 1

    return pairs


arr = [1, 5, 2, 4, 6]
target = 3
result = find_pairs_with_difference_two_pointers(arr, target)
print(result)
