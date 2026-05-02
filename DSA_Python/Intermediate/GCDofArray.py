import math

def gcdOfArray(n,arr):
    q = arr
    def gcd(a, b):
        if b==0:
            return a
        return gcd(b,a%b)
    while len(q)>1:
        a = q.pop(0)
        b = q.pop(0)
        q.append(gcd(a,b))
    return q[0]
    

    

def main():
    # n = int(input())
    arr = [8,12,16]
    res = gcdOfArray(3,arr)
    print(res)

if __name__=="__main__":
    main()