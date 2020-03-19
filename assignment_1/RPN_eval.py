import sys

i=1
j=1

def float_check(value):

	try:
		float(value)
		return True
	except ValueError:
		return False


for expr in sys.stdin.readlines():
	stck = expr.split()
	k=0
	err_flag = 0
	while k<len(stck):
		op_flag = 0
		
		if err_flag==1:   # added instead of err_flag # err_flag again added
			stck = ["ERROR"] # modified remodified
		elif float_check(stck[k]):
			stck[k] = float(stck[k])
		else:
			
			if stck[k]=='+':  
				if k>=2:			
					stck[k-2] = stck[k-2]+stck[k-1]
					op_flag = 1
				else:
					err_flag = 1 # modified remodified
			elif stck[k]=='-':  
				if k>=2:			
					stck[k-2] = stck[k-2]-stck[k-1]
					op_flag = 1
				else:
					err_flag = 1 # modified remodified
			elif stck[k]=='*':  
				if k>=2:			
					stck[k-2] = stck[k-2]*stck[k-1]
					op_flag = 1
				else:
					err_flag = 1 # modified remodified
			elif stck[k]=='/':  
				if (k>=2)&(stck[k-1]!=0):			
					stck[k-2] = stck[k-2]/stck[k-1]
					op_flag = 1
				else:
					err_flag = 1 # modified remodified

			if op_flag==1:
				dum=stck.pop(k)
				dum=stck.pop(k-1)
				k-=2

			if (float_check(stck[k]))&(err_flag!=1):
				stck[k] = float(stck[k])
			else:
				stck = ["ERROR"]				
				err_flag = 1
				break

		k+=1
	if stck==[]:
		print ""
	elif (len(stck)!=1)|(stck==["ERROR"])|(err_flag==1):
		print "ERROR"
	else:
		print ("%.4f" %stck[0])

	j+=1

