#E1, sum two nums.
nums = [0,4,3,0]
target = 0
t = len(nums)
for i in range(t):
    for j in range(t-(i+1)):
        j = j+(i+1)
        if nums[i] > target or nums[j] > target:
            print("Pass for: ", nums[i], nums[j])
            continue
        print("Checking: ", nums[i], nums[j])
        if (nums[i] + nums[j]) == target:
            print(f"[{i},{j}]")