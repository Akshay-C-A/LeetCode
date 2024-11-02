class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        for i in range(len(sentence)):
            if (sentence[i]==' '):
                if (sentence[i-1]==sentence[i+1]):
                    pass
                else:
                    return False

        return sentence[0]==sentence[-1]