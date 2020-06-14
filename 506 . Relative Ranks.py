"""
506. Relative Ranks
Easy

Given scores of N athletes, find their relative ranks and the people with
the top three highest scores, who will be awarded medals: "Gold Medal",
"Silver Medal" and "Bronze Medal".

"""
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
    	for i, (j,k) in enumerate(sorted(zip(nums,range(len(nums))), reverse = True)):
    		nums[k] = str(i+1) if i > 2 else ["Gold","Silver","Bronze"][i] + " Medal"
    	return nums
