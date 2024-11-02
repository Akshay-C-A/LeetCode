import numpy
class Solution:
    def trap(self, height: List[int]) -> int:
        maxh=height[0]
        r=[]
        r.append(maxh)

        for i in range(1, len(height)):
            if height[i] > maxh:
                maxh=height[i]
            r.append(maxh)
            
        height.reverse()

        maxh=height[0]
        l=[]
        l.append(maxh)

        for i in range(1,len(height)):
            if height[i] > maxh:
                maxh=height[i]
            l.append(maxh)

        l.reverse()
        height.reverse()
        minh=[min(i,j) for i,j in zip(r,l)]
        water=list(numpy.array(minh)-numpy.array(height))
        count=0
        for i in water:
            count+=i
        return count


    



            