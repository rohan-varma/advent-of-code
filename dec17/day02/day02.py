

def checksum(matrix):
	return sum([max(li) - min(li) for li in matrix])

if __name__ == '__main__':
	lines = open('input.txt').readlines()
	matrix = [ [int(x) for x in line.split()] for line in lines]
	print(checksum(matrix))