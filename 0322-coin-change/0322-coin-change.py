class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if amount == 0:return 0
        self.memo = {}
        self.dp(amount, coins)
        
        return self.memo[amount] if self.memo[amount] != 1000000000 else -1
        
        
    def dp(self, amount, coins):
        
        if amount == 0:return 0
        
        
        temp = 1000000000
        for i in range(len(coins)):
            
            curr_amount = amount - coins[i]
            if curr_amount < 0:
                continue
                
            if curr_amount not in self.memo:
                self.memo[curr_amount] = self.dp(curr_amount, coins) + 1
                
            temp = min(self.memo[curr_amount], temp)

        self.memo[amount] = temp
        
        return self.memo[amount] 
       
        
        
        
        
        
        
        
        
