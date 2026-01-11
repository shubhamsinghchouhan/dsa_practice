# Find the first occurrences of 1 in sorted stream of zeros and ones
arr = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]

class ArrayOperations:
    @staticmethod
    def find_first_occurrences(arr):
        # mid = len(arr)//2
        # if (arr[mid] == 0):   # check right
        #   find_first_occurrences(arr[mid+1:])
        # elif (arr[mid] == 1): # check left
        #   find_first_occurrences(arr[:mid-1])

        # print(mid)
        low = 0
        high = len(arr) - 1
        result = -1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == 1:
                result = mid  # Potential answer
                high = mid - 1  # Keep looking left to see if there's an earlier '1'
            else:
                low = mid + 1  # Look right

        return result


print(ArrayOperations.find_first_occurrences(arr))