# reverse_a_string

str = "iamtheking"

# str[start:stop:step]
print(str[::-1])

i = 1
while i in range(len(str)+1):
  print(str[-i])
  i += 1

# Output:
#
# gnikehtmai
# g
# n
# i
# k
# e
# h
# t
# m
# a
# i