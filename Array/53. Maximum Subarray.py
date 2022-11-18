def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_subarray = nums[0]
        max_subarray = nums[0]
        
        for i in range(1, len(nums)):
            current_subarray = max(nums[i], current_subarray + nums[i])
            if current_subarray > max_subarray:
                max_subarray = current_subarray
                
        return max_subarray
