def f(xs):
	return #配列xsに格納されるx_1からx_nを引数に持つ関数
	
def bibun(xs): #x1から順に偏微分して配列に格納
	before_xs=xs.copy()
	ans=[]
	h=0.000000001

	for i in range(len(xs)):
		xs[i]+=h
		ans.append((f(xs)-f(before_xs))/h)
		xs[i]-=h
	return ans
