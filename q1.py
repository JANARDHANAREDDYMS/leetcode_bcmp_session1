class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}
        for i, value in enumerate(numbers):
            dif = target - value
            if dif in dict:
                return [dict[dif] + 1, i + 1]
            dict[value] = i
        return []
