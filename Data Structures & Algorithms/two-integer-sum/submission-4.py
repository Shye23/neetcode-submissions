class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumMap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in sumMap and sumMap[diff] != i:
                return [sumMap[diff],i]
            sumMap[num] = i
        return []