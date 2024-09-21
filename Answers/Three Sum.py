def three_sum(nums):
    nums.sort()  # Sort the array first
    result = []
    
    for i in range(len(nums) - 2):
        # Avoid duplicates for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                # Avoid duplicates for the second element
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Avoid duplicates for the third element
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                # Move both pointers after finding a valid triplet
                left += 1
                right -= 1
            elif total < 0:
                left += 1  # Need a larger sum
            else:
                right -= 1  # Need a smaller sum
    
    return result

# Example usage:
nums = [-1, 0, 1, 2, -1, -4]
triplets = three_sum(nums)
print(triplets)