class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dict1={}
        # for i in nums:
        #     if i in dict1:
        #         dict1[i]+=1
        #     else:
        #         dict1[i]=1
        # sorted_dict = dict(sorted(dict1.items(), key=lambda item: item[1], reverse=True))
        # return list(sorted_dict.keys())[0:k]

        freq = Counter(nums)
        sorted_freq = sorted(freq.items(),key= lambda item: item[1], reverse=True)
        return [i[0] for i in sorted_freq[0:k]]
        
