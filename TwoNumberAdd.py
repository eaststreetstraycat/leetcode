nums = input("请输入数组")
nums = [int(n) for n in nums.split()]
target = int(input("请输入目标值"))
numbermap = {}
for index,num in enumerate(nums):
    another_num = target - num
    if another_num in numbermap:
        print(numbermap[another_num],index)
    numbermap[num] = index