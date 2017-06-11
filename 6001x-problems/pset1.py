# pset1.py
# Aspen Hollyer
# June 3, 2017


# PROBLEM 1
# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string
# s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s =
# 'azcbobobegghakl', your program should print:
# Number of vowels: 5

s = 'azcbobobegghakl'
num_vowels = 0

for c in s:
    if c == 'a' or c == 'e' or c =='i' or c == 'o' or c =='u':
        num_vowels += 1
print("Number of vowels:", num_vowels)


# PROBLEM 2
# Assume s is a string of lower case characters.
# Write a program to print the number of times the string 'bob' occurs in s.
# For example, if s = 'azcbobobegghakl', then your program should print
# Number of times bob occurs is: 2

num_bobs = 0

for i in range(len(s) - 2):
    if s[i:i + 3] == 'bob':
            num_bobs += 1
print("Number of times bob occurs is:", num_bobs)


# PROBLEM 3
# Assume s is a string of lower case characters.
#
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
#
# Longest substring in alphabetical order is: abc
#
# Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.

s = 'abcdefghijklmnopqrstuvwxyz'
s = 'gskolchm'

longest = s[0]
temp = s[0]

if list(s) == sorted(s):
    print("Longest substring in alphabetical order is:", s)
else:
    for c in s[1:]:
        if c >= temp[-1]:
            temp += c
            print(temp)
        else:
            if len(temp) > len(longest):
                longest = temp
            temp = c
    if len(temp) > len(longest):
            longest = temp
    print("Longest substring in alphabetical order is:", longest)
