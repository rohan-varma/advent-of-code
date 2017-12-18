
if __name__ == '__main__':
	print(sum([max(li) - min(li) for li in [[int(x) for x in line.split()] for line in open('input.txt').readlines()]]))