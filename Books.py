'''
Problem Source: Codeforces
Language: Python

Problem: When Valera has got some free time, he goes to the library to read some books. Today he's got tt free minutes to read. That's why Valera took nn books in the library and for each book he estimated the time he is going to need to read it. Let's number the books by integers from 11 to nn. Valera needs ai
minutes to read the i-th book.

Valera decided to choose an arbitrary book with number i and read the books one by one, starting from this book. In other words, he will first read book number ii, then book number i + 1i+1, then book number i+2i+2 and so on.
He continues the process until he either runs out of the free time or finishes reading the n-th book.
Valera reads each book up to the end,
that is, he doesn't start reading the book if he doesn't have enough free time to finish reading it.

Print the maximum number of books Valera can read.
'''

'''Solution'''

n, t = map(int, input().split())
a = list(map(int,input().split()))


def solution(n,t,a):
    cnt = 0
    max_book = 0
    s = 0
    for i in range(n):
        ep = a[i] #end pointer
        cnt += ep
        while cnt > t:
            sp = a[s] #start pointer
            cnt -= sp
            s += 1
        max_book = max(max_book,i - s + 1)
    return max_book
  
print(solution(n,t,a))
