class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0

        maxval=max(A)
        maxindex = A.index(maxval)

        firstone,secondone = True, True

        smlist = A[0:maxindex]
        biglist = A[maxindex+1:len(A)]
        #print biglist

        if sorted(smlist) == smlist and sorted(biglist,reverse=True) == biglist:
            #print 'Yes'
            return maxindex
        else:
            return 0
