from typing import List

#题最长连续递增序列(674)
def findLengthOfLCIS(self, nums: List[int]) -> int:
    if not nums: return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = 1
    return max(dp)


#题最长回文子序列(516)
def longestPalindromeSubseq(self, s: str) -> int:
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for i in range(n, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
    return dp[0][-1]

#题编辑距离(72)
def minDistance(self, word1, word2):
	m=len(word1)
	n=len(word2)
	dp=[[0 for _ in range(n+1)] for _ in range(m+1)]
	for i in range(n+1):
		dp[0][i]=i
	for j in range(m+1):
		dp[j][0]=j
	for i in range(1,m+1):
		for j in range(1,n+1):
			if word1[i-1]==word2[j-1]:
				dp[i][j]=dp[i-1][j-1]
			else:
				dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
	return dp[-1][-1]

#题打家劫舍(198)
def rob(self, nums):
	if(not nums):
		return 0
	if len(nums)==1:
		return nums[0]
	n=len(nums)
	dp=[0]*n
	dp[0]=nums[0]
	dp[1]=max(nums[0],nums[1])
	for i in range(2,n):
		dp[i]=max(dp[i-2]+nums[i],dp[i-1])
	return dp[-1]


#题打家劫舍II(213)
def rob(self, nums: List[int]) -> int:
    if not nums:
        return 0
    elif len(nums) <= 2:
        return max(nums)

    def helper(nums):
        if len(nums) <= 2:
            return max(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]

    return max(helper(nums[1:]), helper(nums[:-1]))
