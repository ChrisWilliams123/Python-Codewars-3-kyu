#Solution to Codewars kata: https://www.codewars.com/kata/54cb771c9b30e8b5250011d4

def height(n,m):
    if m == 0 or n == 0: return 0
    if n>m: n = m
    a = m
    i = a
    for j in range(2,n+1):
        a = a*(m-j+1)//j
        i += a

        
    return i
