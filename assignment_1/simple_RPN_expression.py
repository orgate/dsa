expr = [0]
res  = [0]
i=1
j=1

while expr[i-1]!="":
	expr.append(raw_input())
	i+=1

while j<i-1:
	k=0
	stck = []
	err_flag = 0
	temp_stck = ''
	flag = 0
	while k<len(expr[j]):
		if expr[j][k]==' ':
			if len(temp_stck)!=0:
				numb = 0.0
				if '.' in temp_stck:
					dec = temp_stck.index('.')
					l=0
					while l<dec:
						numb+=(ord(temp_stck[l])-48)*(10**(dec-1-l))
						l+=1
					while (l<(len(temp_stck)-1))&(l>=dec):
						numb+=(ord(temp_stck[l+1])-48)*(10**(dec-1-l))
						l+=1
				else:
					l=0
					while l<len(temp_stck):
						numb+=(ord(temp_stck[l])-48)*(10**(len(temp_stck)-l-1))
						l+=1
				if flag==0:
					stck.append(numb)
				if flag==1:
					stck.append(-numb)
					flag = 0
				temp_stck = ''

		if expr[j][k]=='-':
			if (expr[j][k-1]==' ')|(k==0):
				flag = 1
			else:
				err_flag = 1

		if (ord(expr[j][k])>=48)&(ord(expr[j][k])<=57): 
			temp_stck = temp_stck + expr[j][k]
		if expr[j][k]=='.':
			temp_stck = temp_stck + '.'



		if expr[j][k]=='+':
			if len(stck)>=2:			
				stck[-2] = stck[-2]+stck[-1]
				stck.remove(stck[-1])
			else:
				err_flag = 1
				stck = []
		if expr[j][k]=='-':
			if len(stck)>=2:			
				stck[-2] = stck[-2]-stck[-1]
				stck.remove(stck[-1])
				flag = 0
			elif flag==1:
				temp=1 
			else:
				err_flag = 1
				stck = []
		if expr[j][k]=='*':
			if len(stck)>=2:			
				stck[-2] = stck[-2]*stck[-1]
				stck.remove(stck[-1])
			else:
				err_flag = 1
				stck = []
		if expr[j][k]=='/':
			if len(stck)>=2:			
				stck[-2] = stck[-2]/stck[-1]
				stck.remove(stck[-1])
			else:
				err_flag = 1
				stck = []
		k+=1



	if ((len(stck)!=1)&(temp_stck==''))|(err_flag==1):
		res.append("ERROR")
	elif temp_stck!='':
		res.append(temp_stck)
	else:
		res.append(stck[0])

	err_flag = 0

	if res[j]=="ERROR":
		print "ERROR"
	elif temp_stck!='':
		if flag==1:
			print "-"+temp_stck
		else:
			print temp_stck
	else:
		print ("%.4f" %res[j])
	
	j+=1

