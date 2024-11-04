class Solution:
    def compressedString(self, word: str) -> str:
        count = 1
        final=''
        for i in range(1,len(word)):
            if ((word[i] == word[i-1]) and (count<9)):
                count+=1
            else :
                final += str(count) + word[i-1]
                count = 1
        final +=  str(count) + word[-1]
        return final