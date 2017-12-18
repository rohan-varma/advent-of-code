


def get_sum(digits):
	running_sum = 0
	cur = digits[0]
	i = 0
	while i + 1 < len(digits):
		if digits[i+1] == cur:
			running_sum+=int(cur)
		else:
			cur = digits[i+1]
		i+=1
	# compare the last
	if digits[-1] == digits[0]:
		running_sum+=int(digits[0])
	return running_sum

if __name__ == '__main__':
	# parse input from input.txt
	digit_str = open('input.txt').read()
	assert get_sum('1122') == 3
	assert get_sum('1111') == 4
	assert get_sum('1234') == 0
	assert get_sum('91212129') == 9
	print('all basic tests passed')
	print(get_sum(digit_str))