# Input : arr = {30, 20, 50} , K = 70
# Output : 30, 20
# 30 + 20 = 50, which is the maximum possible sum which is less than K

# def two_sum_less_than_k(arr,target):
#     nl = []
#     max_aum = 0
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             cur_sum = arr[i] + arr[j]
#             if cur_sum<target:
#                 max_aum = cur_sum
#
#
#     return max_aum
#
# ip = [30,20,50,80,60,10,10]
#
# op = two_sum_less_than_k(ip,70)
# print(op)

# def two_sum_lessthan_k(arr,target):
#
#     arr.sort()
#     l = 0
#     h = len(arr) - 1
#     max = 0
#
#     while l<h:
#         addition = arr[l] + arr[h]
#         if addition < target:
#             max = addition
#             l = l+1
#         else:
#             h = h-1
#     return max
#
# ip = [30,20,50,80,60,10,10]
#
# op = two_sum_lessthan_k(ip,70)
# print(op)



# ip = [30,20,50]
# op = two_sum_lessthan_k(ip,50)
# print(op)