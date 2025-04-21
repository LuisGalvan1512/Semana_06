from collections import deque

def rotate_array(nums, k):
    if not nums or k <= 0:
        return nums

    n = len(nums)

    queue = deque(nums)

    for _ in range(k):
        value = queue.pop()
        queue.appendleft(value)

    return list(queue)

#TEST

print(rotate_array([1, 2, 3, 4, 5, 6, 7], 3))
# Output: [5, 6, 7, 1, 2, 3, 4]

print(rotate_array([10, 20, 30], 1))
# Output: [30, 10, 20]

print(rotate_array([1], 10))
# Output: [1]

print(rotate_array([], 3))
# Output: []

print(rotate_array([4, 5, 6, 7], 4))
# Output: [4, 5, 6, 7]