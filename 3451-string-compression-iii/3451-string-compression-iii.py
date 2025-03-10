class Solution:
    def compressedString(self, word: str) -> str:
        comp_num = 0
        same_word = 1
        comp_word = ''
        if len(word) == 1:
            comp_word = f"{same_word}{word[0]}"
            return comp_word
            
        while comp_num < len(word)-1:
            if word[comp_num] != word[comp_num+1]:
                comp_word += f"{same_word}{word[comp_num]}"
                same_word = 1
            else:
                if same_word >= 9:
                    comp_word += f"{same_word}{word[comp_num]}"
                    same_word = 0
                same_word += 1
            comp_num += 1

        if len(word) > 1:
            if word[comp_num-1] != word[comp_num]:
                same_word = 1
                comp_word += f"{same_word}{word[comp_num]}"
            else:
                comp_word += f"{same_word}{word[comp_num]}"
        return comp_word
