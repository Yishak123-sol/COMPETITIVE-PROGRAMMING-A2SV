class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        distinct_factorial = set()
        for num in nums:
            divisor = 2
            
            while divisor * divisor <= num:
                while num%divisor == 0:
                    num //= divisor
                    
                    if divisor not in distinct_factorial:
                        distinct_factorial.add(divisor)
                divisor += 1
            
            if num > 1 and num not in distinct_factorial:
                distinct_factorial.add(num)
        
        return len(distinct_factorial)
                
                