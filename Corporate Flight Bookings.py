class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        output = [0] * n
        for first, last, seat in bookings:
            output[first - 1] += seat
            if last < n:
                output[last] -= seat
        print(output)
        for i in range(1, n):
            output[i] = output[i-1] + output[i]
            
        return output
