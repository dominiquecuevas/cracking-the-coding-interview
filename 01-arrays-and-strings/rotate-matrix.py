'''
Given an image represented by an NxN matrix, 
where each pixel in the image is represented by an integer,
write a method to rotate the image by 90 degrees.
Can you do this in place?
'''
image = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12],
    [13,14,15,16]
]
'''
output = [
    [13, 9, 5, 1],
    [14, 10, 6, 2],
    [15, 11, 7, 3],
    [16, 12, 8, 4]
]

0,0 -> 3,0
0,1 -> 2,0
0,2 -> 1,0
0,3 -> 0,0

1,0 -> 3,1
1,1 -> 2,1
1,2 -> 1,1
1,3 -> 0,1
'''

def rotate_matrix(image):
    results = [[None]*len(image) for row in image]
    for r in range(len(image)):
        for c in range(len(image)):
            results[r][c] = image[len(image)-1-c][r]
    return results

print(rotate_matrix(image))

'''
time comlexity is O(n^2), where n is the width and height of matrix
space complexity is O(n^2)
'''