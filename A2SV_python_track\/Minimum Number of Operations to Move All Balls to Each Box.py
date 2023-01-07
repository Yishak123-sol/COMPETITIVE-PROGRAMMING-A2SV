class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        min_operation = []

        for i in range(len(boxes)):

            total = 0

            for j in range(len(boxes)):

                if boxes[j] == "1":

                    if i < j:
                        total += (j -i)

                    else:
                        total += (i - j)

            min_operation.append(total)

        
        return min_operation
