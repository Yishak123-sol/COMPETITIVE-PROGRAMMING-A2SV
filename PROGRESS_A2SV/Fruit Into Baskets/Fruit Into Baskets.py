class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        left = right =  0
        max_fruit = 0 
        basket = defaultdict(int)

        for right in range(len(fruits)):

            basket[fruits[right]] += 1

            while len(basket) == 3:

                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1

            max_fruit = max(max_fruit, right-left+1)
            
        return max_fruit









