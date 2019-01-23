#Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #simplest
        max_frequency_element=nums[0]
        max_frequency=int(len(nums)/2)
        dict_num={}
        for num in nums:
                # print(num,dict_num)
                if num not in dict_num:
                    dict_num[num]=1
                else:    
                    dict_num[num]+=1
                    if dict_num[num]>=max_frequency:
                        max_frequency=dict_num[num]
                        max_frequency_element=num
        # print(dict_num)
        return max_frequency_element
