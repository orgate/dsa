import sys

expr = ['']
i=1
j=1
#stck = []
#err_flag=0

def str2num(numb_string):
##	numb_string = stack[k]
	
##	ind1 = 0
##	ind2 = 0
##	ind3 = 0
##	ind4 = 0

##	if '+' in numb_string:
##		ind1 = numb_string.index('+')
##	if '-' in numb_string:
##		ind2 = numb_string.index('-')
##	if '*' in numb_string:
##		ind3 = numb_string.index('*')
##	if '/' in numb_string:
##		ind4 = numb_string.index('/')
	
##	if (ind1!=0)|(ind2!=0)|(ind3!=0)|(ind4!=0):
##		stack = "ERROR"
##		return stack

	numb = 0.0
	if numb_string[0]=='-':
		numb_string = numb_string.replace('-','')
		flag=1
	elif numb_string[0]=='+':
		numb_string = numb_string.replace('+','')
		flag=0
	elif (numb_string[0]=='*')|(numb_string[0]=='/')|(numb_string[0]=='.'):
		flag=0
	else:
		flag=0
	
	if '.' in numb_string:
		dec = numb_string.index('.')
		l=0
		while l<dec:
			numb+=(ord(numb_string[l])-48)*(10**(dec-1-l))
			l+=1
###		while (l<(len(numb_string)-1))&(l>=dec):
		while (l<min((len(numb_string)-1),(dec+5)))&(l>=dec):
			numb+=(ord(numb_string[l+1])-48)*(10**(dec-1-l))
			l+=1
		if flag==0:
##			stack[k] = numb
			return numb
		else:
			flag=0
#			stack[k] = -numb
			return (-numb)

	else:
		l=0
		while l<len(numb_string):
			numb+=(ord(numb_string[l])-48)*(10**(len(numb_string)-l-1))
			l+=1
		if flag==0:
#			stack[k] = numb
			return numb
		else:
			flag=0
#			stack[k] = -numb
			return (-numb)

##def check4char(char):
##	return not(((ord(char)>=48)&(ord(char)<=57))|(char=='+')|(char=='-')|(char=='*')|(char=='/')|(char=='.'))
		

def add(stack,index):
	if index>=2:			
		stack[index-2] = stack[index-2]+stack[index-1]
		stack.remove(stack[index])
		stack.remove(stack[index-1])
	else:
		stack = ["ERROR"] # modified
	return stack

def sub(stack,index):
	if index>=2:			
		stack[index-2] = stack[index-2]-stack[index-1]
		stack.remove(stack[index])
		stack.remove(stack[index-1])
	else:
		stack = ["ERROR"] # modified
	return stack

def mul(stack,index):
	if index>=2:			
		stack[index-2] = stack[index-2]*stack[index-1]
		stack.remove(stack[index])
		stack.remove(stack[index-1])
	else:
		stack = ["ERROR"] # modified
	return stack

def div(stack,index):
	if (index>=2)&(stack[index-1]!=0):			
		stack[index-2] = stack[index-2]/stack[index-1]
		stack.remove(stack[index])
		stack.remove(stack[index-1])
	else:
		stack = ["ERROR"] # modified
	return stack


while expr[i-1]!='\n':
	expr.append(sys.stdin.readline())
	i+=1
# for debugging
#print expr

while j<i-1:
	stck = expr[j].split()
	k=0
	res = ['']
#	err_flag = 0
	
#	print stck # for debugging
#	print "err_flag is ",err_flag # for debugging

	while k<len(stck):
		l=0
		
#		print "initially"		# for debugging
#		print stck[k]		# for debugging

##		while (l<len(stck[k]))&(type(stck[k])!=float):

#			print stck[k] # for debugging

##			if check4char(stck[k][l]):
##				err_flag = 1
#				print stck[k][l] # for debugging
##			l+=1

#		print stck # for debgging

##		if err_flag==1:
##			stck = "ERROR"
		if stck[0]=="ERROR":   # added instead of err_flag
			stck = ["ERROR"] # modified
		elif stck[k]=='+':  
			stck = add(stck,k)
##			if err_flag!=1:
			k-=2
		elif stck[k]=='-':
			stck = sub(stck,k)
##			if err_flag!=1:
			k-=2
		elif stck[k]=='*':
			stck = mul(stck,k)
##			if err_flag!=1:
			k-=2
		elif stck[k]=='/':
			stck = div(stck,k)
##			if err_flag!=1:
			k-=2
		else:
#			if ('+' in stck[k])|('-' in stck[k])|('*' in stck[k])|('/' in stck[k]):
#				if stck[k][0]!='+'

			stck[k] = str2num(stck[k])

		k+=1

	if (len(stck)!=1)|(stck[0]=="ERROR"):
		print "ERROR"
	else:
		print ("%.4f" %stck[0])

	j+=1

