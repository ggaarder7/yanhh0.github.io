def mul(a, b):
        return a[0]*b[1]+a[1]*b[0]+a[0]*b[0], a[0]*b[0]+a[1]*b[1]
 
def fib(n):
        x, r = (1, 0), (0, 1)
        while n:
                if n & 1: r = mul(r, x)
                x = mul(x, x)
                n >>= 1
        return r[0]
         
print(fib(int(input())))
/**************************************************************
    Problem: 1229
    User: 20160748
    Language: Python
    Result: 正确
    Time:32 ms
    Memory:33064 kb
****************************************************************/
