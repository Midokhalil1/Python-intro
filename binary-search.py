# Binary search

from typing import List 

def search(nums: List[int], target: int) -> int:

    length = len(nums) -1 
    low, high = 0, length 

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target: