class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        skill.sort()

        left = 0
        right = len(skill)-1
        target = skill[left] + skill[right]
        total = 0

        while left < right:

            if skill[left] + skill[right] != target:
                return -1
            
            else:
                total += skill[left] * skill[right]
                right -= 1
                left += 1

        return total
