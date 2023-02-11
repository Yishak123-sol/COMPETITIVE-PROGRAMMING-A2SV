class Solution:
    def compress(self, chars: List[str]) -> int:
        dic = {}
        ans = []
        
        for char in chars:
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1

        chars.clear()
        for value, key in dic.items():

            if int(key) > 1 and int(key) < 10:
                ans.append(value)
                ans.append(str(key))
            elif key == 1:
                ans.append(value)
            else:
                ans.append(value)
                for x in str(key):
                    ans.append(x)

        chars.extend(ans)
        return len(ans)
