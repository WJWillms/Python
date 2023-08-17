class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        summie = []
        for i, x in enumerate(nums):
            for j, y in enumerate(nums[i+1:], start=i+1):
                if x + y == target:
                    summie.append(i)
                    summie.append(j)
        return summie



#You can use the enumerate() function to iterate over a sequence (like a list)
#while also keeping track of the index of each element. In the context of the
#twoSum function, using enumerate() allows you to iterate through the nums list 
#and simultaneously track the index of the current element.		
		
#Index Tracking: The purpose of the function is to find two elements
#in the nums list that add up to the given target. In order to correctly 
#compare pairs of elements and record their indices, you need to keep track 
#of the index of each element. Using enumerate() provides an elegant way to achieve this.

#Starting Index: The inner loop (for j, y in enumerate(nums[i+1:], start=i+1)) 
#starts from i+1 to avoid comparing an element with itself and to prevent 
#duplicate pairs. By starting the inner loop from i+1, you ensure that you're 
#comparing each element with all subsequent elements.