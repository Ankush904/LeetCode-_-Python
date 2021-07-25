from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                if target == sum:
                    print("\n" , "The numbers are ",nums[i]," & ",nums[j])
                    return[i,j]  
if __name__=="__main__":
    s=Solution()
    nums=[3,2,4]
    print(s.twoSum(nums,7))
