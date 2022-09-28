class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        length_OFanswer = (m * n)
        answer_list = []
        main_index = 0

        while length_OFanswer > len(answer_list):
            sub_index = main_index
            while len(answer_list) < length_OFanswer and sub_index < n:
                answer_list.append(matrix[main_index][sub_index])
                sub_index += 1

            end_col = main_index + 1
            while len(answer_list) < length_OFanswer and end_col < m:
                answer_list.append(matrix[end_col][n-1])
                end_col += 1

            down_row = n-2
            while len(answer_list) < length_OFanswer and down_row >= main_index:
                answer_list.append(matrix[m-1][down_row])
                down_row -= 1

            first_col = m-2
            while len(answer_list) < length_OFanswer and first_col > main_index:
                answer_list.append(matrix[first_col][main_index])
                first_col -= 1

            main_index += 1
            n -= 1
            m -= 1

        return answer_list
