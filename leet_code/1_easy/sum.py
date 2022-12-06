nums = [2,7,11,15]
target=9
for i in range(0,len(nums)):
     for j in range(i+1,len(nums)):

        number= nums[i] + nums[j]
        if number == target:
         print([i,j]) 

