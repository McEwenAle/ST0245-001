def Suma_grupo(start, nums, target):
    if(start == len(nums)):
        return target == 0
        pass
    
    a = Suma_grupo(start +1, nums, target - nums[start])
    b = Suma_grupo(start +1, nums, target)
    return a or b


print(Suma_grupo(0,[2, 4, 8],10))