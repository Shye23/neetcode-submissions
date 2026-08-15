class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fMap = {}
        for i in nums:
            fMap[i] = 1 + fMap.get(i,0)
        arr = []
        for num, cnt in fMap.items():
            arr.append([cnt,num])
        arr.sort()

        res=[]
        while len(res) < k:
            res.append(arr.pop()[1])
        return res