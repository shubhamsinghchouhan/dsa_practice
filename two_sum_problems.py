# nums = [3,4,5,6], target = 7
# Given an array of integers nums and an integer target, 
# return the indices i and j such that nums[i] + nums[j] == target and i != j.
#
# input = [3,5,6,1]
# # print(dict(input))
#
# dic = {}
# i = 0
# target = 7
# for element in input:
#   dic[element] = i
#   i += 1
# print(dic)
#
# j = 0
# for first_element in input:
#   second_element = target - first_element
#   if (dic.get(second_element)):
#     print([j, dic[second_element]])
#     break
#   j += 1

# 
# n^2
# nlog(n)


# Output:
#
# {3: 0, 5: 1, 6: 2, 1: 3}
# [2, 3]