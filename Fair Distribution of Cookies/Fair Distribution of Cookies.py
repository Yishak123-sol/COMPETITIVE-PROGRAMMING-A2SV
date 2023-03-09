class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort(reverse = True)
        def backtrack(i, people):
            if i >= len(cookies):
                return max(people)

            fair = float("inf")
            for idx, person in enumerate(people):
                people[idx] += cookies[i]
                if people[idx] < fair:
                    fair = min(fair, backtrack(i+1, people))
                people[idx] -= cookies[i]

            return fair

        return backtrack(0, [0 for _ in range(k)])
