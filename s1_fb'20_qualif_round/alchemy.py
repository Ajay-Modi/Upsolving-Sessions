# import sys
# sys.stdin=open("input.in","r")
# sys.stdout=open("output.out","w") 

t = int(input())
for _ in range(t):
	n = int(input())
	shards = input()
	result_shards = 0

	for i in shards:
		if i == "A":
			result_shards += 1
		else:
			result_shards -= 1

	if abs(result_shards) == 1:
		ans = "Y"
	else:
		ans = "N"

	print("Case #{}: {}".format(_+1,ans))
