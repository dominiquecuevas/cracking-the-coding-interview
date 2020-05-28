'''
Assume you have a method isSubstring which checks if one word is a substring of another. 
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring 
(e.g., "waterbottle" is a rotation of "erbottlewat")
'''

'''
s1 and s2 should be same length to be rotation - edge case to False
is_substring - s2 can be shorter than s1 "water"
should walk through each element in s1

have indexes for each word
check if s2's index element equal to s1 element

'''
s1 = 'waterbottle'
s2 = 'erbottlewat'


def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    if len(s1) == len(s2):
        return isSubstring(s1+s1, s2)
    return False