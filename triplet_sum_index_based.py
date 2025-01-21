#return the index of triplet sum


def triplet_sum(arr,target):
    for i in range(len(arr)):
        dct = {}

        for j in range(i+1,len(arr)):
            complement = target - arr[i] - arr[j]

            if complement in dct:
                return i, j, dct[complement]
            dct[arr[j]] = j
    return -1

ip = [1,2,3,4,5,6,7]
op = triplet_sum(ip,18)
print(op)