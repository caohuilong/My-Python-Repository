class Solution_Initial:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        i = 0
        for iterms1 in nums:
            count = 1
            i += 1
            for iterms2 in nums[i:]:
                if iterms1 < iterms2:
                    iterms1 = iterms2
                    count += 1
            if res < count:
                res = count
        return res


class Solution_Brute_Force:
    def checkMonotonic(self, temp):   #判断temp是否是递增序列
        flag = True
        for k in range( len( temp ) - 1 ):
            if temp[k] >= temp[ k + 1 ]:      #比较k和k+1之间的大小，只要有一个不满足就跳出循环，并return False
                flag = False
                break
        return flag
    def lengthOfLIS(self, nums):
        #找出所有的子序列
        res = 0
        i = pow(2, len(nums)) - 1       #对于有n个数的列表，会有2^n-1种子序列
        while i > 0:
            length = 0
            temp = []
            for j in range(len(nums)):   #将i对应的子序列存储到temp中
                if i & (1 << j):
                    length += 1
                    temp.append(nums[j])
            if self.checkMonotonic(temp) and res < length:      #判断temp是否递增且其长度是否比res大
                res =length
                print(temp)
            i -= 1
        return res

class Solution_DP:      # Dynamic Programing
    def lengthOfLIS(self, nums):
        dp = []     # 用来存放到当前元素的最长子序列
        if nums == []:      # 判断输入是否为空,输入为空直接返回0
           return 0
        for i in range(len(nums)):      # 遍历整个列表nums
            dp.append(1)        # 读一个元素就在dp列表尾加一个元素
            for j in range(i):      # 遍历第i个元素前面的元素
                if nums[i] > nums[j] and dp[i] < dp[j] + 1: # 如果i元素比它前面的j元素大，且j元素前面没有比j更长的子序列
                    dp[i] = dp[j] + 1
        print (dp)
        return max(dp[:])

class Solution_DP_BS:      # Dynamic Programing with Binary Search
    def Binary_Search(self,dp,n):
        lo = 0
        hi = len(dp) - 1
        while lo < hi:
            if n > dp[(lo + hi)//2]:
                lo = (lo + hi)//2 + 1
            else:
                hi = (lo + hi)//2
        return hi
    def lengthOfLIS(self, nums):
        if nums == []:
            return 0
        dp = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                j = self.Binary_Search(dp,nums[i])
                dp[j] = nums[i]
        # print (dp)
        return len(dp)




def stringToIntegerList(input):
    import json
    return json.loads(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line)
            # ret = Solution_Initial().lengthOfLIS(nums)
            # ret = Solution_Brute_Force().lengthOfLIS(nums)    #O(2^n)
            # ret = Solution_DP().lengthOfLIS(nums)         # O(n^2)
            ret = Solution_DP_BS().lengthOfLIS(nums)        # O(n log n)
            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
