# Reads the input.txt file
h = open('input1.txt', 'r')
content = h.readlines()

# Initializes nums
nums = []

# Appends the inputs into nums
for line in content:
	nums.append(int(line))

result = []
n = len(nums)

# Creates an array of basically "I" for increases
# and "D" for decreases then counts number of "I"s
for i in range(n - 1):
	if nums[i] < nums[i+1]:
		result.append("I")
	else:
		result.append("D")

# Get result
print(result.count("I"))
	