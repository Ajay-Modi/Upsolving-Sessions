# import sys
# sys.stdin=open("input.in","r")
# sys.stdout=open("output.out","w") 

# number of test case
t = int(input()) 

for _ in range(t):

	# number of tree Eva has assigned
	n = int(input()) 

	pos_hth = []

	# collecting position and height of each tree
	for i in range(n):
		pos,hth = map(int,input().split())
		pos_hth.append((pos,hth))

	# arrange them in ascending order W.R.T position of trees
	pos_hth.sort()

	# will Dp to find out the largest timber interval 
	# we will be storing maximum length of interval for each tree using dict
	
	dp = {}

	for i in range(n):
		curr = pos_hth[i][0]	

		# here we covered the case if tree fell towards right after chopped 
		if curr+pos_hth[i][1] not in dp:
			if curr not in dp:
				dp[curr+pos_hth[i][1]] = pos_hth[i][1]
			else:
				dp[curr+pos_hth[i][1]] = pos_hth[i][1] + dp[curr]

		else:
			if curr not in dp:
				dp[curr+pos_hth[i][1]] = max(pos_hth[i][1], dp[curr+pos_hth[i][1]])
			else:
				dp[curr+pos_hth[i][1]] = max(pos_hth[i][1] + dp[curr], dp[curr+pos_hth[i][1]])

		# remaning case which if tree fell left side

		if curr-pos_hth[i][1] not in dp:
			if curr not in dp:
				dp[curr] = pos_hth[i][1]
			else:
				dp[curr] = max(dp[curr],pos_hth[i][1])

		else:
			if curr not in dp:
				dp[curr] = dp[curr-pos_hth[i][1]]+pos_hth[i][1]
			else:
				dp[curr] = max(dp[curr],dp[curr-pos_hth[i][1]]+pos_hth[i][1])

	ans = max(dp.values())
	# format answer as required 
	print("Case #{}: {}".format(_+1,ans))