#两数之和(1)
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

#三数之和(15)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_len = len(nums)
        if nums_len < 3:
            return []
        res_ls = []
        nums.sort()
        for i in range(nums_len):
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i-1]: continue
            l,r = i+1,nums_len-1
            while l<r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res_ls.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l<r and nums[l-1] == nums[l]: l += 1
                    while l<r and nums[r] == nums[r+1]: r -= 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
        return res_ls

#最接近的三数之和(16)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res_sum = sum(nums[:3])
        min_sub = abs(res_sum-target)
        nums.sort()
        for i in range(len(nums)):
            l,r = i+1, len(nums)-1
            while l<r:
                if nums[i] + nums[l] + nums[r] == target:
                    return target
                else:
                    if abs(nums[i] + nums[l] + nums[r]-target) < min_sub:
                        res_sum = nums[i] + nums[l] + nums[r]
                        min_sub = abs(res_sum-target)
                    if nums[i] + nums[l] + nums[r] < target:
                        l += 1
                    else:
                        r -= 1
        return res_sum

#四数之和(18)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res_ls = []
        nums_len = len(nums)
        if nums_len < 4:
            return res_ls
        if nums_len == 4:
            if sum(nums) == target: res_ls.append(nums)
            return res_ls
        for i in range(nums_len-3):
            if i > 0 and nums[i-1]==nums[i]: continue
            for j in range(i+1,nums_len-2):
                if j > i + 1 and nums[j-1]==nums[j]: continue
                l,r = j+1,nums_len-1
                while l<r:
                    if nums[i] + nums[j] + nums[l] + nums[r] == target:
                        res_ls.append([nums[i],nums[j],nums[l],nums[r]])
                        l += 1
                        r -= 1
                        while l<r and nums[l] == nums[l-1]: l+=1
                        while l<r and nums[r] == nums[r+1]: r-=1
                    elif nums[i] + nums[j] + nums[l] + nums[r] < target:
                        l += 1
                    else:
                        r -= 1
        return res_ls

#字母异位词分组(49)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        strs_dic = defaultdict(list)
        for stro in strs:
            key = ''.join(sorted(list(stro)))
            strs_dic[key] += stro.split(',')
        return [v for v in strs_dic.values()]

#直线上最多的点数(149)
class Solution:
    def maxPoints(self,points):
        if len(points) <= 1:
            return len(points)
        res = 0
        from collections import defaultdict
        for i in range(len(points)):
            record = defaultdict(int)
            samepoint = 0
            for j in range(len(points)):
                if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                    samepoint += 1
                else:
                    record[self.get_Slope(points,i,j)] += 1
            for v in record.values():
                res = max(res, v+samepoint)
            res = max(res, samepoint)
        return res
    def get_Slope(self,points,i,j):
        if points[i][1] - points[j][1] == 0:
            return float('Inf')
        else:
            return (points[i][0] - points[j][0]) / (points[i][1] - points[j][1])


#存在重复元素2(219)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_set = set()
        for i in range(len(nums)):
            if nums[i] in nums_set:
                return True
            nums_set.add(nums[i])
            if len(nums_set) == k + 1:
                nums_set.remove(nums[i - k])
        return False

#存在重复元素3(220)
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t==0:
            if len(nums) == len(set(nums)):
                return False
            else:
                return True
        for i in range(len(nums)):
            for j in range(i+1,i+1+k):
                if j >= len(nums): break
                if abs(nums[i]-nums[j]) <= t:
                    return True
        return False

#回旋镖的数量(447)
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        from collections import Counter
        def f(x1,y1):
            point_dic = Counter((x2-x1)**2+(y2-y1)**2 for x2,y2 in points)
            return sum(t*(t-1) for t in point_dic.values())
        return sum(f(x,y) for x,y in points)

#四数相加2(454)
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        from collections import Counter
        search_dic = Counter()
        for i in range(len(C)):
            for j in range(len(D)):
                search_dic[C[i]+D[j]] += 1
        res = 0
        for i in range(len(A)):
            for j in range(len(B)):
                find_value = 0-(A[i]+B[j])
                if find_value in search_dic:
                    res += search_dic[find_value]
        return res



