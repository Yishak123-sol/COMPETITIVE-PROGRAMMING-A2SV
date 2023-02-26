class DataStream:

    def __init__(self, value: int, k: int):
        
        self.k = k
        self.temp = [0, value]

    def consec(self, num: int) -> bool:
        if self.temp[-1] == num:
            self.temp[0] += 1
        else:
            self.temp[0] = 0
            
        return False if self.temp[0] < self.k else True
    
#     def __init__(self, value: int, k: int):

#         self.k = k
#         self.value = value
#         self.count = 0


#     def consec(self, num: int) -> bool:

#         if num == self.value:
#             self.count += 1

#         else:
#             self.count = 0

#         if self.k <= self.count:
#             return True
        
#         return False

# # Your DataStream object will be instantiated and called as such:
# # obj = DataStream(value, k)
# # param_1 = obj.consec(num)