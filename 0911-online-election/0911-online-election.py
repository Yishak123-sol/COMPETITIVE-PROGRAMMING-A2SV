class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        
        self.persons = persons
        self.times = times
        
        hashmap = defaultdict(int)
        self.leading = defaultdict(int)
        maxval = 0
        curr = 0
        for i in range(len(self.persons)):
            hashmap[self.persons[i]] += 1
            if hashmap[self.persons[i]] >= maxval:
                self.leading[i] = self.persons[i]
                curr = self.persons[i]
            else:
                self.leading[i] = curr
            maxval = max(maxval, hashmap[self.persons[i]])
            
    def q(self, t: int) -> int:
        key = bisect.bisect_right(self.times, t)
        return self.leading[key-1]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)