
class Solution:
    def printVertically(self, s: str) -> List[str]:


        s_list = s.split()
        max_length = 0

        for index in range(len(s_list)):
            max_length = max(max_length, len(s_list[index]))


        columend_list = [""] * max_length

        for char_index in range(max_length):
            for word in s_list:

                if char_index >= (len(word)):
                    columend_list[char_index] += " "

                else:
                    columend_element = word[char_index]
                    columend_list[char_index] += columend_element
            
            columend_string = columend_list[char_index].rstrip()
            columend_list[char_index] = columend_string

        return columend_list
