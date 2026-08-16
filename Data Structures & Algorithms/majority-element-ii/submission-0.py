class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = collections.defaultdict(int)
        for i in nums:
            count[i] = 1 + count.get(i,0)
        res = []
        for n in count:
            if count[n] > len(nums)//3:
                res.append(n)
        return res