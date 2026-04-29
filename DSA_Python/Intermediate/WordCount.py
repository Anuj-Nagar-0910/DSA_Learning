'''
Given a string, return the number of unique words in the string.
'''

def unique_word_count(s):
    return len(set(s.split()))


if __name__ == "__main__":
    s = "Hello World, how are you? Hello again!"
    print("String:", s)
    print("Unique Word Count:", unique_word_count(s))
