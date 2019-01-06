'''
In a array A of size 2N, there are N+1 unique elements, 
and exactly one of these elements is repeated N times.

Return the element repeated N times.
'''

class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        #we should define N first 
        N = len(A)/2
        
        #Let's create a collection which returns a dictionary of the keys and values
        
        count = collections.Counter(A)
        
        for k, v in count.items():
            if v == N:
                 return k
        return 0
            