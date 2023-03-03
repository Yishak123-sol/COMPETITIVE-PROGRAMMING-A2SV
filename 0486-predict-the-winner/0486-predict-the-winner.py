class Solution:
    def playerOneScore(self, nums, left, right, turn, memo):
        if left > right:
            return 0

        if (left, right, turn) in memo:
            return memo[(left, right, turn)]

        choice1 = self.playerOneScore(nums, left+1, right, -turn, memo)
        choice2 = self.playerOneScore(nums, left, right-1, -turn, memo)
        
        if turn == 1:
            result = max(choice1+nums[left], choice2+nums[right])
        else:
            result = min(choice1, choice2)
        
        memo[(left, right, turn)] = result
        return result
        
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        totalScore = sum(nums)
        memo = {}

        p1_score = self.playerOneScore(nums, 0, n-1, 1, memo)
        p2_score = totalScore - p1_score
        
        return p1_score >= p2_score

