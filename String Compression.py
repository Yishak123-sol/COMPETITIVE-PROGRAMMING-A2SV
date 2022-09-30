class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        
        temporary = ""
        count = 0
        current = chars[0]
        for char in chars:
            if current == char:
                count += 1
            else:
                if count > 1:
                    temporary += (current + str(count))
                else:
                    temporary += current
                    
                count = 1
                current = char

        if count > 1:
            temporary += (current + str(count))

        else:
            temporary += current
            
        
        chars.clear()
        for char in temporary:
            chars.append(char)
        
        return len(chars)
