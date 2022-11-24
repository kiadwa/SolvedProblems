'''
language: Python3

Problem: According to rules of the Berland fashion, a jacket should be fastened by all the buttons except only one, 
but not necessarily it should be the last one. Also if the jacket has only one button, it should be fastened, 
so the jacket will not swinging open.

You are given a jacket with nn buttons. Determine if it is fastened in a right way

Input:The first line contains integer nn (1≤n≤1000) — the number of buttons on the jacket.

The second line contains n integers ai (0≤ai≤1). The number a_i = 0 if if the i-th button is not fastened. Otherwise a_i = 1.

Output: In the only line print the word "YES" if the jacket is fastened in a right way. Otherwise print the word "NO".
'''
'''Solution'''


n = int(input())  
a = list(map(int, input().split()))  


if n == 1: 
	if a[0] == 1:
		print("YES")
	else:
		print("NO")

else:
	cnt = 0
	for i in range(0,n):
		if a[i] == 1:
			cnt += 1

	if cnt == n - 1: 
		print("YES")
	else:
		print("NO")
