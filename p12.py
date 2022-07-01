# Reads the input.txt file
h = open('input1.txt', 'r')
content = h.readlines()

# Initializes nums
nums = []

# Appends the inputs into nums
for line in content:
	nums.append(int(line))

# Initializes variables
count = 0
n = len(nums)

# Initializes window
window_sum = sum(nums[:3])

# Compute sums of sliding window
# change compare_sum to previous window_sum
# if the new sum is larger then increase
# count by 1
for i in range(n - 3):
	compare_sum = window_sum
	window_sum = window_sum - nums[i] + nums[i + 3]
	if compare_sum < window_sum:
		count += 1

# Get result
print(count)
