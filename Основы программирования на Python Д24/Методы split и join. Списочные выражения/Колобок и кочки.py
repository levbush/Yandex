print((lambda ans: ans[1:] if len(ans[1:]) == int(ans[0]) 
       else 'нечленораздельно')((lambda n, nums, words: str(n) + 
                                 ''.join([''.join(set(
                                     i for i in words[j] 
                                     if words[j].count(i) == nums[j])) 
                                          if len(set(i for i in words[j] 
                                                     if words[j].count(i) == 
                                                     nums[j])) == 1 else '' for 
                                          j in range(len(nums))])) 
                                (n := int(input()), [int(input()) 
                                                     for _ in range(n)], 
                                 [input() for _ in range(n)])))