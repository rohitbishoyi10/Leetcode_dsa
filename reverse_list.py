#programme to reverse a list

def revrse_list(arr:list):
    mid = len(arr)//2
    high = len(arr)-1
    for i in range(mid):
            arr[i],arr[high] = arr[high],arr[i]
            high-=1
    return arr

a1 = [1,2,3,4,5,6,7,8,9]
re = revrse_list(a1)
print(re)

#reverse a list

# def rev_List(arr:list):
#     return arr[::-1]
# a1 = [1,2,3,4,5,6,7,8]
# re = rev_List(a1)
# print(re)