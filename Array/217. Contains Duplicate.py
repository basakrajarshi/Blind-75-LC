def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        if len(nums) == 0 or len(nums) == 1: 
            return False
        
        """
        if len(set(nums)) == len(nums):
            return False
        
        return True
        """
        
        nums = sorted(nums)
        
        for i in range(len(nums)):
            if i == len(nums) - 1: break
            if nums[i] == nums[i+1]:
                return True
            
        return False
