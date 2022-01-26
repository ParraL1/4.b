#Name: Lilliana Parra
#Github username: ParraL1
#Date: 01/26/2022
#Description: fibonacci sequence



def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)