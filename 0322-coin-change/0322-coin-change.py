class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if amount == 0:return 0
        
        dp = [0]*(amount+1)
        for curr_amount in range(1, len(dp)):
            temp = []
            for coin in coins:
                if curr_amount - coin < 0:
                    continue
                    
                if dp[curr_amount-coin] < 0:
                    continue
                
                temp.append(dp[curr_amount-coin] + 1)
                
            if len(temp) > 0:
                dp[curr_amount] = min(temp)
            else:
                dp[curr_amount] = -1
        
        return dp[len(dp)-1]