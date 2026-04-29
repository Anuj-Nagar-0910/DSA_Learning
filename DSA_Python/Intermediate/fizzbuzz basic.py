"""
Give me optimal solution for the following problem which`s time and space complexity is minimum.:
write a progrtam that prints the numbers from 1 to 100. But for multiples of three print "Fizz" instead of the number
and for the multiples of five print "Buzz". 
For numbers which are multiples of both three and five print "FizzBuzz".
Input format
First line contains an integer n.
output format
print N lines where each line is a string which is either fizz or buss or fizzbuss or an integer.
sample input 1
15
sample Output 1
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
"""
n = int(input())
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)