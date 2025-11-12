print('johnson' in 'Joe Johnson') # False, string johnson is not in string Joe Johnson (capitalization matters.)
print('sen' not in 'Joe Johnson') # True, string sen is not in Joe Johnson.
print('Joe J' in 'Joe Johnson') # True, Joe J appears at the start of Joe Johnson
print(5 in range(5)) # False, 5 does not appear in range(5)
                     # because it prints (0,1,2,3,4) no 5 
print(5 in range(6)) # True, 5 does apear in range(6)
                     # since it prints (0,1,2,3,4,5) 5 is at the last index
print(5 not in range(5, 10)) # False, 5 is in range(5,10)
                             # because it prints
                             # (5,6,7,8,9)
print(0 in range(10, 0, -1)) # False, because it prints
                             # (10,9,8,7,6,5,4,3,2,1) 0 is exluded in range(10,0,-1)
print(4 in {6, 5, 4, 3, 2, 1}) # True, the integer 4 is in the set.
print({1, 2, 3} in {1, 2, 3}) # False, It prints False because Python checks for elements, 
                              #not equality between whole sets.
print({3, 2} in {1, frozenset({2, 3})}) # True, True, because the contents {3,2} are considered equal between sets {3,2} = frozenset{{2,3}}