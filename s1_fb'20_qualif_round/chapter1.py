import sys
sys.stdin=open("input.in","r")
sys.stdout=open("output.out","w") 


# number of test case
t = int(input())
for _ in range(t):
	N,K,W = map(int,input().split())

	# contains southwest corner of rooms
	left_corner = list(map(int,input().split()))

	# constants for generating full data set of left_corner
	al,bl,cl,dl = map(int,input().split())
	
	# contains height of rooms
	height = list(map(int,input().split()))

	# constants for generating full data set of height
	ah,bh,ch,dh = map(int,input().split())

	# firstly generate full data set of left_corner and height
	for i in range(K,N):
		l = ((al*left_corner[i-2] + bl*left_corner[i-1] + cl) % dl) + 1
		left_corner.append(l)

		h = ((ah*height[i-2] + bh*height[i-1] + ch) % dh) + 1
		height.append(h)
	# main logic starts here
	# will use some kind DP concept and what to do depends on the position
	# consecutive rooms 

	# contains perimeter of union of rooms i.e Pi = union of (r1...ri)
	p = []

	mod = 1000000007
	ans = 1

	# this is for storing height of visited rooms 
	d = {}

	for i in range(N):
		if i == 0:
			# appending perimeter of first room  
			p.append(2*(W+height[i]))

			# updating the height from left corner to right corner 
			# so that we can easily use this height in finding the extra portion
			for j in range(left_corner[i],left_corner[i]+W+1):
				d[j] = height[i]
		else:
			# check previous's southeast corner is present on next room's south wall
			if left_corner[i-1] + W >= left_corner[i]:

				# in this case some part between the rooms is shared so we will be adding only extra 
				# part in the perimeter 
				w_extra = left_corner[i] - left_corner[i-1]
				h_extra = max(0,height[i] - d[left_corner[i]])
				p.append(p[-1] + 2*(w_extra+h_extra))
			else:

				# now this very simple case two rooms which aren't sharing any part 
				# so we have to add whole perimeter of current room to the previous
				p.append(p[-1] + 2*(W + height[i]))	

			temp = dict(d)
			d = {}
			j = left_corner[i]
			while j <= left_corner[i] + W:
				if j not in temp:
					d[j] = height[i]
				else:
					d[j] = max(temp[j],height[i])
				j += 1
		ans = (ans*(p[-1]%mod))%mod 

	print("Case #{}: {}".format(_+1,ans)) 
	# print(p)



