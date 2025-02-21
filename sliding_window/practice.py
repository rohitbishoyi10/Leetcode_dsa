# Input :  X = "GeeforGeeks",
#          Y = "GeeksQuiz"
from collections import defaultdict


# def find_substring(st:str):
#     # s = set()
#     d = dict()
#     l = 0
#     start = 0
#     cv =0
#     mv = 0
#     fs = ""
#     for end in range(len(st)):
#         if st[end] in d and d[st[end]] >=start:
#             start = d[st[end]] +1
#         d[st[end]] = end
#         cv = end - start+1
#         if cv >mv:
#             mv = cv
#             l=start
#     return st[l:l+mv]
#
# ip = "abcdd"
# op = find_substring(ip)
# print(op)


# def find_common_strings(s1,s2):
#     longrst = ""
#     fs = ""
#     for i in range(len(s1)):
#         for j in range(i+1,len(s1)):
#             fs = s1[i:j]
#             if fs in s2:
#                 if len(fs)>len(longrst):
#                     longrst = fs
#     return longrst
#
# s1 = "rohitkumarbishoyi"
# s2 = "kumarrohitbishof"
# op = find_common_strings(s1,s2)
# print(op)
# def  num_count(st:str):
#     ns = ""
#     count = 1
#     for i in range(1,len(st)):
#         if st[i] == st[i-1]:
#             count+=1
#         else:
#             ns = ns + str(count) + st[i-1]
#             count = 1
#     ns = ns+str(count)+st[-1]
#
#     return ns
# ip = "aaeerraa"
# op = num_count(ip)
# print(op)

# def max_average_subarr(arr,k):
#     ini_sum = sum(arr[:k])
#     max_sum = ini_sum
#     l = 0
#
#     for i in range(k,len(arr)):
#         ini_sum = ini_sum + arr[i] -arr[l]
#         l+=1
#         if ini_sum>max_sum:
#             max_sum = ini_sum
#     return max_sum/4
#
# ip = [1,12,-5,-6,50,3]
# op = max_average_subarr(ip,4)
# print(op)

# def two_sum(arr1,arr2,arr3,target):
#     s = set(arr1)
#     for i in range(len(arr2)):
#         for j in range(len(arr3)):
#             comp = target -arr2[i]- arr3[j]
#
#             if comp in s:
#                 return comp, arr2[i],arr3[j]
#
#
#
#     return -1
#
# ip1 = [2,3,4,5]
# ip2 = [0,0,0,0]
# ip3= [11,12,13,14]
# op = two_sum(ip1,ip2,ip3,20)
# print(op)


# def reverse_list(arr):
#     l = 0
#     r = len(arr)-1
#     while l<r:
#         arr[l],arr[r] = arr[r],arr[l]
#         l+=1
#         r-=1
#     return arr
#
# ip = [0,1,2,3,4,5,6,7]
# op = reverse_list(ip)
# print(op)


# def tri_sum_unique(arr,target):
#     arr.sort()
#     res = []
#     for i in range(len(arr)):
#         if i>0 and arr[i] == arr[i-1]:
#             continue
#         l = i+1
#         r = len(arr)-1
#         while l<r:
#             cu_sum = arr[i] + arr[l] + arr[r]
#             if cu_sum == target:
#                 res.append((arr[i],arr[l],arr[r]))
#
#                 while l<r and arr[l]==arr[l+1]:
#                     l+=1
#                 while l<r and arr[r] == arr[r-1]:
#                     r-=1
#                 l += 1
#                 r -= 1
#
#
#             elif cu_sum <target:
#                 l+=1
#             else:
#                 r-=1
#     return res
#
# ip = [3,2,5,1,1,8,8,2,5,3,6,5]
# op = tri_sum_unique(ip,8)
# print(op)


# def group_anagram(arr):
#     dct = defaultdict(list)
#     nl2=[]
#     for i in arr:
#         nl = [0] * 26
#         for j in i:
#             temp = ord(j) - ord('a')
#             nl[temp] = 1
#         tpl = tuple(nl)
#         dct[tpl] += [i]
#     for k in dct.values():
#         nl2.append(k)
#     return nl2
#
# ip = ["eat","tea","tan","ate","nat","bat"]
# op = group_anagram(ip)
# print(op)

# def group_anagram(arr):
#     dct = dict()
#     ss = ""
#     nl = []
#     for i in arr:
#         ss = "".join(sorted(i))
#         if ss in dct:
#             dct[ss] += [i]
#         else:
#             dct[ss] = [i]
#     for k in dct.values():
#         nl.append(k)
#
#
#     return nl


# ip =  ["eat","tea","tan","ate","nat","bat"]
# op = group_anagram(ip)
# print(op)


def product_of_number_except_current()





