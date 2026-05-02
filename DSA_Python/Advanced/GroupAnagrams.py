"""
Problem Description
Given an array of strings, group anagrams together.

Input format
First line contains an integer N - Number of String.

Second line contains N strings.

Output format
Print each group on a separate line.

For each group print all anagrams of a group on a single line.

Note:The order of your output does not matter.

Sample Input 1
6

eat tea tan ate nat bat

Sample Output 1
ate eat tea

nat tan

bat

Sample Input 2
6

arun aurn desk kept kpet kkpk

Sample Output 2
arun aurn

kept kpet

kkpk

desk
"""
def groupAnagrams(n, array):
    anagram_dict = {}
    for word in array:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    
    result = []
    for group in anagram_dict.values():
        result.append(' '.join(group))
    
    return result

if __name__ == "__main__":
    n = int(input())
    array = input().split()
    output = groupAnagrams(n, array)
    for group in output:
        print(group)