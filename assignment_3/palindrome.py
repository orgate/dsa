###################################################################
#																  #
#	Title			:	Finding the next least palindrome number  #
#	Author			:	Alfred Ajay Aureate R					  #
#	Roll No			:	EE10B052								  #
#	Course			:	EE4371 - Data Structures and Algorithms	  #
#	Assignment No	:	3										  #
#																  #
###################################################################


import sys

# Class used for stack related operations
class stackclass:

	# The actual stack used is initiated
	# below

	stack = []


	# This function initializes the stack
	# when class is initiated
	# The syntax is in-built in Python

	def __init__(self):
		self.stack = []


	# This function gives the length of the
	# stack when length of class is called
	# The syntax is in-built in Python

	def __len__(self):
		return len(self.stack)


	# This function pushes an element to the
	# top or the end of stack

	def stack_push(self,element):
		self.stack.append(element)
		return self.stack


	# This function pops the top or the last element
	# from the stack

	def stack_pop(self):	
		return self.stack.pop()


# This function checks whether the given string could be
# converted to a floating point number or not

def float_check(value):
	try:
		float(value)
		return True
	except ValueError:
		return False


# This function checks whether the given string is a
# non-negative integer or not

def pos_int_check(value):
	try:
		int(value)
		if int(value)>=0:
			return True
		else:
			return False
	except ValueError:
		return False


# This function checks whether the given string could be
# converted to a list or not

def list_check(string):
	try:
		list(string)
		return True
	except ValueError:
		return False




i=0
count = 0

# This loop reads every line, from a given text file till
# the last line

for expr in sys.stdin.readlines():

#	print "here"
#	err_flag = 0
#	pal_numb_flag = 0


#	# This parses a line removing all spaces and stores the
#	# whole set of symbols or numbers belonging to a line
#
#	input_list = expr.split()

###	if pos_int_check(expr):
###		numb = int(expr)
###		numb_str = str(numb)
###	else:
###		err_flag = 1

##	if expr[-1]=='\n':
##		numb_str = expr.replace('\n','')
##	else:
##		numb_str = expr

	numb_str = expr[0:-1]
#		break

	out_str = ''

	if i==0:
		count = int(expr)
	
	if (i==count+1):
		break

##	if list_check(numb_str):
##		numb_list = list(numb_str)

#	a = sys.getline()
	
	l = len(numb_str)
	j=0
#	num = a
#	stck1 = stackclass()
#	stck2 = stackclass()

#	print numb_str[j/2] + "hi",l

	if (l%2==0)&(i!=0):

#		out_str = ''
		half_len = (l/2)
		zeros = ''
		pal_elm = numb_str[half_len-1]

		if numb_str[(half_len-1)::-1]<=numb_str[half_len:]:
			while j<half_len:
				if(numb_str[half_len-j-1]=='9'):
					zeros+='0'
				else:
					pal_elm = str(int(numb_str[half_len-j-1])+1)
					break
				
#				else:
#					numb_str = numb_str[0:(half_len-j-1)] + temp + numb_str[(-half_len-2)::-1]
					
		
#			if (numb_str[(l/2)-j-1]!=numb_str[(l/2)+j])&(pal_numb_flag!=1):
###				if numb_str[half_len-j-1]!=numb_str[half_len+j]:
###					if numb_str[half_len-j-1]<numb_str[half_len+j]:
###						temp = str(int(numb_str[half_len-1])+1)
###						out_str = numb_str[0:(half_len-1)] + temp + temp + numb_str[(-half_len-2)::-1]
###						break
###					else:
#					temp = numb_str[(l/2)-j-1]
###						out_str = numb_str[0:half_len] + numb_str[(-half_len-1)::-1]
###						break
##				numb_list[(l/2)+j] = str(max(int(numb_list[(l/2)+j]),int(numb_list[(l/2)-j-1])))
#				print "1 " + numb_list[(l/2)+j]
##				numb_list[(l/2)-j-1] = str(max(int(numb_list[(l/2)+j]),int(numb_list[(l/2)-j-1])))
#				print "2 " + numb_list[(l/2)-j-1]
##				pal_numb_flag = 1
##			elif (numb_str[(l/2)-j-1]!=numb_str[(l/2)+j])&(pal_numb_flag==1):
##				temp = numb_str[(l/2)-j-1]
###				else:
###					temp = numb_str[half_len-j-1]
#				print "3 " + numb_list[(l/2)+j]
			
