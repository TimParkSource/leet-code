nums = [2,7,11,15]
target = 9

def twoSum(nums, target):
    #less_than_target = list(filter(lambda x: x <= target, nums))
    output = [None,None]
    for x in range(len(nums)):
        ele = target - nums[x]
        nums[x] = None #Prevents double counting current index
        if(nums.count(ele)):
            output[0] = x
            output[1] = nums.index(ele)
            print(output)
            return

twoSum(nums, target)

    