class Solution:
    def sortSentence(self, s: str) -> str:
        dic = {}
        for i in s.split():
            dic[i[-1]] = i[:-1]
            
        final_sentence = []
        for num,word in sorted(dic.items()):
            final_sentence.append(word)
            
        return ' '.join(final_sentence)
