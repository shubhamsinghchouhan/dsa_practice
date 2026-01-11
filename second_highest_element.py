import sys
class ArrayPractice:
    @staticmethod
    def second_highest_element(input):
      max_ele = -sys.maxsize - 1
      sec_max_ele = -sys.maxsize - 1
      for element in input:
        if element > max_ele:
          max_ele = element
      for element in input:
        if element != max_ele:
          if element > sec_max_ele:
            sec_max_ele = element
      print("max_ele", max_ele, "sec_max_ele", sec_max_ele)


input = [4,11,7,5,1,2]
# Output:
#
# max_ele 11 sec_max_ele 7
ArrayPractice.second_highest_element(input)