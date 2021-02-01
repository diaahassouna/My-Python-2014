def maxmin(x,x2,step=1):
	while x<x2:
		x=x+step
		y=4*x**3-120*x**2+900*x
		xa=x-step                      #xa is behind x by one step
		ya=4*xa**3-120*xa**2+900*xa    #ya is behind y by one step
		xb=xa+2*step                   #xb is front of x by one step
		yb=4*xb**3-120*xb**2+900*xb    #yb is front of y by one step
		if ya<y and yb<y:
			print 'y(max) =', y
			print 'x[y(max)] =', x
		if ya>y and yb>y:
			print 'y(min) =', y
			print 'x[y(min)] =', x
