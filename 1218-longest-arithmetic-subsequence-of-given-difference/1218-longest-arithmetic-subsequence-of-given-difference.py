class Solution:
	def longestSubsequence(self, arr: List[int], difference: int) -> int:
		dp = {}
		for i in arr:
			dp[i] = 1
		seen = set()
		for i in range(1, len(arr)):
			seen.add(arr[i - 1])
			if arr[i] - difference in seen:
				dp[arr[i]] = 1 + dp[arr[i] - difference]
                
		return max(dp.values())