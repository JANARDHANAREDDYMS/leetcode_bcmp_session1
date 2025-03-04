class Solution:
    def sortColors(self, nums: List[int]) -> None:
        self.quicksort(nums, 0,len(nums)-1)
    
    def quicksort(self, nums: List[int], low: int, high: int) -> None:
        if low < high:
            p = self.partition(nums, low, high)
            self.quicksort(nums, low, p-1)
            self.quicksort(nums, p+1,high)

    def partition(self, nums: List[int], low: int, high: int) -> int:
        p = random.randint(low,high)
        nums[p], nums[high] = nums[high],nums[p]
        pivot = nums[high]
        print(p)
        slide = low -1
       
        for j in range(low,high):
            if nums[j]< pivot:
                slide +=1
                nums[j], nums[slide] = nums[slide],nums[j]
        nums[slide + 1], nums[high] = nums[high], nums[slide + 1] 
        print(nums)
        return slide+1

        

            
        