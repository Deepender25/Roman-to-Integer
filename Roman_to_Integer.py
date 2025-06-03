class Solution(object):
    def romanToInt(self, s):
        n = []
        li = [str(i) for i in s]
        ref = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in li:
            n.append(ref[i])
        for i in range(len(n)-1):
            if n[i] < n[i+1]:
                n[i+1] = n[i+1] - n[i]
                n[i] = 0
        return sum(n)
