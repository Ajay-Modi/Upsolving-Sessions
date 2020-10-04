for _ in range(int(input())):
	# number of tree Eva has assigned
	n=int(input())
	l=[]
	# collecting position and height of each tree

	for i in range(n):
		l.append(list(map(int,input().split())))
	# sorting trees according to there position 
	l.sort()
	ma=0
	s=set()
	d={}
	for i in range(n):
		# left position of tree when fall
		x=l[i][0]-l[i][1]
		ma=max(ma,l[i][1])
		# right position of tree when fall
		y=l[i][0]+l[i][1]
		if l[i][0] in s:
			ma=max(ma,d[l[i][0]]+l[i][1])
			if y in d:
				d[y]=max(d[l[i][0]]+l[i][1],d[y])
			else:
				d[y]=d[l[i][0]]+l[i][1]
			s.add(y)
		else:
			s.add(y)
			if y in d:
				d[y]=max(l[i][1],d[y])
			else:
				d[y]=l[i][1]
		if x in s:
			ma=max(ma,d[x]+l[i][1])
			s.add(l[i][0])
			if l[i][0] in d:
				d[l[i][0]]=max(d[x]+l[i][1],d[l[i][0]])
			else:
				d[l[i][0]]=d[x]+l[i][1]
		else:
			s.add(l[i][0])
			if l[i][0] in d:
				d[l[i][0]]=max(l[i][1],d[l[i][0]])
			else:
				d[l[i][0]]=l[i][1]
	print("Case #%d: %d"%(_+1,ma))
