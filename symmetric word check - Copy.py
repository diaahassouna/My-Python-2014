def sym(x):
	if x=='':
		return 'Empty word , can\'t solve'
	n=0
	m=-1
	while n>0:
		n+=1
		m-=1
	return x[n]==x[m]