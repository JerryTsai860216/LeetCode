class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #min/max函數找出字元加總的string
        str1,str2=min(strs),max(strs)
        i=0

        while i<len(str1):
        	if str1[i]!= str2[i]:
        		str1 = str1[:i]
        	i+=1
        return str1
        	