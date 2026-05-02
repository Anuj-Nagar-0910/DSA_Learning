import math


def countPrimes(n):
    ans = 0
    if n == 1:
        return 0
    for number in range(2, n):
        print("Number:", number)
        count = 0
        for num in range(1,int(math.sqrt(number))+1):
            print("Number:", number, "Divisor:", num)
            if number%num == 0:
                    count=count+1
            print("Count:", count)
            print("******************")
        if count == 1:
            ans=ans+1
        print("Ans:", ans)
        print("-------------")

    return ans

if __name__ == '__main__':
	# n = int(input())
	result = countPrimes(12)
	# print(result)