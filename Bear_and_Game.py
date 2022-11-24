'''
language: Python 3
Problem Source: Codeforces

Problem:Bear Limak likes watching sports on TV. He is going to watch a game today. The game lasts 90 minutes and there are no breaks.

Each minute can be either interesting or boring. If 1515 consecutive minutes are boring then Limak immediately turns TV off.

You know that there will be n interesting minutes t1,t2,...,tn. Your task is to calculate for how many minutes Limak will watch the game.



Input: The first line of the input contains one integer nn (1 \leq n \leq 90)(1≤n≤90) — the number of interesting minutes.

The second line contains nn integers t1,t2,t3,...,tn(1 ≤ t1 < t2 < t3 <...<tn≤90), given in the increasing order.



Ouput: Print the number of minutes Limak will watch the game.

'''
'''Solution'''

n = int(input())
a = list(map(int, input().split()))

def BearandGame(n, a):
    if a[0] > 15:
        return 15
    else:
        for i in range(n):
            enj_time = a[i] + 15
            if i + 1 > n-1:
                if (a[n-1] <= 90) and (a[n-1] + 15) > 90:
                    return 90
                else:
                    return (a[n-1] + 15)
            if a[i+1] not in range(enj_time+1):
                return a[i] + 15

print(BearandGame(n,a))
