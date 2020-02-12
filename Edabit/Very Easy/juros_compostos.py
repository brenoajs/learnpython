def compound_interest(m, c, i, t):
	m = c*(1+i)**t
	print(m)
	return m 

compound_interest(100000, 20, 0.15, 365)