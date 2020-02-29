def foo(nums):
    """
    O(n)
    ignore the 2 in O(2n) since it is constant
    """
    summed = 0
    product = 1
    for idx in range(len(nums)):
        summed += nums[idx]
    for idx in range(len(nums)):
        product *= nums[idx]
    return f"{summed}, {product}"

def print_pairs(nums):
    """
    runtime is O(n**2)
    """
    for idx in range(len(nums)):
        for idx_ in range(len(nums)):
            print(f"{nums[idx]}, {nums[idx_]}")

def print_unordered_pairs(nums):
    """
    nums = [0, 1, 2, 3, 4]
    at first iteration the inner loop only allows 1 less iteration upto n
    4 + 3 + 2 + 1 = 6
    the inner loop cuts the work in half roughly
    this is n*(n-1)/2
    1/2 is constant and -1 is insignificant
    which is O(n**2)
    """
    for idx in range(len(nums)):
        for idx_ in range(idx+1, len(nums)):
            print(f"{nums[idx]}, {nums[idx_]}")
