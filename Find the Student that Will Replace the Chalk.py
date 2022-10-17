class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)
        for index, value in enumerate(chalk):
            if k < value:
                return index
            k -= value
            
