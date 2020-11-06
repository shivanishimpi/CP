for _ in range(int(input())):
    nums = list(map(int, input().split(',')))
    print(nums)
    validNums = []
    if sum(nums) == 0:
        print(validNums)
    else:
        nums = (sorted(nums))
        for i in range(len(nums)):
            if nums[i] ==0:
                print(nums)
                print(i)
                if abs(nums[i-1]-nums[i]) == abs(nums[i]-nums[i+1]):
                    validNums.append(nums[i-1])
                    validNums.append(nums[i])
                    validNums.append(nums[i-1])
            print(validNums)
