class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        
        can_be = False # to chek weather a whole word can be formed from chars

        for word in words:
            temp = list(chars)
            
            for ch in word:
                if ch not in temp:
                    can_be = False
                    break
                    
                else:
                    temp.remove(ch)
                    can_be = True
            if can_be:
                res += len(word)
                
        return res