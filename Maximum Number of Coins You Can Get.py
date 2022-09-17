class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        piles.reverse()
        index = 1
        sum_ofMy_coins = 0
        for i in range(int(len(piles)/3)):
            s = piles[index]
            sum_ofMy_coins += s
            index += 2
            
        return sum_ofMy_coins
