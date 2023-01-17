class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        row = len(mat)
        col = len(mat[0])


        if row * col != c * r:
            return mat

        new_matrix = [[] for i in range(r)]
        temp_matrix = []
        

        for ro in range(row):
            for cl in range(col):
                temp_matrix.append(mat[ro][cl])

        l = 0
        
        for index in range(r):

            col = 0
            
            while col < c:

                if l < len(temp_matrix):
                    print(index,l)
                    element = temp_matrix[l]
                    new_matrix[index].append(element)

                    l+=1


                col +=1
            

        return new_matrix
