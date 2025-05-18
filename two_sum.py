"""
1. Two sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

#the following is a O(n) solution

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        targets = {}#target[i] is the target for number in index i

        for i in range(len(nums)):
            current = nums[i]

            if targets.get(current,0):
                return [i, targets.get(current)-1]
            else:
                t = target - current
                targets[t] = i+1 

