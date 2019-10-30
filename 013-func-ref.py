
def lesen():
	print("schmoeker")
	
def essen():
	print("mjam")
	
todo = {
	'buch': lesen,
	'obst': essen,
	}

todo['buch']()
