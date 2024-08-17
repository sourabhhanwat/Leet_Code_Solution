class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp_dict = {}
        n = len(nums)

        for i in range(n):
            item = target - nums[i]
            if item in temp_dict:
                return [temp_dict[item], i]
            temp_dict[nums[i]] = i
        
        return []