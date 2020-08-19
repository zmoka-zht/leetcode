#寻找众数(169)
class Solution1(object):
    def majorityElement(self, nums):
        list_1=[]
        n=len(nums)
        for i in range(n//2+1):
            if nums[i]  in list_1:
                i+=1
                continue
            else :
                list_1.append(nums[i])
                if nums.count(nums[i])>n//2:
                    return nums[i]

num_list=[2,2,1,1,1,2,2]
result= Solution1().majorityElement(num_list)
print(result)

#最大子序和(53)
class Solution2(object):
    def maxsubArray(list):
        list_1=[]
        dict={}
        s=0
        for i in range(0,len(list)-1):
            for j in range(i+1,len(list)+1):
                mysum=sum(list[i:j])
                list_1.append(mysum)
            t=max(list_1)
            dict[t]=s
            s+=1
            del list_1[:]
        m=max(dict.keys())
        print(str(m))
        flag=True
        while flag:
            for i in range(dict[m]+1,len(list)+1):
                sum_1=sum(list[dict[m]:i])
                if sum_1==m:
                    flag=False
                    return list[dict[m]:i]

list=[-2,1,-3,4,-1,2,1,-5,4]
result=Solution2.maxsubArray(list)
print(result)

#Pow(x，n) (50)
class Solution3(object):
    def pow(self, x, n):
        if n < 0:
            return 1/self.pow(x, -n)
        if n == 1:
            return x
        else:
            return x*self.pow(x, n-1)

result = Solution3().pow(2.1, 3)
print(result)

