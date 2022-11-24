'''
Language: Python3
Problem Source: Codeforces Div2

Problem Desc: You are given two arrays AA and BB consisting of integers, sorted in non-decreasing order. 
Check whether it is possible to choose k numbers in array AA and choose mm numbers in array BB so 
that any number chosen in the first array is strictly less than any number chosen in the second array.

'''

'''Solution'''
#get two arrays with k length from a (ta) and m length from b (tb)
#because a and b is sorted, ta will have elements from a[0] to a[k] while tb will have elements from b[nb-1] to b[nb-m-1]
#compare the a[k] to b[nb-m-1] to get the result


#get input
na, nb = map(int,input().split())
k, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))


def solution(na,nb,k,m,a,b):
    ta = []
    tb = []
    for i in range(k):
        ta.append(a[i])
    for i in range((nb-1),(nb-m-1),-1):
        tb.append(b[i])
    if ta[k-1] < tb[m-1]:
      #compare a "k"th element to b "m"th if smaller return YES
        return "YES"
    return "NO"
 
print(solution(na,nb,k,m,a,b))
