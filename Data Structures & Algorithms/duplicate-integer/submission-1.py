class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        
        for i in range(len(nums)):
            seen.add(nums[i])
        print(len(seen))
        print(len(nums))
        if len(seen)!=len(nums):
            return True
        return False

