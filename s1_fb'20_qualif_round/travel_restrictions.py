for _ in range(int(input())):
	n=int(input())
	incom=list(input())
	outcom=list(input())
# 	dp for calculating answer
	ans=[["" for i in range(n)] for j in range(n)]
	for i in range(n):
		ans[i][i]="Y"
		for j in range(i-1,-1,-1):
			if ans[i][j+1]=="Y":
				if incom[j]=="Y" and outcom[j+1]=="Y":
					ans[i][j]="Y"
				else:
					ans[i][j]="N"
			else:
				ans[i][j]="N"
		for j in range(i+1,n):
			if ans[i][j-1]=="Y":
				if incom[j]=="Y" and outcom[j-1]=="Y":
					ans[i][j]="Y"
				else:
					ans[i][j]="N"
			else:
				ans[i][j]="N"
	print("Case #%d: "%(_+1))
	for i in ans:
		print("".join(i))
