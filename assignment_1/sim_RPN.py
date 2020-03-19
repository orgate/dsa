import sys

expr = ['']
i=1
j=1
flag = 0



def float_check(value):

	try:
		float(value)
		return True
	except ValueError:
		return False



##def str2num(numb_string):

##	numb = 0.0
##	if numb_string[0]=='-':
##		numb_string = numb_string.replace('-','')
##		flag=1
##	elif numb_string[0]=='+':
##		numb_string = numb_string.replace('+','')
##		flag=0
##	else:
##		flag = 0
##	
##	if '.' in numb_string:
##		dec = numb_string.index('.')
##	l=0
##		while l<dec:
##			numb+=(ord(numb_string[l])-48)*(10**(dec-1-l))
##			l+=1
##		while (l<min((len(numb_string)-1),(dec+5)))&(l>=dec):
##			numb+=(ord(numb_string[l+1])-48)*(10**(dec-1-l))
##			l+=1
##		if flag==0:
##			return numb
##		else:
##			flag=0
##			return (-numb)
##
##	else:
##		l=0
##		while l<len(numb_string):
##			numb+=(ord(numb_string[l])-48)*(10**(len(numb_string)-l-1))
##			l+=1
##		if flag==0:
##			return numb
##		else:
##			flag=0
##			return (-numb)

while expr[i-1]!='\n':
	expr.append(sys.stdin.readline())
	i+=1

while j<i-1:
	stck = expr[j].split()
	k=0
	res = ['']
	err_flag = 0

	while k<len(stck):
		l=0
		
		if err_flag==1:   # added instead of err_flag # err_flag again added
			stck = ["ERROR"] # modified remodified
		elif type(stck[k])==float:
			stck[k] = stck[k]
		else:
			if '+' in stck[k]:  
				if (k>=2)&(len(stck[k])==1):			
					stck[k-2] = stck[k-2]+stck[k-1]
					stck.remove(stck[k])
					stck.remove(stck[k-1])
					k-=2
#					break
				else:
					err_flag = 1 # modified remodified
#				break
#				k-=2
			if type(stck[k])==float:
				stck[k] = stck[k]
			elif '-' in stck[k]:  
				if (k>=2)&(len(stck[k])==1):			
					stck[k-2] = stck[k-2]-stck[k-1]
					stck.remove(stck[k])
					stck.remove(stck[k-1])
					k-=2
#					break
				else:
					err_flag = 1 # modified remodified
#				break
#				k-=2
			if type(stck[k])==float:
				stck[k] = stck[k]
			elif '*' in stck[k]:  
				if (k>=2)&(len(stck[k])==1):			
					stck[k-2] = stck[k-2]*stck[k-1]
					stck.remove(stck[k])
					stck.remove(stck[k-1])
					k-=2
#					break
				else:
					err_flag = 1 # modified remodified
#				break
#				k-=2
			if type(stck[k])==float:
				stck[k] = stck[k]
			elif '/' in stck[k]:  
				if (k>=2)&(stck[k-1]!=0)&(len(stck[k])==1):			
					stck[k-2] = stck[k-2]/stck[k-1]
					stck.remove(stck[k])
					stck.remove(stck[k-1])
					k-=2
#					break
				else:
					err_flag = 1 # modified remodified
#				break
#				k-=2

#			print "else loop ",stck

			if (float_check(stck[k]))&(err_flag!=1):
				stck[k] = float(stck[k])
			else:
				stck = ["ERROR"]				
				err_flag = 1

##			if type(stck[k])==float:
##				stck[k] = stck[k]
##			elif (('0' in stck[k])|('1' in stck[k])|('2' in stck[k])|('3' in stck[k])|('4' in stck[k])|('5' in stck[k])|('6' in stck[k])|('7' in stck[k])|('8' in stck[k])|('9' in stck[k]))&(err_flag!=1):
##				if (((ord(char)>=48)&(ord(char)<=57))|(char=='+')|(char=='-')|(char=='*')|(char=='/')|(char=='.')):			
##					stck[k] = str2num(stck[k])
##				else:
##					err_flag = 1
##			else:
##				stck = ["ERROR"] # added 
	
		k+=1

	if (len(stck)!=1)|(stck[0]=="ERROR")|(err_flag==1):
		print "ERROR"
	else:
		print ("%.4f" %stck[0])

	j+=1

