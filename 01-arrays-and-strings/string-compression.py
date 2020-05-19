'''
Implement a method to perform basic string compression using the counts of repeted characters.
If the "compressed" string would not become smaller than the original string, 
your method should return the original string.

input: 'aabcccccaaa'
        012345678910
output: 'a2b1c5a3'
input: 'lmaooo'
    -> 'l1m1a1o3'
output: 'llmaooo'
'''

'''
edge case return ~
make an empty list to add to
pointer index for start
pointer for end start at 1
loop until end pointer is equal to length of input string
    check if start is equal to end
        increment end by 1
    if not:
        append start element to list
        append different of end and start
        make start equal to end
        make end = start + 1
    if end is length of input
        append start element
        append diff end and start
if compressed not greater than input string
    return input string
return joined elements in list for compressed string
'''
'''
input: 'aabcccccaaa'
        012345678910
        [a, 2, b, 1]
output: 'a2b1c5a3'
input: 'lmaooo'
    -> 'l1m1a1o3'
output: 'llmaooo'

input: 'o'
output : 'o'
'''
def string_compression(string) -> str:
    if len(string) <= 2:
        return string
    compressed_list = []
    start = 0
    end = 1
    while end < len(string):
        if string[start] != string[end]:
            compressed_list.append(string[start])
            compressed_list.append(str(end - start))
            start = end
            end = start + 1 
        else:
            end += 1
        if end == len(string):
            compressed_list.append(string[start])
            compressed_list.append(str(end - start))
    compressed = ''.join(compressed_list)
    if len(string) <= len(compressed_list):
        return string
    else:
        return compressed

input = 'aabcccccaaa'
print(string_compression(input))

input = 'lmaooo'
print(string_compression(input))

input = 'oh'
print(string_compression(input))

input = 'CCCCCCHHHHHHHHHHHHOOOOOO'
print(string_compression(input))