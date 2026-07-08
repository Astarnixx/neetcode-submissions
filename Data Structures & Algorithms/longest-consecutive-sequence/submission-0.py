class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums = sorted(list(set(nums)))
        length = len(nums)
        ans = 1
        current_streak = 1
        for i in range(1, length):
            if nums[i] == nums[i-1] + 1:
                current_streak += 1
            else:
                current_streak = 1
            ans = max(ans, current_streak)
        return ans