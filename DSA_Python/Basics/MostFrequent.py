"""
Problem Description
You are given a string which comprises lower case alphabets (a-z), upper case alphabets (A-Z), numbers, (0-9) and special characters like !,-.; etc.

You are supposed to find out which character occurs the maximum number of times and its occurrence count in the given string. If two characters occur equal number of times, you have to output the character with the lower ASCII value.

For example, if your string was: aaaaAAAA, your output would be: A 4, because A has lower ASCII value than a.

Input format
One line of input containing the string S.

Output format
You will have to output two space separated values:

The character which occurs the maximum number of times.

The number of its occurrence.

Sample Input 1
Statements are unique.

Sample Output 1
e 4

Constraints
1 <= |S| <= 100
using a dictionary to count the frequency of each character in the string. We can iterate through the string and update the count for each character in the dictionary. After counting, we can find the character with the maximum frequency and handle ties by comparing ASCII values.
"""

# def mostFrequent(S):
#     char_count = {}
#     for char in S:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1

#     max_char = None
#     max_count = 0

#     for char, count in char_count.items():
#         if count > max_count or (count == max_count and (max_char is None or char < max_char)):
#             max_char = char
#             max_count = count

#     return f"{max_char} {max_count}"    
# S = "Statements are unique."
# print(mostFrequent(S))
from typing import Tuple

def mostFrequent(s: str) -> Tuple[chr, int]:
    count_char = {}
    for char in s:
        if char in count_char:
            count_char[char] += 1
        else:
            count_char[char] = 1
    
    max_count = 0
    lower_ascii = ''
    for chars, count in count_char.items():
        if count > max_count:
            count = max_count
            lower_ascii = chars
        if count == max_count:
            if chars < lower_ascii:
                lower_ascii = chars
                print(lower_ascii, max_count)
    return (lower_ascii, max_count)

S = "AAA aaa"
print(mostFrequent(S))