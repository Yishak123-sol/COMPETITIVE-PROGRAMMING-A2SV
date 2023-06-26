class Solution(object):
    def minimumTotal(self, triangle):   
        for i in range(len(triangle)):
            for j in range(len(triangle[i])):
                triangle[i][j] += (min( triangle[i-1][j] if j < len(triangle[i-1]) else +float('inf'), triangle[i-1][j - 1] if (j - 1 >=0) else +float('inf')) if (i - 1 >=0) else 0)
        return min(triangle[-1])