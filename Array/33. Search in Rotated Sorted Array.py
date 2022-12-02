def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            # define the pivot
            mid = start + (end - start)//2
            
            # return pivot if it is target
            if nums[mid] == target:
                return mid
            
            # if the pivot is more than the 1st element
            elif nums[mid] >= nums[start]:
                # if target in non-rotated array
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                # otherwise
                else:
                    start = mid + 1
                    
            # if the pivot is less than the 1st element
            else:
                # if target in non-rotated array
                if target > nums[mid] and target <= nums[end]:
                    start = mid + 1
                # otherwise
                else:
                    end = mid - 1
                    
        return -1
