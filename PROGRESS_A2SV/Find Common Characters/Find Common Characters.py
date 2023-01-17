class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        word = [0]*26
        commonchar_list = []

        for i in range(len(words[0])):

            index = ord(words[0][i]) - 97
            word[index] += 1

        for j in range(1, len(words)):

            temp_store = [0] * 26

            for letter_indx in range(len(words[j])):

                index = ord(words[j][letter_indx]) - 97
                temp_store[index] += 1


            for indx in range(26):
                word[indx] = min(word[indx], temp_store[indx])

        
        for indx in range(26):

            current = int(word[indx])

            if current > 0:
                for _ in range(current):

                    letter = chr(97+indx)
                    commonchar_list.append(letter)
        

        return commonchar_list
