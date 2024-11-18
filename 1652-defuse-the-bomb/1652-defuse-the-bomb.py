class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        new=[]
        l=len(code)

        if k==0:
            return [0]*l
            
        if k>0:
            for i in range(l):
                new.append(sum(code[(j+i)%l] for j in range(1,k+1)))
        elif k<0:
            for i in range(l):
                new.append(sum(code[(j+i)%l] for j in range(k,0)))

        return new
