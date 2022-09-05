class Solution(object):
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        answer = []
        
        for x in nums:
            thesenums = nums.copy()
            thesenums.remove(x)
            for y in thesenums:
                if (y + x) == target:
                    answer = [nums.index(x), nums.index(y)]
                    break
            if not answer == []:
                break
        
        return answer
  
    print(twoSum([2,7,11,15], 9))
    
    
