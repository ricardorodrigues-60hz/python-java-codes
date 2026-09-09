class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            tmp = []
            while i > 0:
                tmp.append(i % 10)
                i //= 10
                print(tmp)
            res.extend(tmp[::-1])
        return res


nums = [13, 25, 83, 77]
x = Solution()
x.separateDigits(nums)