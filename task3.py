#两个数组的交集(349)
class Solution():
   def intersection_of_two_nums(self,nums1,nums2):
      nums1=set(nums1)
      return [i for i in nums1 if i in nums2]

res=Solution()
print(res.intersection_of_two_nums([1,2,2,1],[2,2]))

#两个数组的交集2(350)
class Solution():
   def intersection_of_two_nums(self,nums1,nums2):
      from collections import Counter
      nums1_dict=Counter(nums1)
      res=[]
      for num in nums2:
         if nums1_dict[num]>0:
            res.append(num)
            nums1_dict[num]-=1
      return res

res=Solution()
print(res.intersection_of_two_nums([1,2,2,1],[2,2]))

#快乐数(202)
class Solution():
   def ishappy(self,n:int)->bool:
      already=set()
      while n!=1:
         sum=0
         while n>0:
            temp=n%10
            sum+=temp**2
            n//=10
         if sum in already:
            return False
         else:
            already.add(sum)
         n=sum
      return True

res1=Solution()
print(res1.ishappy(19))

res2=Solution()
print(res2.ishappy(101))

#有效的字母异位词(242)
class Solution():
   def isAnagram(self,s:str,t:str)->bool:
      from collections import Counter
      s=Counter(s)
      t=Counter(t)
      if s==t:
         return True
      else:
         return False
#测试函数
s='anagram'
t='nagaram'
res=Solution()
print(res.isAnagram(s,t))

#单词规律(290)
class Solution():
   def wordpattern(self,s:str,pattern:str)->bool:
      s=s.split()
      n1=len(s)
      n2=len(pattern)
      if n1==n2:
         n=n1
         dic={}
         for i in range(0,n):
            if pattern[i] not in dic.keys():
               dic[pattern[i]]=s[i]
            else:
               if dic[pattern[i]]!=s[i]:
                  t=False
                  break
               else:
                   t = True
               return t

s = 'dog cat cat dog'
pattern = 'abba'
res = Solution()
print(res.wordpattern(s, pattern))

#同构字符串(205)
class Solution():
   def isIsomorphic(self,s:str,t:str)->bool:
      return list(map(t.index,t))==list(map(s.index,s))

s='egg'
t='add'
res=Solution()
print(res.isIsomorphic(s,t))
s='foo'
t='bar'
res=Solution()
print(res.isIsomorphic(s,t))

#根据字符出现频率排序(451)
class Solution():
   def frequencySort(self,s:str)->str:
      from collections import Counter
      s_dict=Counter(s)
      s=sorted(s_dict.items(),key=lambda item:item[1],reverse=True)
      res=''
      for key,value in s:
         res+=key*value
      return res

s='tree'
res=Solution()
print(res.frequencySort(s))

#搜索插入位置(35)
class Solution():
   def searchnum(self,nums,s:int)->int:
      dic={}
      n=len(nums)
      lst=[i for i in range(n)]
      for i in range(n):
         dic[nums[i]]=lst[i]
      if s in nums:
         return dic[s]
      else:
         if (nums[0]<nums[1] and s>nums[n-1]) or (nums[0]>nums[1] and s<nums[n-1]):
            return n
         else:
            for i in range(n-1):
               if (nums[0]<nums[1] and s>nums[i] and s<nums[i+1]) or (nums[0]>nums[1] and s<nums[i] and s>nums[i+1]):
                  return i+1
                  break

nums=[1,3,5,6]
s=5
res=Solution()
print(res.searchnum(nums,s))
nums=[1,3,5,6]
s=2
res=Solution()
print(res.searchnum(nums,s))
nums=[1,3,5,6]
s=7
res=Solution()
print(res.searchnum(nums,s))

#分割数组的最大值(410)
class Solution():
    def splitArray(self, nums,m: int) -> int:

        def helper(mid):
            res = tmp = 0
            for num in nums:
                if tmp + num <= mid:
                    tmp += num
                else:
                    res += 1
                    tmp = num
            return res + 1

        lo, hi = max(nums), sum(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if helper(mid) > m:
                lo = mid + 1
            else:
                hi = mid
        return lo

nums = [7,2,5,10,8]
m = 2
res=Solution()
print(res.splitArray(nums,m))

#有序数组的单一元素(540)
class Solution():
   def single_num(self,nums)->int:
      from collections import Counter
      nums=Counter(nums)
      n=len(nums)
      for i in range(n):
         if list(nums.values())[i]==1:
            return int(list(nums.keys())[i])

nums=[1,1,2,3,3,4,4,8,8]
res=Solution()
print(res.single_num(nums))
nums=[3,3,7,7,10,11,11]
res=Solution()
print(res.single_num(nums))

