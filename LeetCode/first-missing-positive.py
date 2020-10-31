"""
Given an unsorted integer array nums, find the smallest missing positive integer.

Follow up: Could you implement an algorithm that runs in O(n) time and uses constant extra space.?
Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1

#SOLUTION
for _ in range(int(input())):
    nums = list(map(int, input().split(' ' )))
    if len(nums)!=0:
        minimum = min([i for i in nums if i>0])
        maximum = max([i for i in nums if i>0])
        val = 1
        if maximum >= minimum and minimum ==1:
            #print(f'min,max:{minimum, maximum}')
            val+=1
            #print(f'val:{val}')
            if val == maximum:
                #print(f'nums:{nums}')
                val+=1
                nums.append(val)
                print(val)
                #print(f'appendedNums:{sorted(nums)}')
            if val not in nums:
                #print(f'nums:{nums}')
                nums.append(val)
                print(val)
                #print(f'appendedNums:{sorted(nums)}')
        if minimum !=1:
            #print(f'nums:{nums}')
            nums.append(val)
            print(val)
            #print(f'appendedNums:{sorted(nums)}')
    else:
        print(1)
"""
#SOLUTION
for _ in range(int(input())):
    nums = list(map(int, input().split(' ')))
    for i in range(1,2**31-1):
        if i not in nums:
            print(i)
            break
