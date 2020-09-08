# import sys
# sys.stdin=open("input.in","r")
# sys.stdout=open("output.out","w")

t = int(input())
for _ in range(t):
	n = int(input())  # total number of countries
	I = input()		  
	O = input()

	output = [["N"]*n for i in range(n)]

	for i in range(n):
		output[i][i] = "Y"

		# covering first half 
		p = i-1
		while p > -1:
			if O[p+1] == "Y" and I[p] == "Y":
				output[i][p] = "Y"
			else:
				break
			p -= 1

		# Covering second half 
		p = i+1
		while p < n:
			if O[p-1] == "Y" and I[p] == "Y":
				output[i][p] = "Y"
			else:
				break
			p += 1

	# Printing output in required format
	print("Case #{}:".format(_+1))
	for i in output:
		print("".join(i))
