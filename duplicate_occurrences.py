# Find duplicate occurrence
# Input = [1,2,3,2,4,5,4,5] output = [2,4,5]

class ArrayPractice:
  @staticmethod
  def find_duplicate_occurrences(list_of_elements):
      dic = {}
      for element in list_of_elements:
          if element not in dic:
              dic[element] = 1
          else:
              dic[element] += 1
      duplicate_occurrences = []
      for element, occurrences  in dic.items():
          if occurrences > 1:
              duplicate_occurrences.append(element)
      return duplicate_occurrences

list_of_elements = [1,2,3,2,4,5,4,5]
ap = ArrayPractice()
print(ap.find_duplicate_occurrences(list_of_elements))