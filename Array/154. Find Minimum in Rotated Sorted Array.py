def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        # Initialize left and right pointer
        left = 0
        right = len(nums) - 1
        
        # If the last element is greater than the first element then 
        # there is no rotation, hence array is already sorted
        # Thus the first element is the smallest element
        if nums[right] > nums[0]:
            return nums[0]
        
        # Binary search 
        while left <= right:
            
            # Find the mid element
            mid = left + (right - left)//2
            
            # If the mid element is greater than the next element,
            # then the mid + 1 element is the smallest
            if nums[mid] > nums[mid + 1]: 
                return nums[mid + 1]
            
            # If the mid element is smaller than the previous element,
            # then the mid element is the smallest
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            # If the mid elements's value is greater than the 0th element,
            # we are working with elements greater than nums[0],
            # therefore, the smallest element is to the left of mid
            if nums[mid] > nums[0]:
                left = mid + 1
                
            # If nums[0] is greater than the mid element,
            # then the smallest value is to the right of mid
            else:
                right = mid - 1