###					out_str = out_str.join(temp+temp)

#			print out_str

#			rem1 = num%10
#			num = num/10
#			
#			rem2 = num/(10**(l-1))
#			num = num%(10**(l-1))
#			l-=2

				j+=1

#		if (pal_numb_flag==0)&(out_str[0]=='9'):
#			out_str = '0'
#			j1=0
#			while j1<((l-2)/2):
#				out_str = out_str.join('0'+'0')
#				j1+=1
#			out_str = out_str.join('1'+'1') 
			
		if l==2:			
			print pal_elm + zeros + zeros + pal_elm
		elif j==half_len:
			print '10' + zeros[:-1] + zeros[:-1] + '1'
		else:
			print numb_str[0:(half_len-j-1)] + pal_elm + zeros + zeros + pal_elm + numb_str[(half_len-2-j)::-1]
	
	elif (i!=0):

		half_len = ((l-1)/2)
#		out_str = numb_str[half_len]

		zeros = numb_str[half_len]
		pal_elm = ''

		if numb_str[(half_len-1)::-1]<=numb_str[(half_len+1):]:
			while j<=half_len:
				if(numb_str[half_len-j]=='9'):
					if j!=0:
						zeros=zeros.join('0'+'0')
					else:
						zeros = '0'
				else:
					if j!=0:
						pal_elm = str(int(numb_str[half_len-j])+1)
					else:
						zeros = str(int(numb_str[half_len-j])+1)
					break

###		while j<half_len:
		
##			if (numb_str[((l-1)/2)+j+1]!=numb_str[((l-1)/2)-j-1])&(pal_numb_flag!=1):
###			if numb_str[half_len+j+1]!=numb_str[half_len-j-1]:
###				if (numb_str[half_len-j-1]<numb_str[half_len+j+1]):
###					temp = str(int(numb_str[half_len])+1)

###					out_str = numb_str[0:((l-1)/2)] + temp + numb_str[(-half_len-2)::-1]
###					break
###				else:
##					temp = numb_str[((l-1)/2)-j-1]
###					temp = str(int(numb_str[half_len]))
###					out_str = numb_str[0:half_len] + temp + numb_str[(-half_len-2)::-1]
###					break
					
##				numb_list[((l-1)/2)+j+1] = str(max(int(numb_list[((l-1)/2)+j+1]),int(numb_list[((l-1)/2)-j-1])))
#				print "4 " + numb_list[((l-1)/2)+j+1]
##				numb_list[((l-1)/2)-j-1] = str(max(int(numb_list[((l-1)/2)+j+1]),int(numb_list[((l-1)/2)-j-1])))
#				print "5 " + numb_list[((l-1)/2)-j-1]
#				pal_numb_flag = 1
##			elif (numb_str[((l-1)/2)+j+1]!=numb_str[((l-1)/2)-j-1])&(pal_numb_flag==1):
##				temp = numb_str[((l-1)/2)-j-1]
#				print "6 " + numb_list[((l-1)/2)+j+1]
###			else:
###				temp = numb_str[half_len-j-1]

###				out_str = out_str.join(temp+temp)
#			print out_str		 

#			rem1 = num%10
#			num = num/10
#			
#			rem2 = num/(10**(l-1))
#			num = num%(10**(l-1))
#			l-=2
				j+=1

		if l==1:
			print str(int(zeros)+1)
		elif j==half_len+1:
			print '1' + zeros[:-1] + '1'
		else:
			print numb_str[0:(half_len-j)] + pal_elm + zeros + pal_elm + numb_str[(half_len-j-1)::-1]


#		if (pal_numb_flag==0)&(out_str[0]=='9'):
#			out_str = ''
#			j2=0
#			while j2<((l-1)/2):
#				out_str = out_str.join('0'+'0')
#				j2+=1
#			out_str = out_str.join('1'+'1') 



#	# Initializing the output list that would temporarily
#	# contain the output expression in the form of list
#
#	outputlist = []
	
	                 
#	# Initializing the input symbol counter
#
#	k=0
	
#	print i

	# Prints "ERROR" if error flag is 1

###	if i!=0:
###		if err_flag==1:
###			print "ERROR"


		# Otherwise, it joins and converts the output list into
		# an expression with spaces and prints it	
	
###		else:
#			print ''.join(a for a in numb_list)
#			print numb_str
###			print out_str

	i+=1

	# THE END


