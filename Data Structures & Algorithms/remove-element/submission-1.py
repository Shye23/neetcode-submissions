class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new = []
        for n in nums:
            if n != val:
                new.append(n)
        for i in range(len(new)):
            nums[i] = new[i]
        return len(new)