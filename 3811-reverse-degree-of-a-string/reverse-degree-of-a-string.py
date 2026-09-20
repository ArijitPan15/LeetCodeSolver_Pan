
class Solution:
    def reverseDegree(self, s: str) -> int:
        total=0
        for index,char in enumerate(s):
            weight=26-(ord(char)-97)
            total+=weight*(index+1)
        return total