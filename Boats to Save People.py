class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people = sorted(people)
        count = 0
        left_pointer = 0
        right_pointer = len(people)-1
        
        
        while left_pointer <= right_pointer:
                
            if people[right_pointer] + people[left_pointer] > limit:
                right_pointer -= 1
                count += 1

            else:
                right_pointer -= 1
                left_pointer += 1
                count += 1

        return count
