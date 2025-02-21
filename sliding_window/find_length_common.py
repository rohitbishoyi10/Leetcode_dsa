# Input :  X = "GeeforGeeks",
#          Y = "GeeksQuiz"
# Output : Geeks
from os import lseek


def find_longest_common_substring(st1,st2):
     max_length = 0
     ls = ""
     for i in range(len(st1)):
         for j in range(i+1,len(st1)+1):
             ss = st1[i:j]
             if ss in st2:
                 if len(ss)>len(ls):
                     ls = ss
                     max_length = len(ls)

     return ls,max_length

ip = "GeeksforGeekst"
ip2 = "GeekstQuiz"
op = find_longest_common_substring(ip,ip2)
print(op)


